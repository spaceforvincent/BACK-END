from rest_framework import serializers
from .models import Movie


class MovieSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Movie
        fields = ('title','release_date','poster_path','overview','vote_average','original_title',)
