from flask import Flask, request, jsonify
from flask_cors import CORS
import pandas as pd
import pickle
import requests

app = Flask(__name__)
CORS(app)

movie = pickle.load(open('movie.pkl', 'rb'))
movies = pd.DataFrame(movie)
similarity = pickle.load(open('similarity.pkl', 'rb'))

def fetchPosture(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=0ef8fd90d0f9fa26fac224e1a50af8a7'.format(movie_id))
    data = response.json()
    return "https://image.tmdb.org/t/p/original/" + data['poster_path']

def recommend(movie_name):
    try:
        index = movies[movies['title'] == movie_name].index[0]
    except IndexError:
        return []
    dist = similarity[index]
    movies_list = sorted(list(enumerate(dist)), reverse=True, key=lambda x: x[1])[1:6]
    recommended_movies = [movies.iloc[i[0]].title for i in movies_list]
    recommend_movie_posters = []
    for i in movies_list:
        recommend_movie_posters.append(fetchPosture(movies.iloc[i[0]].movie_id))
    return recommended_movies,recommend_movie_posters

@app.route('/recommend', methods=['POST'])
def recommend_movie():
    try:
        data = request.json
        movie_name = data['movie_name']
        recommendations,posters = recommend(movie_name)
        if not recommendations:
            return jsonify({'error': 'Movie not found'}), 404
        return jsonify({'recommendations': recommendations, 'posters': posters})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)