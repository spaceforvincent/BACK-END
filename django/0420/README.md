# 보충 학습 (DRF)

## 시작하기

1. 바탕화면에서 Git Bash 열기

2. 프로젝트 클론 받기

    ```bash
    $ git clone https://lab.ssafy.com/s07/python/add-drf.git
    ```

3. Visual Studio Code 열기

4. 가상환경 생성 및 실행

    ```bash
    $ python -m venv venv
    $ source venv/Scripts/activate

5. 패키지 설치

    ```bash
    (venv) $ pip install -r requirements.txt
    ```

6. 서버 실행 하기

## 가이드

모델과 마이그레이션 파일은 사전에 정의되어 있습니다.

시작하기 전에 DB migrate를 진행하고, 데이터베이스에 seed 데이터를 추가합니다.

```bash
$ python manage.py migrate
$ python manage.py seed articles --number=20
```

### [필수] Article API 구현하기

#### Serializer 구현

1. Article QuerySet Serializer 

   ```python
   from rest_framework import serializers
   from .models import Article
   
   class ArticleListSerializer(serializers.ModelSerializer):
   
       class Meta:
           model = Article
           fields = ('id', 'title',)
   ```

2. Article 객체 Serializer

   ```python
   from rest_framework import serializers
   
   class ArticleSerializer(serializers.ModelSerializer):
   
       class Meta:
           model = Article
           fields = '__all__'
   ```

#### URL 패턴

| METHOD | URL                              | 기능         | Status code                    |
| ------ | -------------------------------- | ------------ | ------------------------------ |
| GET    | `/api/v1/articles/`              | 전체 글 조회 | 200<br />없는 경우 404         |
| POST   | `/api/v1/articles/`              | 글 작성      | valid : 201<br />invalid : 400 |
| GET    | `/api/v1/articles/<article_pk>/` | 특정 글 조회 | 200<br />없는 경우 404         |
| PUT    | `/api/v1/articles/<article_pk>/` | 특정 글 수정 | 200<br />invalid : 400         |
| DELETE | `/api/v1/articles/<article_pk>/` | 특정 글 삭제 | 204                            |

* 프로젝트 `urls.py` 에 아래와 같이 정의합니다.

  ```python
  from django.contrib import admin
  from django.urls import path, include
  
  urlpatterns = [
      path('admin/', admin.site.urls),
      path('api/v1/', include('articles.urls')),
  ]
  ```

* `articles` 앱 `urls.py`에 상세 URL을 정의합니다.

#### 기능 구현

> 기능 구현시 API 클라이언트로 [postman](https://www.postman.com/)을 활용합니다.

> Status code와 JSON 응답 형식을 참고하여 작성합니다.

##### 전체 글 조회 

* 상태코드 200을 반환합니다.

* JSON 예시

    ```json
  [
        {
            "id": 1, 
            "title": "제목1",
            "content": "내용1"
        }, 
        {
            "id": 2, 
            "title": "제목2",
            "content": "내용2"
        }    
    ]
  ```

##### 상세 글 조회

* 상태코드 200을 반환합니다.

* JSON 예시

  ```JSON
  {
      "id": 1, 
      "title": "제목1",
      "content": "내용1",
      "created_at": "1980-07-07T15:07:31+09:00",
      "updated_at": "1980-07-07T15:07:31+09:00"
  }
  ```

##### 글 생성


  * 생성이 된다면, 상태코드 201을 반환합니다.

  * JSON 예시

    ```python
    {
        "id": 1, 
        "title": "제목1",
        "content": "내용1",
        "created_at": "1980-07-07T15:07:31+09:00",
        "updated_at": "1980-07-07T15:07:31+09:00"
    }
    ```

  * 생성에 실패한다면, 상태코드 400을 반환합니다.

  * JSON 예시

    ```python
    {
        "title": [
            "This field is required."
        ],
        "content": [
            "This field is required."
        ]
    }
    ```

##### 글 삭제


  * 상태코드 204를 반환합니다.

  * JSON 예시

    ```JSON
    {
        "delete": "데이터 1번이 삭제되었습니다."
    }
    ```

##### 글 수정

* 상태코드 200을 반환합니다.

* JSON 예시

  ```JSON
  {
      "id": 2,
      "title": "1111",
      "content": "222",
      "created_at": "1987-08-31T05:20:35Z",
      "updated_at": "2022-04-20T06:23:52.195728Z"
  }
  ```

* 수정에 실패한다면, 상태코드 400을 반환합니다.

* JSON 예시

  ```JSON
  {
      "content": [
          "This field is required."
      ]
  }
  ```

### [선택] 댓글 기능

> 댓글 기능은 강의 자료를 참고하여 구성해보세요.

#### URL 패턴

| METHOD | URL                                       | 기능           | Status code                    |
| ------ | ----------------------------------------- | -------------- | ------------------------------ |
| GET    | `/api/v1/comments/`                       | 전체 댓글 조회 | 200<br />없는 경우 404         |
| POST   | `/api/v1/articles/<article_pk>/comments/` | 댓글 작성      | valid : 201<br />invalid : 400 |
| GET    | `/api/v1/comments/<comment_pk>/`          | 특정 댓글 조회 | 200<br />없는 경우 404         |
| PUT    | `/api/v1/comments/<comment_pk>/`          | 특정 댓글 수정 | 200<br />invalid : 400         |
| DELETE | `/api/v1/comments/<comment_pk>/`          | 특정 댓글 삭제 | 204                            |

