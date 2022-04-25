- python -m venv venv
- source venv/Scripts/activate
- pip install django==3.2.12 (pip install -r requirements.txt)
- django-admin startproject my_api .
- python manage.py startapp articles

```
pip install djangorestframework
pip install django-extensions
pip install django-seed
```

- settings.py -> installed_app에 articles, django_seed, rest_framework, django_extensions 추가



- urls.py(프로젝트)

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('articles.urls')),
]
```

- urls.py(articles 앱)

```python
from django.urls import path
from . import views

urlpatterns = [
    path('articles/', views.article_list), #GET으로 전체 article 목록 가져옴, POST로 새로운 article 작성
    path('articles/<int:article_pk>/',views.article_detail), #GET으로 특정 article 하나 가져옴, PUT으로 특정 article 하나 수정, DELETE로 특정 article 하나 삭제
    path('articles/<int:article_pk>/comments/',views.comment_create),
    path('comments/', views.comment_list),
    path('comments/<int:comment_pk>',views.comment_detail),
]

```

- articles/models.py

```python
from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE) #1:N관계이니 외래키 설정
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
```

- python manage.py <u>makemigrations</u> 후 migrations/0001_initial.py 생성 확인
- python manage.py <u>migrate</u> (0001_initial.py를 실제 DB에 반영)
- adminpage 혹은 shell_plus 혹은 python manage.py seed articles --number=... 활용해서 모델 구조에 맞는 데이터 생성



- articles/serializers.py

```python
from rest_framework import serializers
from .models import Article, Comment

#모든 게시글 정보를 반환하기 위한 ModelSerializer
class ArticleListSerializer(serializers.ModelSerializer): 

    class Meta:
        model = Article
        fields = ('id','title',)

#댓글 상세 정보를 반환 및 생성하기 위한 ModelSerializer
class CommentSerializer(serializers.ModelSerializer):
	#Read-only fields는 API 결과에 포함되지만 등록, 수정시에 request 파라미터에는 포함되지 않는다.
    #comment_create 시 유효성 검사 이후 save를 진행할 때 (article = article)로 인자를 넘겨준다.
    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('article',)
        
#게시글 상세 정보를 반환 및 생성하기 위한 ModelSerializer                
class ArticleSerializer(serializers.ModelSerializer):

	#특정 게시글에 작성된 댓글 목록 출력하기
    comment_set = CommentSerializer(many=True, read_only=True) 
    #특정 게시글에 작성된 댓글의 개수 구하기(serializer을 필드로 표현)
    comment_count = serializers.IntegerField(source='comment_set.count',read_only = True) 
    
    class Meta:
        model = Article
        fields = '__all__'
```



- articles/views.py

```python
from django.shortcuts import get_object_or_404, get_list_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import ArticleListSerializer, ArticleSerializer, CommentSerializer
from .models import Article, Comment

'''
Django REST Framework (DRF) 사용할 때
View 함수에서 주의할 점들

1) 함수에 데코레이터 달기
2) Response 함수에 serializer 변수 그대로 넣지 말고
serializer.data로 넘기기
'''

# Create your views here.
@api_view(['GET', 'POST'])
def article_list(request):
    
    #GET
    if request.method == 'GET':
        #1. Article model(DB)에서 모든 게시글을 가져온다
        articles = get_list_or_404(Article)
        #2. 데이터 전송을 위해 json으로 변환하기 좋은 형태로 바꾼다(many=True 필수)
        serializer = ArticleListSerializer(articles, many=True)
        #3. json으로 응답한다
        return Response(serializer.data)

    elif request.method == 'POST':
        #1. postman의 body에 사용자가 입력한 정보를 Serializer에 바인딩
        serializer = ArticleListSerializer(data=request.data)
        #2. 그 정보가 유효한지 검사(유효하지 않으면 400 에러 발생)
        if serializer.is_valid(raise_exception=True):
            #3. 유효하다면 DB에 저장 후 저장결과 응답
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
         


@api_view(['GET', 'DELETE', 'PUT'])
def article_detail(request, article_pk):
    #Article model(DB)에서 article 객체 가져옴 (GET, DELETE, PUT 공통으로 사용할) 
    article = get_object_or_404(Article, pk=article_pk)
    
    if request.method == 'GET':
        #데이터 전송을 위해 json으로 변환하기 좋은 형태로 바꾼다
        serializer = ArticleSerializer(article)
        return Response(serializer.data)

    elif request.method == 'DELETE':
        #특정 게시글을 삭제한다.
        article.delete()
        #삭제가 완료되면 삭제한 게시글의 id, http상태코드를 응답한다.
        data = {
            'delete' : f'데이터 {article_pk}번이 삭제되었습니다.'
        }
        return Response(data, status=status.HTTP_204_NO_CONTENT)

    elif request.method == 'PUT':
		#1. postman의 body에 사용자가 입력한 정보를 Serializer에 바인딩
        serializer = ArticleSerializer(article, data=request.data)
        #2. 그 정보가 유효한지 검사(유효하지 않으면 400 에러 발생)
        if serializer.is_valid(raise_exception=True):
            #3. 유효하다면 DB에 저장 후 저장결과 응답
            serializer.save()
            return Response(serializer.data)

@api_view(['GET'])
def comment_list(request):
    #1. Comment model(DB)에서 모든 comment들을 가져온다
    comments = get_list_or_404(Comment)
    #2. 데이터 전송을 위해 json으로 변환하기 좋은 형태로 바꾼다(many=True 필수)
    serializer = CommentSerializer(comments, many=True)
    #3. 데이터 전송을 위해 json으로 변환하기 좋은 형태로 바꾼다(many=True 필수)
    return Response(serializer.data)


@api_view(['GET', 'DELETE', 'PUT'])
def comment_detail(request, comment_pk):
	#Comment model(DB)에서 comment 객체 가져옴 (GET, DELETE, PUT 공통으로 사용할)
    comment = get_object_or_404(Comment, pk=comment_pk)
 
    if request.method == 'GET':
        #데이터 전송을 위해 json으로 변환하기 좋은 형태로 바꾼다
        serializer = CommentSerializer(comment)
        return Response(serializer.data)

    elif request.method == 'DELETE':
        #특정 comment를 삭제한다.
        comment.delete()
        #삭제가 완료되면 삭제한 게시글의 id, http상태코드를 응답한다.
        data = {
            'delete' : f'댓글 {comment_pk}번이 삭제되었습니다.'
        }
        return Response(data, status=status.HTTP_204_NO_CONTENT)
	
    elif request.method == 'PUT':
        #1. postman의 body에 사용자가 입력한 정보를 Serializer에 바인딩
        serializer = CommentSerializer(comment, data=request.data)
        #2. 그 정보가 유효한지 검사(유효하지 않으면 400 에러 발생)
        if serializer.is_valid(raise_exception=True):
            #3. 유효하다면 DB에 저장 후 저장결과 응답
            serializer.save()
            return Response(serializer.data)


@api_view(['POST'])
def comment_create(request, article_pk):
    #Article model(DB)에서 article 객체 가져옴
    article = get_object_or_404(Article, pk = article_pk)
    
    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(article=article)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

```





