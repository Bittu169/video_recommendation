import streamlit  as st

from click import option
import pickle
import pandas as pd
import requests
# def fetch_poster(movie_id):
#     print(movie_id)
#     response=requests.get(f'https://api.themoviedb.org/3/movie/{movie_id}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US',timeout=30)
#     data=response.json()
#     print(data)
#     return "https://image.tmdb.org/t/p/w500/"+data['poster_path']
def fetch_poster(movie_id):
    try:
        response = requests.get(
            f'https://api.themoviedb.org/3/movie/{movie_id}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US',
            timeout=30
        )
        response.raise_for_status()
        data = response.json()
        if 'poster_path' in data and data['poster_path']:
            return f"https://image.tmdb.org/t/p/w500/{data['poster_path']}"
        else:
            return "https://via.placeholder.com/500x750?text=No+Image"
    except requests.exceptions.RequestException as e:
        print(f"Error fetching poster: {e}")
        return "https://via.placeholder.com/500x750?text=Error"


def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies=[]
    recommended_movies_posters=[]
    for i in movie_list:
        movies_id=movies.iloc[i[0]].movie_id


        recommended_movies.append(movies.iloc[i[0]].title)
        # fetch poster from api
        recommended_movies_posters.append(fetch_poster(movies_id))
    return recommended_movies,recommended_movies_posters


movies_dict= pickle.load(open('movies_dict.pkl','rb'))
movies=pd.DataFrame(movies_dict)
st.title('Movie Recommender System')


similarity=pickle.load(open('similarity.pkl','rb'))
selected_movie_name = st.selectbox(
    'Select a movie to get recommendations:',
    movies['title'].values
)

# selected_movie_name=st.selectbox(
#     'How would you like to be connected?',
#     movies['title'].values)
if st.button('Recommend'):
    names,posters=recommend(selected_movie_name)
    col1,col2,col3,col4,col5=st.columns(5)
    with col1:
        st.header(names[0])
        st.image(posters[0])
    with col2:
        st.header(names[1])
        st.image(posters[1])
    with col3:
        st.header(names[2])
        st.image(posters[2])
    with col3:
        st.header(names[3])
        st.image(posters[3])
    with col3:
        st.header(names[4])
        st.image(posters[4])



