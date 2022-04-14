from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm, PasswordChangeForm
from django.contrib.auth import login as auth_login, logout as auth_logout, update_session_auth_hash
from .forms import CustomUserChangeForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods, require_POST
# Create your views here.

@require_http_methods(['GET','POST'])
def login(request) :
    if request.user.is_authenticated: #로그인된 사용자는 로그인 버튼 볼 필요 없다
        return redirect('articles:index')

    if request.method == 'POST': #로그인 처리
        form = AuthenticationForm(request, request.POST) #데이터 유효성 검사
        if form.is_valid(): #있는 id/pw라면
            auth_login(request, form.get_user())
            return redirect(request.GET.get('next') or 'articles:index')

    else: #로그인 창
        form = AuthenticationForm()
    context = {
        'form' : form
    }
    return render(request, 'accounts/login.html', context)


#로그인 되어있는 경우에만 로그아웃 가능
@require_POST
def logout(request) : 
    if request.user.is_authenticated:
        auth_logout(request)
    return redirect('articles:index') 


def signup(request):
    if request.user.is_authenticated:
        return redirect('articles:index')
    #회원가입 처리
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            #회원 가입 후 자동으로 로그인 진행하기
            user = form.save() 
            auth_login(request, user)
            return redirect('articles:index')
    #회원가입 화면 보여주기
    else:
        form = UserCreationForm()
    context = {
        'form':form
    }

    return render(request, 'accounts/signup.html', context)


@require_POST
def delete(request):
    if request.user.is_autenticated:
        request.user.delete()
        auth_logout(request) #탈퇴하면서 해당 유저의 세션 데이터도 함께 지움
    return redirect('articles:index')


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

@login_required
@require_http_methods(['GET','POST'])
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            return redirect('articles:index')
    else:
        form = PasswordChangeForm(request.user)
    context = {
        'form' : form,
    }
    return render(request, 'accounts/change_password.html', context)