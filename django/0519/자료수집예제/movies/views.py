



from rest_framework import serializers, status
from rest_framework.response import Response
from rest_framework.decorators import api_view
import requests
from django.shortcuts import get_object_or_404
from .serializers import MovieSerializer
from .models import Movie
from datetime import datetime
from dateutil import parser


@api_view(['GET', 'POST','PUT'])
def takeMovie(request):
    if request.method == 'GET':
        for i in range(1,21) :
            
            movieURL = f'https://api.themoviedb.org/3/discover/movie?api_key=f433951fa3f9ea7fc5b7f38dbec9ac20&language=ko-KR&page={str(i)}'
            movieList = requests.get(movieURL).json()
            results = movieList.get('results')

        
            for item in results :
                title = item.get('title')
                release_date = item.get('release_date')
                print(type(release_date), release_date)
                poster_path = item.get('poster_path')
                overview = item.get('overview')
                vote_avereage = item.get('vote_average')
                original_title = item.get('original_title')
                
                movie = Movie()     
                movie.title = title
                # movie.release_date = datetime.strptime(release_date, '%Y-%m-%d').date()
                movie.release_date = parser.parse(release_date)
                movie.poster_path = poster_path
                movie.overview = overview
                movie.vote_average = vote_avereage
                movie.original_title = original_title
                movie.save()
        return Response(results)
            
@api_view(['GET'])
def movie(request) :
    if request.method == 'GET' :
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data)

@api_view(['GET', 'POST','PUT'])
def takeGenre(request): 
    if request.method == 'GET':
        movieURL = f'https://api.themoviedb.org/3/discover/movie?api_key=f433951fa3f9ea7fc5b7f38dbec9ac20&language=ko-KR'
        genreURL = f'https://api.themoviedb.org/3/genre/movie/list?api_key=f433951fa3f9ea7fc5b7f38dbec9ac20'
        genreList = requests.get(genreURL).json()
        movieList = requests.get(movieURL).json()
        genre = genreList.get('genres')
        
    return Response(genre)



