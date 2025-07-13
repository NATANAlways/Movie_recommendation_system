import streamlit as st
import pickle
import pandas as pd

def recommed(movie):
  movie_index = movies[movies['title']  == movie].index[0]
  distances = similarity[movie_index]
  movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x:x[1])[1:6]
  
  recommed_movies = []
  for i in movies_list:
    movie_id = i[0]
    # fetch poster from api

    recommed_movies.append(movies.iloc[i[0]].title)
  return recommed_movies

movies_dic = pickle.load(open('movies_dic.pkl', 'rb'))
movies = pd.DataFrame(movies_dic)

similarity = pickle.load(open('similarity_1.pkl', 'rb'))

st.title('Movie Recommender System')
select_movie = st.selectbox(
    'Select a movie from the list below:',
    movies['title'].values
)

if st.button('Recommend'):
    recommendations = recommed(select_movie)
    for i in recommendations:
       st.write(i)
    st.write(select_movie)