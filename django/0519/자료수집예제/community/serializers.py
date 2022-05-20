from rest_framework import serializers
from .models import Review, Comment



class ReviewSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Review
        fields = ('id', 'title', )


class CommentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Comment
        fields = ('id', 'content', 'movie_title','created_at','updated_at')

        