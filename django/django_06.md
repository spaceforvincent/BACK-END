# The Django Authentication System

- Django 인증 시스템은 django.contrib.auth에 Django contrib module로 제공
  - settings.py- >INSTALLED_APPS 설정에 포함되어있는 필수구성
    - django.contrib.auth : 인증 프레임워크의 핵심과 기본 모델을 포함
    - django.contrib.contenttypes  : 사용자가 생성한 모델과 권한을 연결할 수 있음
- Authentication % Authorization
  - Authentication (인증)
    - 신원확인
    - 사용자가 자신이 누구인지 확인하는 것
  - Authorization (권한, 허가)
    - 권한 부여
    - 인증된 사용자가 수행할 수 있는 작업을 결정

- HTTP
  - HTML 문서와 같은 리소스들을 가져올 수 있도록 해주는 프로토콜
  - 웹에서 이루어지는 모든 데이터 교환의 기초
  - 비연결지향
    - 서버는 요청에 대한 응답을 보낸 후 연결을 끊음
  - 무상태
    - 연결을 끊는 순간 클라이언트와 서버간의 통신이 끝나며 상태 정보가 유지되지 않음
    - 클라이언트와 서버가 주고받는 메세지들은 서로 완전히 독립적임





- 쿠키

  - 클라이언트와 서버의 지속적인 관계를 유지하기 위해 존재

  - 사용자가 웹사이트를 방문할 경우 해당 웹사이트의 서버를 통해 사용자의 컴퓨터에 설치되는 작은 기록 정보 파일

  - HTTP 쿠키는 상태가 있는 세션을 만들어줌

  - 두 요청이 동일한 브라우저에서 들어왔는지 아닌지를 판단할 때 주로 사용

    - 사용자의 로그인 상태를 유지할 수 있음
    - 상태가 없는 HTTP 프로토콜에서 상태 정보를 기억시켜 주기 때문

  - 웹 페이지에 접속하면 요청한 웹페이지를 받으며 쿠키를 저장(KEY-VALUE)하고,

    클라이언트가 같은 서버에 재요청시 요청과 함께 쿠키도 함께 전송

  - 사용목적

    - 세션관리 : 로그인, 아이디 자동완성, 공지 하루 안보기, 팝업 체크, 장바구니 등
    - 개인화 : 사용자 선호, 테마 등의 설정
    - 트래킹 : 사용자 행동을 기록 및 분석

  - 수명

    - session cookies : 현재 세션이 종료되면 삭제됨. 클라이언트가 현재 세션이 종료되는 시기를 정의
    - persistent cookies : expires 속성에 지정된 날짜 혹은 max-age 속성에 지정된 기간이 지나면 삭제



- 세션

  - 클라이언트와 서버의 지속적인 관계를 유지하기 위해 존재

    - 사이트와 특정 브라우저 사이의 상태를 유지시키는 것

  - 클라이언트가 서버에 접속하면 서버가 특정 session id를 발급하고, 클라이언트는 발급 받은 session id를 쿠키에 저장

    - 클라이언트가 다시 서버에 접속하면 요청과 함께 session id가 저장된 쿠키를 서버에 전달
    - 쿠키는 요청 때마다 서버에 함께 전송되므로 서버에서 session id를 확인해 알맞은 로직을 처리
    - id는 세션을 구별하기 위해 필요하며, 쿠키에는 id만 저장함

  - Django는 특정 session id를 포함하는 쿠키를 사용해서 각각의 브라우저와 사이트가 연결된 세션을 알아냄

    - 세션 정보는 django db의 django_session 테이블에 저장됨

    

    

    

- 로그인 (AuthenticationForm)
  - session을 create
  - 현재 세션에 연결하려는 인증된 사용자가 있는 경우
  - HttpRequest(request) 객체와 User 객체가 필요
  - django의 session framework를 사용하여 세션에 user의 ID를 저장(==로그인)
  - login 함수를 auth_login으로 변경 (login view 함수와의 혼동을 방지)
  - get_user() : AuthenticationForm의 인스턴스 메서드. 인스턴스의 유효성을 먼저 확인하고 인스턴스가 유효할 때만 user를 제공하려는 구조
    - 인스턴스 생성 시에 None으로 할당되며, 유효성 검사를 통과했을 경우 로그인한 사용자 객체로 할당됨 

```python
#accounts/views.py
from django.contrib.auth import login as auth_login
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.views.decorators.http import require_http_methods

@require_http_methods(['GET','POST'])
def login(request) :
    if request.user.is_authenticated: #로그인된 사용자는 로그인 버튼 볼 필요 없다
        return redirect('articles:index')

    if request.method == 'POST': #로그인 처리
        form = AuthenticationForm(request, request.POST)
        if form.is_valid(): #유효성 검사를 통과했을 경우
            auth_login(request, form.get_user()) #HttpRequest 객체와 User객체
            return redirect(request.GET.get('next') or 'articles:index') #로그인이 정상적으로 진행되면 기존에 요청했던 주소로 redirect하기 위해 주소를 keep

    else: #로그인 창
        form = AuthenticationForm()
    context = {
        'form' : form
    }
    return render(request, 'accounts/login.html', context)
```



- 로그아웃
  - session을 delete
  - httpRequest 객체를 인자로 받고 반환값이 없음
  - 사용자가 로그인하지 않은 경우 오류를 발생시키지 않음
  - 현재 요청에 대한 session data를 db에서 완전히 삭제하고 클라이언트의 쿠키에서도 sessionid가 삭제됨 (다른 사람이 동일한 웹브라우저를 사용하여 로그인하고, 이전 사용자의 세션 데이터에 액세스 하는 것을 방지하기 위함)

