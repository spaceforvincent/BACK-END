# Django, The Web Framework 2



### Model

- 단일한 데이터에 대한 정보를 가짐. 사용자가 저장하는 데이터들의 필수적인 필드들과 동작들을 포함. Django는 model을 통해 데이터에 접속하고 관리

- 일반적으로 각각의 model은 하나의 데이터베이스 테이블에 매핑됨

- 웹 애플리케이션의 데이터를 구조화하고 조작하기 위한 도구

- Django에서는 ORM(Object-relational-mapping)을 활용하여 테이블(RDBMS)을 조작할 수 있음.

  - SQL을 잘 알지 못해도 DB조작이 가능

  - 절차적 접근이 아닌 객체 지향적 접근으로 인한 높은 생산성 (현대 웹 프레임워크의 요점)

  - But, ORM만으로 완전한 서비스를 구현하기 어려울 수 있음

    

- Models.py 작성 (어떠한 타입의 DB컬럼을 정의할 것인가?)

```
#articles/models.py
class Article(models.Model):
	#CharField : 길이의 제한이 있는 문자열, max_length는 필수 인자
	title = models.CharField(max_length=10) 
	#TextField : 글자의 수가 많을 때 사용
	content = models.TextField()
```

*DateField's options : auto_now_add(최초 생성일자), auto_now(최종 수정일자)

###  Migrations

- Django가 Model에 생긴 변화를 반영하는 기법

  - makemigrations : model을 변경한 것에 기반한 새로운 설계도를 만들 때 사용
  - migrate : 설계도를 실제 DB에 반영, 변경사항 동기화
  - sqlmigrate : 마이그레이션에 대한 SQL구문을 보기 위해 사용
  - showmigrations : 프로젝트 전체의 마이그레이션 여부 확인

*실제 DB TABLE은 vscode sqlite 확장 프로그램을 통해 확인 가능

- model 수정 시에는 models.py에 추가 모델 필드 작성 후 makemigrations -> migrate

  

### DB API

- DB를 조작하기 위한 도구
  - ClassName.Manager.QuerySet의 형식 (Article.objects.all())
- QuerySet : 데이터베이스로부터 전달받은 객체 목록
- Django shell

```
$ pip install ipython
$ pip install django-extensions

#settings.py에 앱 등록 후 shell_plus 실행
INSTALLED_APPS = [
....
'django_extensions'
....
]

$ python manage.py shell_plus
```



### CRUD

- Create

  - 인스턴스 생성 후 인스턴스 변수 설정

    - ```django
      article = Article()
      article.title = 'first'
      article.content = 'django!'
      article.save()
      ```

  - 초기값과 함께 인스턴스 생성

    - ```
      article = Article(title='second',content='django!')
      article.save()
      ```

  - QuerySet API - create() 사용

    - ```
      #save 필요 x
      Article.objects.create(title='third', content = 'django!!!')
      ```

      

- Read 

  - Article.objects.all() : 현재 QuerySet의 복사본 반환

  - Article.objects.get() : 주어진 lookup 매개변수와 일치하는 객체 반환(pk와 같이 고유성을 보장하는 조회에서 사용)

  - Article.objects.filter() : 주어진 lookup 매개변수와 일치하는 객체를 포함하는 새 QuerySet 반환

    - Field lookups

    ```django
    Article.objects.filter(pk__gt=2)
    Article.objects.filter(content__contains='ja')
    ```

    

- Update

```
#UPDATE articles SET title='byebye' WHERE id=1;
article = Article.objects.get(pk=1)
article.title = 'byebye'
article.save()
```



- Delete : QuerySet의 모든 행에 대해 SQL 삭제 쿼리 수행

```
#save 필요 x
article.delete()
```



### Admin Site

- 서버의 관리자가 활용하기 위한 페이지

- Model class를 admin.py에 등록하고 관리

- record 생성 여부 확인에 매우 유용하며, 직접 record를 삽입할 수도 있음

- admin 생성

  ```
  $ python manage.py createsuperuser
  ```

  - 관리자 계정 생성 후 서버를 실행한 다음 /admin으로 가서 관리자 페이지 로그인
  - 내가 만든 Model을 보기 위해서는 admin.py에 작성하여 Django 서버에 등록

- admin 등록

  ```
  # articles/admin.py
  from django.contrib import admin
  from .models import Article
  
  #admin site에 register하겠다.
  admin.site.register(Article)
  
  ```

  - admin.py는 관리자 사이트에 Article 객체가 관리자 인터페이스를 가지고 있다는 것을 알려주는 것

### CRUD with views

- csrf_token template tag (http method를 post로 설정한 경우 사용)

  - {% csrf_token %} : CSRF(사이트 간 요청 위조) 보호에 사용
  - input type이 hidden으로 작성되며 value는 Django에서 생성한 hash값으로 설정됨
  - 해당 태그 없이 요청을 보낸다면 Django 서버는 403 for bidden을 응답

- redirect() : 새 URL로 요청을 다시 보냄

  ```
  def create(request):
  	title = request.POST.get('title')
  	content = request.POST.get('content')
  	
  	article = Article(title=title, content=content) #CREATE
  	article.save()
  	return redirect('articles:index')
  ```

  

