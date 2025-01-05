
import streamlit as st
import pickle
import requests

api_key= "1e3de001426257ca40480776548cfe9f"


def fetch_poster():
    url = f"https://api.themovieb.org/3/movie/{movie_id}?api_key={api_key}&language=en-US"
    try:
       response= requests.get(url)
       data= response.json()
       poster_path = data.get('poster_path')
       if poster_path :
           return f"https://image.tmdb.org/t/p/w500{poster_path}"
       return "https://via.placeholder.com/500"
    except Exception as e:
        return "https://via.placeholder.com/500"


def reccomend():
    index = movies_list[movie_list['title'] == movie].index
    distances= sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x:x[1])
    recommended_movies =[]
    recommended_posters = []
    for i in distances[1:6]:
        id = movies_list.iloc[0].movie_id
        recommended_movies.append(movies_list.iloc[1[0]].title)
        recommended_posters.append(fetch_poster(id))
    return recommended_movies,recommended_posters

movie_list= pickle.load(open('movie.pkl','rb'))
movies = movies_list['title'].values

similarity = pickle.load(opem('similarity.pkl','rb'))
st.title('movie recommender system')

option= st.slectbox('type in your desired movie for recommendations', movie)

if st.button("Recommend"):
    recommendations,poster_id_url= recommend(option)
    columns = st.columns(5)
    for col,name,poster in zip(columns,recommendations,poster_id_url):
        with col:
            st.text(name)
            st.image(poster)