```
#accounts/views.py
from django.views.decorators.http import require_http_methods, require_POST
from django.contrib.auth import logout as auth_logout
from django.shortcuts import render, redirect

@require_POST
def logout(request) : 
    if request.user.is_authenticated:
        auth_logout(request)
    return redirect('articles:index') 
```



- 로그인 사용자에 대한 접근 제한
  - is_authenticated 
    - User model의 속성 중 하나
    - AnonymousUser을 제외한 모든 User 인스턴스에 대해 항상 True인 읽기 전용 속성
    - 단, 권한과는 관련이 없으며 사용자가 활성화 상태이거나 유효한 세션을 가지고 있는지도 확인하지 않음
    - 이를 활용하여 로그인과 비로그인 상태에서 출력되는 링크를 다르게 설정할 수 있고, 인증된 사용자만 게시글 작성 링크를 볼 수 있도록 처리 가능
  - login_required decorator
    - 인증 성공 시 사용자가 redirect 되어야 하는 경로는 next라는 쿼리 문자열 매개변수에 저장됨 (로그인이 정상적으로 진행되면 기존에 요청했던 주소로 redirect하기 위해 주소를 keep)
    - @require_POST가 작성된 함수에 @login_required를 함께 사용하는 경우 에러 발생
      - 로그인 이후 next 매개 변수를 따라 해당 함수로 다시 redirect되는데 이 때 require_POST 때문에 405 에러가 발생하게 됨
    - login_required는 get method request를 처리할 수 있는 view 함수에서만 사용해야 함.



- 회원가입(UserCreationForm)
  - 주어진 username과 password로 권한이 없는 새 user를 생성하는 ModelForm
  
  - User 모델 대체하기
  
    - 일부 프로젝트에서는 Django의 내장 User모델이 제공하는 인증 요구사항이 적절하지 않을 수 있음
  
    - Django는 User을 참조하는 데 사용하는 <u>AUTH_USER_MODEL</u> 값을 제공하여, <u>default user model을 재정의(override)</u>할 수 있도록 함 (AUTH_USER_MODEL은 프로젝트가 진행되는 동안 변경할 수 없음)
  
    - Django는 새 프로젝트를 시작하는 경우 기본 사용자 모델이 충분하더라도, 커스텀 유저 모델을 설정하는 것을 강력하게 권장 (단, 프로젝트의 모든 migrations 혹은 첫 migrate를 실행하기 전에 이 작업을 마쳐야 함)
  
    - 프로젝트 중간에 진행했다면 데이터베이스를 초기화한 후 마이그레이션 진행
  
      (db.sqlite3 파일 삭제 -> 파일 명에 숫자 붙은 migrations 파일 모두 삭제)
  
      (오류 날 경우 pycache도 삭제하고 makemigrations -> migrate 진행)

```python
#accounts/models.py
#관리자 권한과 함께 완전한 기능을 갖춘 user모델을 구현하는 기본 클래스인 AbstractUser을 상속받아 새로운 User모델 작성
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
	pass

#settings.py
#기존에 Django가 사용하는 User모델이었던 auth 앱의 User 모델을 accounts 앱의 User모델을 사용하도록 변경

AUTH_USER_MODEL = 'accounts.User'

#accounts/admin.py
#admin site에 Custom User 모델 등록
from django contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

admin.site.register(User, UserAdmin)

#accounts/forms.py

from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.contrib.auth import get_user_model

class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = get_user_model() #user
        fields = UserCreationForm.Meta.fields + ('email',)
        
        
#accounts/views.py
def signup(request):
    if request.user.is_authenticated:
        return redirect('articles:index')
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            #회원 가입 후 자동으로 로그인 진행하기
            user = form.save() 
            auth_login(request, user)
            return redirect('articles:index')
    else:
        form = CustomUserCreationForm()
    context = {
        'form':form
    }

    return render(request, 'accounts/signup.html', context)


```





- 회원탈퇴
  - db에서 사용자를 삭제하는 것과 같음

```
@require_POST
def delete(request):
    if request.user.is_autenticated:
        request.user.delete()
        auth_logout(request) #탈퇴하면서 해당 유저의 세션 데이터도 함께 지움
    return redirect('articles:index')

```

- 회원정보 수정 (UserChangeForm)
  - UserChangeForm 사용 시 문제점
    - 일반 사용자가 접근해서는 안될 정보들까지 모두 수정이 가능해짐
    - 따라서 UserChangeForm을 상속받아 CustomerUserChangeForm이라는 서브클래스를 작성해 접근 가능한 필드를 조정해야 함
  - get_user_model()
    - 현재 프로젝트에서 활성화된 사용자 모델을 반환

```python
#accounts/forms.py
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.contrib.auth import get_user_model
from .forms import CustomUserChangeForm

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = get_user_model() #user
        fields = ('email', 'first_name', 'last_name') #수정시 필요한 필드만 선택해서 작성

@login_required
@require_http_methods(['GET','POST'])
def update(request):
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('articles:index')
    else:
        form = CustomUserChangeForm(instance=request.user)
    context = {
        'form' : form,
    }
    return render(request, 'accounts/update.html', context)

```



- 비밀번호 변경

```
from django.contrib.auth.forms import PasswordChangeForm

@login_required
@require_http_methods(['GET','POST'])
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user) #비밀번호 바꿔도 세션 유지
            return redirect('articles:index')
    else:
        form = PasswordChangeForm(request.user)
    context = {
        'form' : form,
    }
    return render(request, 'accounts/change_password.html', context)
```



- 
