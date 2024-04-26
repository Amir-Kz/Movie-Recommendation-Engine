import streamlit as st
import pickle 
import requests 

movies = pickle.load(open("moviesList.pkl", 'rb'))
similarity = pickle.load(open("similarity.pkl", 'rb'))

moviesList = movies['title'].values

st.header("Movie Recommender System")
selectValue = st.selectbox("Select movie", moviesList)

def fetch_poster(movieID):
    url = f"https://api.themoviedb.org/3/movie/{movieID}?api_key=a8423fbd7360ebcef6dcf36272a34056"
    data = requests.get(url).json()  
    poster_path = data.get('poster_path', '')  
    fullPath = "https://image.tmdb.org/t/p/original" + poster_path
    return fullPath


def recommand(movie):
    index = movies[movies['title'] == movie].index[0]
    distance = sorted(list(enumerate(similarity[index])), reverse = True, key = lambda vector:vector[1])
    recommandMovie = []
    displayPoster = []
    for i in distance[1:6]:
        movieID = movies.iloc[i[0]].id
        recommandMovie.append(movies.iloc[i[0]].title)
        displayPoster.append(fetch_poster(movieID))

    return recommandMovie, displayPoster
   

if st.button("Show recommendations"):
    movieName, moviePoster = recommand(selectValue)

    col1,col2,col3,col4,col5 = st.columns(5)
    
    with col1:
        st.text(movieName[0])
        st.image(moviePoster[0])
    with col2:
        st.text(movieName[1])
        st.image(moviePoster[1])
    with col3:
        st.text(movieName[2])
        st.image(moviePoster[2])
    with col4:
        st.text(movieName[3])
        st.image(moviePoster[3])
    with col5:
        st.text(movieName[4])
        st.image(moviePoster[4])