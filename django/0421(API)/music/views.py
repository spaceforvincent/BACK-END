from django.shortcuts import render

# Create your views here.
from django.shortcuts import get_object_or_404, get_list_or_404, render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import ArtistListSerializer, ArtistSerializer, MusicListSerializer,MusicSerializer
from .models import Artist, Music
'''
Django REST Framework (DRF 사용할 때)
View 함수에서 주의할 점들

1) 함수에 데코레이터 달기
2) Response 함수에 serializer 변수 그대로 넣지 말고
serializer.data 넘기기
'''


# Create your views here.
@api_view(['GET', 'POST']) #게시글 조회 및 생성
def artist_list(request):
    #GET
    if request.method == 'GET':
        #1. 모든 가수 정보들을 가져온다
        artists = get_list_or_404(Artist)
        #2. 데이터 전송을 위해 json으로 변환하기 좋은 형태로 바꾼다
        serializer = ArtistListSerializer(artists, many=True)
        #3. json으로 응답한다
        return Response(serializer.data)

    #POST
    elif request.method == 'POST':
        #1. 사용자가 입력한 정보를 Serializer에 바인딩
        serializer = ArtistListSerializer(data=request.data)
        #2. 그 정보가 유효한지 검사 (유효하다면 DB에 저장, 유효하지 않으면 400 bad requst에러 발생)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)


@api_view(['GET', 'DELETE', 'PUT'])
def artist_detail(request, artist_pk):
    #가수 정보 객체 가져옴 (GET, DELETE, PUT 모두 사용할) 
    artist = get_object_or_404(Artist, pk=artist_pk)
    
    #GET
    if request.method == 'GET':
        #1. 데이터 전송을 위해 json으로 변환하기 좋은 형태로 바꾼다
        serializer = ArtistSerializer(artist) 
        #3. json으로 응답한다
        return Response(serializer.data)

    elif request.method == 'DELETE': #특정 가수정보를 삭제한다.
        artist.delete()
        data = {
            'delete' : f'데이터 {artist_pk}번이 삭제되었습니다.' #삭제가 완료되면 삭제한 가수정보의 id를 응답한다.
        }
        return Response(data, status=status.HTTP_204_NO_CONTENT)

    elif request.method == 'PUT': #특정 가수의 정보를 수정한다.
        #데이터 전송을 위해 json으로 변환하기 좋은 형태로 바꾼다
        serializer = ArtistSerializer(artist, data=request.data)
        if serializer.is_valid(raise_exception=True): #검증에 실패할 경우 400 Bad Request 예외를 발생시킨다. 
            serializer.save() ##검증에 성공하는 경우 수정된 게시글의 정보를 DB에 저장한다.
            return Response(serializer.data) # 수정이 완료되면 수정한 게시글의 정보를 응답한다.

@api_view(['GET'])
def music_list(request):
    #1. 모두 가져온다
    musics = get_list_or_404(Music)
    #2. 데이터 전송을 위해 json으로 변환하기 좋은 형태로 바꾼다
    serializer = MusicListSerializer(musics, many=True)
    #3. json으로 응답한다
    return Response(serializer.data)


@api_view(['GET', 'DELETE', 'PUT'])
def music_detail(request, music_pk):
    
    music = get_object_or_404(Music, pk=music_pk)
    
    if request.method == 'GET':
        serializer = MusicSerializer(music)
        return Response(serializer.data)

    elif request.method == 'DELETE':
        music.delete()
        data = {
            'delete' : f'음악 {music_pk}번이 삭제되었습니다.'
        }
        return Response(data, status=status.HTTP_204_NO_CONTENT)

    elif request.method == 'PUT':
        serializer = MusicSerializer(music, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)


@api_view(['POST'])
def music_create(request, artist_pk):
    artist = get_object_or_404(Artist, pk = artist_pk)
    serializer = MusicSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(artist=artist)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
