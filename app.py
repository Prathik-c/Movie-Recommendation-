import pickle
import pandas as pd
import streamlit as st
import requests


def fetch_poster(movie_id):
    try:
        url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US"
        response = requests.get(url, timeout=5)
        data = response.json()
        poster_path = data.get('poster_path')
        if poster_path:
            return "https://image.tmdb.org/t/p/w500/" + poster_path
        else:
            return "https://via.placeholder.com/500x750?text=No+Image"
    except Exception:
        return "https://via.placeholder.com/500x750?text=Error+Fetching+Image"


def recommend(movie):
    if movie not in movies['title'].values:
        st.warning("Movie not found in dataset.")
        return [], []
    try:
        index = movies[movies['title'] == movie].index[0]
        distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
        recommended_movie_names, recommended_movie_posters = [], []
        for i in distances[1:6]:
            movie_id = movies.iloc[i[0]].movie_id
            recommended_movie_posters.append(fetch_poster(movie_id))
            recommended_movie_names.append(movies.iloc[i[0]].title)
        return recommended_movie_names, recommended_movie_posters
    except Exception as e:
        st.error(f"Error while recommending: {e}")
        return [], []


st.title("🎬 Movie Recommender System")
st.caption("Get 5 similar movies using Machine Learning and TMDB API")

movies_dict = pickle.load(open('movie_dict.pkl','rb'))
movies = pd.DataFrame(movies_dict)
similarity = pickle.load(open('similarity.pkl','rb'))

movie_list = movies['title'].values
selected_movie = st.selectbox("Select a movie:", movie_list)

if st.button('Show Recommendation'):
    recommended_movie_names, recommended_movie_posters = recommend(selected_movie)
    cols = st.columns(5)
    for idx, col in enumerate(cols):
        if idx < len(recommended_movie_names):
            col.text(recommended_movie_names[idx])
            col.image(recommended_movie_posters[idx], width=150)
