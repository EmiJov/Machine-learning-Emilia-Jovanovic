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
