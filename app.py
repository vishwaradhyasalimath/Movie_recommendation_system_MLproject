import streamlit as st
import pickle
import pandas as pd

def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])),reverse=True,key = lambda x: x[1])

    recommend_movies = []
    for i in distances[1:6]:
        recommend_movies.append(movies.iloc[i[0]].title)
    return recommend_movies

movies_dict = pickle.load(open('movie_dict.pkl','rb'))
movies=pd.DataFrame(movies_dict)

similarity=pickle.load(open('similarity.pkl','rb'))

st.title("Movie Recommendation System")

selected_movie_name = st.selectbox(
    "Enter the Movie Name",
    movies['title'].values
)

if st.button('Recommend'):
    recommendations=recommend(selected_movie_name)
    for i in recommendations:
       st.write(i)