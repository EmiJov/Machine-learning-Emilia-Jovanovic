# --- Imports ---
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import os
import re


# Load the data files
def load_data():
    # Get the folder where this file is located
    base = os.path.dirname(os.path.abspath(__file__))

    # Path to the dataset folder
    data_path = os.path.join(base, "..", "data", "ml-latest")

    movies = pd.read_csv(os.path.join(data_path, "movies.csv"))
    ratings = pd.read_csv(os.path.join(data_path, "ratings.csv"), nrows=1000000)
    tags = pd.read_csv(os.path.join(data_path, "tags.csv"))

    return movies, ratings, tags


# Clean and prepare the data
def preprocess(movies, tags, ratings):
    # Replace "|" in genres with spaces
    movies["genres"] = movies["genres"].str.replace("|", " ", regex=False)

    # Clean up tags
    tags["tag"] = tags["tag"].astype(str).replace("nan", "").str.strip().fillna("")

    # Combine all tags for each movie
    tags_grouped = tags.groupby("movieId")["tag"].apply(
        lambda x: " ".join([str(t) for t in x])
    ).reset_index()

    # Add tags to the movies table
    movies = movies.merge(tags_grouped, on="movieId", how="left")
    movies["tag"] = movies["tag"].fillna("")

    # Keep only movies with enough ratings
    rating_counts = ratings.groupby("movieId")["rating"].count()
    popular_movies = rating_counts[rating_counts >= 20].index
    movies = movies[movies["movieId"].isin(popular_movies)]

    # Remove movies with no useful text info
    movies = movies[
        (movies["genres"] != "(no genres listed)") | (movies["tag"] != "")
    ]

    # Give genres more weight than tags
    movies["text"] = (movies["genres"] + " ") * 3 + movies["tag"]

    movies = movies.reset_index(drop=True)
    return movies


# Try to match the movie title even if the user writes it differently
def fuzzy_match_title(user_title, movies):
    user_title = user_title.lower().strip()

    # Exact match
    exact = movies[movies["title"].str.lower() == user_title]
    if len(exact) > 0:
        return exact["title"].iloc[0]

    # Partial match
    contains = movies[movies["title"].str.lower().str.contains(user_title)]
    if len(contains) > 0:
        return contains["title"].iloc[0]

    # Remove year from the title
    cleaned = re.sub(r"\(\d{4}\)", "", user_title).strip()
    contains = movies[movies["title"].str.lower().str.contains(cleaned)]
    if len(contains) > 0:
        return contains["title"].iloc[0]

    # Ignore words like "the", "a", "an"
    cleaned = cleaned.replace("the ", "").replace("a ", "").replace("an ", "").strip()
    contains = movies[movies["title"].str.lower().str.contains(cleaned)]
    if len(contains) > 0:
        return contains["title"].iloc[0]

    return None


# Build the TF-IDF model
def build_model(movies):
    tfidf = TfidfVectorizer(stop_words="english")
    tfidf_matrix = tfidf.fit_transform(movies["text"])
    return tfidf_matrix


# Recommend similar movies
def recommend(title, movies, tfidf_matrix, n=5):
    # Try to find the correct movie title
    matched_title = fuzzy_match_title(title, movies)

    if matched_title is None:
        return [f"No movie found matching '{title}'"]

    # Get the index of the matched movie
    indices = pd.Series(movies.index, index=movies["title"]).drop_duplicates()
    idx = indices[matched_title]

    # Compare this movie with all others
    sim_scores = cosine_similarity(tfidf_matrix[idx], tfidf_matrix).flatten()

    # Pick the top N most similar movies
    similar_indices = sim_scores.argsort()[::-1][1:n+1]

    return movies["title"].iloc[similar_indices].tolist()


# Run the program
if __name__ == "__main__":
    movies, ratings, tags = load_data()
    movies = preprocess(movies, tags, ratings)
    tfidf_matrix = build_model(movies)

    print("Recommendations for 'The Matrix':")
    print(recommend("The Matrix", movies, tfidf_matrix))