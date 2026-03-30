**Author:** Emilia Jovanovic  
**Course:** Machine Learning  
**Lab:** Lab 1 – Content‑Based Recommender System  

# Introduction

In this lab, I built a content‑based movie recommender system using the MovieLens dataset.

The goal was to:
- load and clean the data
- combine genres and tags
- create a TF‑IDF model
- calculate similarity between movies
- recommend movies based on a given title

The main idea is to use text information to find movies that are similar

## Dataset

I used the MovieLens **ml-latest** dataset, which includes:

| File        | Description              |
|-------------|--------------------------|
| movies.csv  | Movie titles and genres  |
| ratings.csv | User ratings             |
| tags.csv    | User‑generated tags      |

Since the dataset is large, I filtered out movies with very few ratings.

## Method

### Data preprocessing

To prepare the data, I cleaned genres and tags, merged them into the movies table, and filtered out movies with too few ratings.

### Genres

The `"|"` separators were replaced with spaces so the text works better with TF‑IDF.

### Tags

Tags were cleaned (removing NaN and whitespace) and combined into one string per movie.

### Popularity filter

Only movies with at least 20 ratings were kept to reduce noise.

### Removing empty entries

Movies with no useful text information (no genres and no tags) were removed.

### Weighted text features

Genres are more reliable than tags, so I increased their weight.

### Fuzzy title matching

Movie titles in the dataset can look different from how users type them (for example “Matrix, The”).  
To handle this, I added simple fuzzy matching so the system can still find the right movie even if the title is written differently.  

This includes things like partial matches and ignoring the year in the title.

### TF‑IDF model

I used a TF‑IDF vectorizer to turn the genres and tags into text features for each movie.  
This gives each movie a vector that can be compared with others.

### Similarity calculation

To find similar movies, I calculated the cosine similarity between the selected movie and all others.  
I only compute similarity when needed, which keeps the system fast.

## Results

### Example: “The Matrix”

The system returned the following similar movies:

- Matrix Revolutions, The (2003)
- Thirteenth Floor, The (1999)
- Avalon (2001)
- Matrix Reloaded, The (2003)
- Matrix, The (1999)

These movies share similar themes such as sci‑fi, simulated worlds, and dystopian settings.  
The recommendations make sense and show that the model works well.

## Conclusion

The system can recommend movies based on their genres and tags.  
Weighted features, fuzzy matching, and on‑demand similarity calculations make it both accurate and efficient.  
The project shows how text data can be used to build a simple but effective recommender system.
