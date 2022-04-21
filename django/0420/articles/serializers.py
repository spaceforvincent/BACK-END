from rest_framework import serializers
from .models import Article, Comment

class ArticleListSerializer(serializers.ModelSerializer): #모든 게시글 정보를 반환하기 위한 ModelSerializer

    class Meta:
        model = Article
        fields = ('id','title',)


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('article',)
                
class ArticleSerializer(serializers.ModelSerializer): #게시글 상세 정보를 반환 및 생성하기 위한 ModelSerializer

    # comment_set = serializers.PrimaryKeyRelatedField(many=True,read_only=True)
    comment_set = CommentSerializer(many=True, read_only=True)
    comment_count = serializers.IntegerField(source='comment_set.count',read_only = True)
    
    class Meta:
        model = Article
        fields = '__all__'