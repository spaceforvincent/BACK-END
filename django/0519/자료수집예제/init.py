import requests
import json

TMDB_API_KEY = 'f433951fa3f9ea7fc5b7f38dbec9ac20'

def get_movie_datas():
    total_data = []

    for i in range(1, 100):
        request_url = f"https://api.themoviedb.org/3/movie/popular?api_key={TMDB_API_KEY}&language=ko-KR&page={i}"
        movies = requests.get(request_url).json()

        for movie in movies['results']:
            if movie.get('release_date', ''):
                fields = {
                    # 'movie_id': movie['id'],
                    'title': movie['title'],
                    'released_date': movie['release_date'],
                    'adult': movie['adult'],
                    'vote_avg': movie['vote_average'],
                    'overview': movie['overview'],
                    'poster_path': movie['poster_path'],
                    'genres': movie['genre_ids'],
                    'like_users': []
                }

                data = {
                    "pk": movie['id'],
                    "model": "movies.movie",
                    "fields": fields
                }

                total_data.append(data)

    with open("movies/fixtures/movie_data.json", "w", encoding="utf-8") as w:
        json.dump(total_data, w, indent=4, ensure_ascii=False)

def get_genre_data():
    total_data = []

    request_url = f"https://api.themoviedb.org/3/genre/movie/list?api_key={TMDB_API_KEY}"
    genres = requests.get(request_url).json()

    for genre in genres['genres']:
        fields = {
            # 'genre_id': genre['id'],
            'name': genre['name'],
        }

        data = {
            "pk": genre['id'],
            "model": "movies.genre",
            "fields": fields
        }
        total_data.append(data)

    with open("movies/fixtures/genre_data.json", "w", encoding="utf-8") as w:
        json.dump(total_data, w, indent=4, ensure_ascii=False)


get_movie_datas()
get_genre_data()

'''
movies/fixtures/ 만들고 실행
장르부터 먼저 실행 주의

python manage.py loaddata genre_data.json
python manage.py loaddata movie_data.json

'''