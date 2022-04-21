from rest_framework import serializers
from .models import Artist, Music

class ArtistListSerializer(serializers.ModelSerializer): #모든 가수 정보를 반환하기 위한 ModelSerializer

    class Meta:
        model = Artist
        fields = ('id','name',)

class MusicListSerializer(serializers.ModelSerializer): #모든 음악의 정보를 반환하기 위한 ModelSerializer

    class Meta:
        model = Music
        fields = ('id','title',)
        read_only_fields = ('artist',)


class MusicSerializer(serializers.ModelSerializer): #상세 음악의 정보를 생성 및 반환하기 위한 ModelSerializer

    class Meta:
        model = Music
        fields = '__all__'
        read_only_fields = ('artist',)
                
class ArtistSerializer(serializers.ModelSerializer): #가수 상세 정보를 반환 및 생성하기 위한 ModelSerializer

    # comment_set = serializers.PrimaryKeyRelatedField(many=True,read_only=True)
    music_set = MusicSerializer(many=True, read_only=True)
    music_count = serializers.IntegerField(source='music_set.count',read_only = True)
    
    class Meta:
        model = Artist
        fields = '__all__' #모든 필드를 직렬화