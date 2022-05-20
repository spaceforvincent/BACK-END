# Django, The Web Framework 2



### Model

- 단일한 데이터에 대한 정보를 가짐. 사용자가 저장하는 데이터들의 필수적인 필드들과 동작들을 포함. <u>Django는 model을 통해 데이터에 접속하고 관리</u>

- 일반적으로 <u>각각의 model은 하나의 데이터베이스 테이블에 매핑</u>됨

- <u>웹 애플리케이션의 데이터를 구조화하고 조작</u>하기 위한 도구

- Django에서는 **ORM**(Object-relational-mapping)을 활용하여 테이블(RDBMS)을 조작할 수 있음.

  - SQL을 잘 알지 못해도 DB조작이 가능

  - 절차적 접근이 아닌 <u>객체 지향적 접근</u>으로 인한 높은 생산성 (현대 웹 프레임워크의 요점)

  - But, ORM만으로 완전한 서비스를 구현하기 어려울 수 있음

  - 우리는 <u>DB를 객체로 조작</u>하기 위해 ORM을 사용한다고 볼 수 있음.

    

- Models.py 작성 (어떠한 타입의 DB컬럼을 정의할 것인가?)

```python
#articles/models.py
class Article(models.Model): #테이블
	#CharField : 길이의 제한이 있는 문자열, max_length는 필수 인자
	title = models.CharField(max_length=10) #필드 
	#TextField : 글자의 수가 많을 때 사용
	content = models.TextField() #필드
	created_at = models.DateTimeField(auto_now_add=True) #최초생성일자
	updated_at = models.DateTimeField(auto_now=True) #최종 수정일자 갱신
	
    #각각의 object가 사람이 읽을 수 있는 문자열을 반환하도록 함
	def __str(self):
		return self.title
	
```

###  Migrations

- Django가 <u>Model에 생긴 변화를 반영</u>하는 기법

  - **makemigrations** : model을 변경한 것에 기반한 <u>새로운 설계도를 만들 때</u> 사용
  - **migrate** : <u>설계도를 실제 DB에 반영</u>, 변경사항 동기화
  - **sqlmigrate** : <u>마이그레이션에 대한 SQL구문</u>을 보기 위해 사용
  - **showmigrations** : <u>프로젝트 전체의 마이그레이션 여부 확인</u>

*실제 DB TABLE은 vscode sqlite 확장 프로그램을 통해 확인 가능

- model 수정 시에는 models.py에 추가 모델 필드 작성 후 <u>makemigrations -> migrate</u>

  

### DB API

- DB를 조작하기 위한 도구
  - **ClassName.Manager.QuerySet**의 형식 (Article.objects.all())
- **QuerySet** : 데이터베이스로부터 전달받은 객체 목록
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

- **Create**

  - 인스턴스 생성 후 인스턴스 변수 설정

    - ```django
      article = Article()
      article.title = 'first'
      article.content = 'django!'
      article.save() #객체를 데이터베이스에 저장
      #단순히 모델을 인스턴스화하는 것은 db에 영향을 미치지 않기 때문에 반드시 save()가 필요!
      ```

  - 초기값과 함께 인스턴스 생성(권장)

    - ```
      article = Article(title='second',content='django!')
      article.save() #객체를 데이터베이스에 저장
      ```

  - QuerySet API - create() 사용

    - ```
      #save 필요 x
      Article.objects.create(title='third', content = 'django!!!')
      ```




- **Read** 

  - Article.objects.all() : 현재 <u>QuerySet의 복사본 반환</u>(리스트 형태)

  - Article.objects.get() : 주어진 lookup 매개변수와 일치하는 객체 반환(pk와 같이 고유성을 보장하는 조회에서 사용) (딕셔너리의 요소 하나를 반환)

    - 객체를 찾을 수 없으면 DoesNotExist 예외를 발생시킴
    - 둘 이상의 객체를 찾으면 MultipleObjectsReturned 예외를 발생시킴

    > get 방식의 문제점과 사용이유

    - 100이라는 pk 값이 들어오는 경우에 500오류라고 개발자 오류라고 ERROR가 발생한다. 하지만 사용자가 없어서 100번째 글이 아직 안 적혀서 뜨는거지 나의 잘못이라고 할 수 없다.

    - 즉, url이 없어서 그런거다. 개발자 잘못이 아니라는 점을 표현하고 싶어서 get_object_or_404를 쓴다.

    > get_object_or_404 쓰는법

    ```python
    from django.shortcuts import render, redirect, get_object_or_404
    article = get_object_or_404(Article, pk=pk)
    #object를 가져오거나 404를 가져온다. 즉, 없는 url를 보낸 경우를 알 수 있다.
    ```
  
  
  
- Article.objects.filter() : 주어진 lookup 매개변수와 일치하는 객체를 포함하는 <u>새 QuerySet 반환</u>
  
  - Field lookups
  
  ```django
  Article.objects.filter(pk__gt=2)
  Article.objects.filter(content__contains='ja')
  ```

    

- **Update**

```
#UPDATE articles SET title='byebye' WHERE id=1;
article = Article.objects.get(pk=1) #article 인스턴스 객체
article.title = 'byebye' #인스턴스 객체 변수의 값 변경
article.save() #저장
```



- **Delete** : QuerySet의 모든 행에 대해 SQL 삭제 쿼리 수행

```
#save 필요 x
article = Article.objects.get(pk=1)
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

- ModelAdmin options

  - list_display : models.py에서 정의한 각각의 속성들의 값을 admin 페이지에 출력하도록 설정




- csrf_token template tag (http method를 post로 설정한 경우 사용)

  - {% csrf_token %} : CSRF(사이트 간 요청 위조) 보호에 사용
  - input type이 hidden으로 작성되며 value는 Django에서 생성한 hash값으로 설정됨
  - 해당 태그 없이 요청을 보낸다면 Django 서버는 403 for bidden을 응답

- redirect() : 새 URL로 요청을 다시 보냄

  - 브라우저는 현재 경로에 따라 전체 URL 자체를 재구성
  - 사용가능한 인자
    - model
    - view_name
    - absolute or relative URL
  
  ```
  def create(request):
  	title = request.POST.get('title')
  	content = request.POST.get('content')
  	
  	article = Article(title=title, content=content) #CREATE
  	article.save()
  	return redirect('articles:detail', article.pk)
  ```
  
  
