import streamlit as st
import pickle


def recommend(movie):
    mov_index = movies[movies['title'] == movie].index[0]
    distances = similarity[mov_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    recommended_movies = []
    for i in movies_list:
        movie_id = i[0]
        #fetch poster from API
        recommended_movies.append(movies.iloc[i[0]].title)
    return recommended_movies


movies = pickle.load(open('movies.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))

st.title('Movie Recommender System')
selected_movie_name = st.selectbox('Enter the movie name:', movies['title'].values)
if st.button('Recommend'):
    recommendations = recommend(selected_movie_name)
    for i in recommendations:
        st.write(i)
