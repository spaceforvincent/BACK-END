# Django, The Web Framework

<hr> 

### Web framework

- 거인의 어깨에서 시작... 

  웹 페이지를 개발하는 과정에서 겪는 어려움을 줄이는 것이 주 목적으로 데이터베이스 연동, 템플릿 형태의 표준, 세션 관리, 코드 재사용 등의 기능을 포함.

  

- static web page : 서버에 미리 저장된 파일이 사용자에게 그대로 전달되는 웹 페이지

  서버는 정적 웹페이지에 대한 요청을 받은 경우 서버는 추가적인 처리 과정 없이 클라이언트에게 응답을 보냄. 

  모든 상황에서 모든 사용자에게 동일한 정보 표시.일반적으로 HTML, CSS, JavaScript로 작성됨

  

- dynamic web page : 서버는 동적 웹페이지에 대한 요청을 받은 경우 추가적인 처리 과정 이후 클라이언트에게 응답을 보냄. 

  동적 웹페이지는 방문자와 상호작용하기 때문에 페이지 내용은 그때그때 다름. 

  서버사이드 프로그래밍 언어가 사용되며데이터베이스와의 상호작용이 이루어짐.

- Django Framework Architecture (MTV) :

  - Model : 데이터 구조 정의. DB의 기록 관리
  - Template(View) : 파일의 구조나 레이아웃을 정의. 실제 내용을 보여주는 데 사용
  - View : http 요청 수신, 응답 반환 & Model을 통해 요청을 충족시키는 데 필요한 데이터에 접근 & template에게 응답의 서식 설정 맡김

- ![Django introduction - Learn web development | MDN](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Introduction/basic-django.png)



### Django Intro

- Django 작업순서

  - python -m venv venv (가상환경 생성)

  - source venv/Scripts/activate 

  - pip install django==3.2.12 (LTS ver 장고 설치)

  - django-admin startproject firstpjt . (프로젝트 생성)

  - python manage.py startapp articles (앱 생성)

  - settings.py  -> INSTALLED_APPS에 앱 등록

  - urls.py (include 활용하여 url 분리)

  - views.py 작성

  - templates

  - python manage.py runserver (서버 활성화) 

    *manage.py : Django 프로젝트와 다양한 방식으로 상호작용하는 커맨드라인 유틸리티





### 요청과 응답

- urls.py -> 처리할 요청 작성
  - path('hello/', views.(어플리케이션의) hello라는 요청이 들어오면 실행할 메서드)
- views.py -> 요청을 수신하고 응답을 반환하는 함수 작성
  - render(request,'hello.html') : 템플릿(응답을 위한 틀)을 이용해서 응답을 만들어주는 함수

- 템플릿 위치 : app/templates/템플릿(기본)





### Templates

- 데이터 표현을 제어하는 도구이자 표현에 관련된 로직

- DTL (Django Template Language)

  - {{ variable }} : render()를 사용하여 views.py에서 정의한 변수를 template파일로 넘겨 사용하는 것. 

    ​						render()의 세번째 인자로 딕셔너리 형태로 넘겨주며 여기서 정의한 key에 해당하는 문자열이 template에서 사용가능한 변수명이 됨.

  - {{ variable|Filters }} : 표시한 변수를 수정할 때 사용 

    - ex) lower, truncatewords:30

  - {% tag %} : 출력 테스트를 만들거나 반복 또는 논리를 수행하여 제어 흐름을 만드는 등 변수보다 복잡한 일을 수행

  - 일부 태그는 시작과 종료 태그가 필요

    - ex) if - endif, block - endblock

  - {# #}, {% comment % } ~ {% endcomment %} : 한줄 주석, 여러줄 주석

- 템플릿 상속 : 사이트의 모든 공통 요소를 포함하고 하위 템플릿이 재정의(override)할 수 있는 블록을 정의하는 기본 skeleton 템플릿을 만들 수 있음

  - {% extends '' %} : 반드시 템플릿 최상단에 작성
  - {% block content %} ~{% endblock content %} : 하위 템플릿이 채울 수 있는 공간
  - 작성순서
    - settings.py -> TEMPLATES의 'DIRS' 부분에 [BASE_DIR / 'templates'] 작성 (app_name/templates 디렉토리 외 추가 경로 설정하는 작업)
    - "프로젝트" 밑에 templates폴더 만들어 base.html 작성 (부트스트랩이나 간단한 navbar)
    - 어플의 템플릿(하위 템플릿)으로 와서 최상단에 {% extends 'base.html' %} 작성 후 {% block content %} ~{% endblock content %} 사이에 표시할 내용 작성

- {% include %} : 템플릿을 로드하고 현재 페이지로 렌더링. 템플릿 내에 다른 템플릿을 포함하는 방법

  - ex) base.html에 {% include '_nav.html' %} 사용
  - 

