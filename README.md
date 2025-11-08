# TMDB Movie Recommender System
## Project Overview

The TMDB Movie Recommender System is a content-based machine learning project that suggests movies similar to a user’s favorite ones.
It uses movie metadata such as genres, keywords, cast, and crew from the TMDB 5000 Movies Dataset available on Kaggle.

By analyzing the textual and categorical features of movies, the system calculates similarity scores between films and recommends the most relevant ones.

# Objective

To build a system that can:

Recommend movies similar to a given movie title.

Use metadata (not ratings) to find movie similarity.

Demonstrate the use of Natural Language Processing (NLP) and cosine similarity in recommender systems.

# Dataset Information

Dataset Source: TMDB 5000 Movie Dataset on Kaggle

Files Used:

tmdb_5000_movies.csv

tmdb_5000_credits.csv

Key Features:
Column Name	Description
title	Movie title
overview	Plot summary
genres	Movie genres (Action, Drama, etc.)
keywords	Descriptive tags about the movie
cast	Main actors
crew	Includes director and other crew members
popularity	Popularity score of the movie
# Methodology
1. Data Preprocessing

Merged movies and credits datasets on the title column.

Extracted key columns: overview, genres, keywords, cast, and crew.

Converted JSON-like data into readable text.

Combined selected features into a single text field called tags.

2. Text Vectorization

Applied CountVectorizer to convert text into numerical form.

Removed stop words (common English words like “the”, “and”, etc.).

Limited vocabulary to 5000 most frequent words.

3. Similarity Calculation

Computed Cosine Similarity between movie vectors to measure closeness.

Higher cosine value → more similar movies.

4. Recommendation Function

Defined a function to fetch the top 5 most similar movies for any given title.

### Technologies Used

| **Category** | **Tools / Libraries** |
|---------------|------------------------|
| **Language** | Python |
| **Libraries** | pandas, numpy, scikit-learn, ast |
| **Visualization** | matplotlib, seaborn |
| **Text Processing** | CountVectorizer (from `sklearn.feature_extraction.text`) |
| **Similarity Metric** | cosine_similarity |
| **Environment** | Jupyter Notebook  |

