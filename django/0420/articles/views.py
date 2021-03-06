from django.shortcuts import get_object_or_404, get_list_or_404, render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import ArticleListSerializer, ArticleSerializer, CommentSerializer
from .models import Article, Comment
'''
Django REST Framework (DRF 사용할 때)
View 함수에서 주의할 점들

1) 함수에 데코레이터 달기
2) Response 함수에 serializer 변수 그대로 넣지 말고
serializer.data 넘기기
'''


# Create your views here.
@api_view(['GET', 'POST'])
def article_list(request):
    #GET
    #1. 모든 게시글을 가져온다
    #2. 데이터 전송을 위해 json으로 변환하기 좋은 형태로 바꾼다
    #3. json으로 응답한다
    if request.method == 'GET':
        articles = get_list_or_404(Article)
        serializer = ArticleListSerializer(articles, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        #1. 사용자가 입력한 정보를 Serializer에 바인딩
        serializer = ArticleListSerializer(data=request.data)
        #2. 그 정보가 유효한지 검사
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        #3. 유효하다면 DB에 저장, 유효하지 않으면 에러 발생


@api_view(['GET', 'DELETE', 'PUT'])
def article_detail(request, article_pk):
    
    article = get_object_or_404(Article, pk=article_pk)
    
    if request.method == 'GET':
        serializer = ArticleSerializer(article)
        return Response(serializer.data)

    elif request.method == 'DELETE': #특정 게시글을 삭제한다.
        article.delete()
        data = {
            'delete' : f'데이터 {article_pk}번이 삭제되었습니다.' #삭제가 완료되면 삭제한 게시글의 id를 응답한다.
        }
        return Response(data, status=status.HTTP_204_NO_CONTENT)

    elif request.method == 'PUT': #특정 게시글의 정보를 수정한다.

        serializer = ArticleSerializer(article, data=request.data)
        if serializer.is_valid(raise_exception=True): #검증에 실패할 경우 400 Bad Request 예외를 발생시킨다. 
            serializer.save() ##검증에 성공하는 경우 수정된 게시글의 정보를 DB에 저장한다.
            return Response(serializer.data) # 수정이 완료되면 수정한 게시글의 정보를 응답한다.

@api_view(['GET'])
def comment_list(request):
    comments = get_list_or_404(Comment)
    serializer = CommentSerializer(comments, many=True)
    return Response(serializer.data)


@api_view(['GET', 'DELETE', 'PUT'])
def comment_detail(request, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)
    
    if request.method == 'GET':
        serializer = CommentSerializer(comment)
        return Response(serializer.data)

    elif request.method == 'DELETE':
        comment.delete()
        data = {
            'delete' : f'댓글 {comment_pk}번이 삭제되었습니다.'
        }
        return Response(data, status=status.HTTP_204_NO_CONTENT)

    elif request.method == 'PUT':
        serializer = CommentSerializer(comment, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)


@api_view(['POST'])
def comment_create(request, article_pk):
    article = get_object_or_404(Article, pk = article_pk)
    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(article=article)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
