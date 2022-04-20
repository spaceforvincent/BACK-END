# 보충 학습 (좋아요 기능 구현)

## 시작하기

1. 바탕화면에서 Git Bash 열기

2. 프로젝트 클론 받기

    ```bash
    $ git clone https://lab.ssafy.com/s07/python/add-one-to-many.git
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

시작하기 전에 회원가입/로그인 기능이 정상적으로 동작하는지 확인 해보세요.

### 좋아요 기능 구현하기

* 좋아요 기능 구현을 위해서는 M:N 관계 설정을 하여야 합니다. 테이블 예시는 아래와 같습니다.

  * articles_article

      | id   | title | content |
      | ---- | ----- | ------- |
      | 1    | 제목1   | 내용1   |
      | 2    | 제목2    | 내용2      |
      | 3    | 제목3 | 내용3    |

  * accounts_user

      | id(PK) | username |
      | ------ | -------- |
      | 1      | 홍길동   |
      | 2      | 김철수   |

  * articles_article_like_users
      
      * 홍길동은 1, 2, 3글을 좋아요 눌렀습니다.
      * 김철수는 1글만 좋아요 눌렀습니다.
      * 1글은 홍길동, 김철수가 좋아요 눌렀습니다.
      
      | id     | article_id | user_id |
      | ------ | ---------- | ------- |
      | 1      | 1          | 1       |
      | 2      | 2          | 1       |
      | 3      | 3          | 1       |
      | 4      | 1          | 2       |
      

* 게시글 목록 페이지에서 좋아요 링크를 생성합니다.

* 좋아요 기능을 처리하는 view를 작성합니다.

  * 해당 글에 좋아요를 눌렀는지 확인하고
    * 좋아요를 눌렀다면, 제거를 해야 합니다.
    * 좋아요를 누르지 않았다면, 생성을 해야합니다.

  * 모든 처리가 완료되면 게시글 상세보기 페이지로 redirect합니다.

* 게시글 목록 페이지에서 상황에 따라 좋아요 / 좋아요 취소 링크로 분기합니다.

  

1. 모델 설정

    * User 모델과의 관계 설정입니다.

    * 역참조(related_name)는 like_articles로 합니다.

    ```python
    class Article(models.Model):
        user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
        like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_articles')
    ```
    
    ```python
    # 좋아요를 누른 모든 사람
    article.like_users.all()
    # 유저가 좋아요 누른 모든 글
    user.like_articles.all()
    ```

2. 게시글 링크 만들기

   * POST요청을 위해 form 태그를 활용합니다.

3. URL 생성하기

   ```text
   /articles/article_pk/likes/
   ```

4. view 함수 작성하기

    * 아래의 메서드를 적절하게 활용합니다.

    ```python
    # 좋아요를 누른 모든 사람
    article.like_users.all()
    # 추가
    article.like_users.add(user)
    # 제거
    article.like_users.remove(user)
    # 확인하기 1
    user in article.like_users.all()
    # 확인하기 2
    article.like_users.filter(pk=user.pk).exists()
    ```

5. 게시글 목록에서 상황에 따른 분기하기

### [선택] 팔로우 기능 구현하기

* 프로필 기능은 구현되어 있습니다.

* 팔로우 기능은 User 간의 M:N 관계입니다.

  * accounts_user

    | id(PK) | username |
    | ------ | -------- |
    | 1      | 홍길동   |
    | 2      | 김철수   |

  * accounts_user_followings

    * 홍길동과 김철수는 서로 팔로우를 하였습니다.
    
    | id   | from_user_id | to_user_id |
    | ---- | ------------ | ---------- |
    | 1    | 1            | 2         |
    | 2    | 2            | 1          |

* 모델 설정은 아래와 같습니다.

  * User 모델간의 관계 설정입니다. (`self`)
  * 대칭 관계는 False로 설정합니다.
    * 홍길동이 김철수를 팔로우하는 것과 김철수가 홍길동을 팔로우하는 것은 개별 행위입니다.
  * 역참조(related_name)는 follwers로 합니다.

  ```python
  class User(AbstractUser):
      following = models.ManyToManyField('self', symmetrical=False, related_name='follwers')
  ```

* 프로필 페이지에서 팔로우 링크를 만들고 처리하는 로직을 작성 해보세요.

  * view 함수 로직은 좋아요 기능을 참고하시면 도움이 됩니다.