#### "철학 : 표현(template)과 로직(view)을 분리. 중복을 배제하자"



### URLs

- 웹 어플리케이션은 URL을 통한 클라이언트의 요청에서부터 시작함

- Variable Routing : URL 주소를 변수로 사용하는 것.

  - URL의 일부를 변수로 지정하여 view 함수의 인자로 넘길 수 있음

    - 대신 def hello(request, variable)의 형식으로 받아줘야 함

  - 변수 값에 따라 하나의 path()에 여러 페이지를 연결시킬 수 있음

    ```
    path('accounts/user/<int:user_pk>/...')
    ```

    - accounts/user/1 -> 1번 user 관련 페이지
    - accounts/user/2 -> 2번 user 관련 페이지

- URL Mapping 

  - app의 view 함수가 많아지면서 사용하는 path()또한 많아지고, app 또한 더 많이 작성되기 때문에 프로젝트의 urls.py에서 모두 관리하는 것은 비효율적

  - 각각의 앱 안에 urls.py를 생성하고 프로젝트 urls.py에서 각 앱의 urls.py 파일로 URL 매핑을 위탁

    - include() : 다른 URLconf들을 참조할 수 있도록 도움 ex)app1/urls.py
    - URL의 그 시점까지 일치하는 부분을 잘라내고 남은 문자열 부분을 후속 처리를 위해 include된 URLconf로 전달

    ```django
    #firstpjt/urls.py
    from django.contrib import admin
    from django.urls import path, include
    
    urlpatterns = [
        path('admin/', admin.site.urls),
        path('articles/', include('articles.urls')),
        path('pages/', include('pages.urls')),
    ]
    
    #articles/urls.py
    from django.urls import path
    from . import views
    
    app_name = 'articles'
    urlpatterns = [
        path('index/', views.index, name='index'),
        path('greeting/', views.greeting, name='greeting'),
        path('dinner/', views.dinner, name='dinner'),
        path('dtl-practice/', views.dtl_practice, name='dtl-practice'),
        path('throw/', views.throw, name='throw'),
        path('catch/', views.catch, name='catch'),
        path('hello/<str:name>/', views.hello, name='hello'),
    ]
    
    ```

    

  - Naming URL patterns : 이제는 링크에 url을 직접 작성하는 것이 아니라 path() 함수의 name 인자를 정의해서 사용. url 설정에 정의된 특정한 경로들의 의존성 제거할 수 있음

    - 각 path에 이름 지정한다고 생각하면 될듯

    ```
    #urls.py
    path('index/', views.index, name='index')
    
    #template
    <a href={% url 'index' %}> 메인 페이지 </a>
    
    name이라는 value가 {% url '' %} 태그에 의해 호출됨
    ```

    - {% url '' %} : 주어진 URL패턴 이름 및 선택적 매개 변수와 일치하는 절대 경로 주소를 반환. 템플릿에 URL을 하드코딩하지 않고도 링크를 출력하는 방법
    - 