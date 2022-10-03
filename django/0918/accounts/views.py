from re import L
from django.shortcuts import render,redirect
from django.contrib.auth.forms import login as auth_login
from django.contrib.auth.forms import logout as auth_logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from .forms import CustomUserCreationForm
from .forms import CustomUserChangeForm

# Create your views here.
def login(request):
    if request.method == "POST": # req 방식이 포스트라면 
        # 어스 폼안에 리퀘랑, post방식 리퀘 정보를 넣어서 저장해라
        form  = AuthenticationForm(request, request.POST)
        # 만약 폼이 유효한 정보를 가지고 있다면
        if form.is_valid():
            # 로그인 절차를 통과 시켜라 리퀘랑 폼쩜 겟 유저넣고, 성공하면 사용자객체 반환해
            auth_login(request, form.get_user())
            return redirect('articles:index')
    else:
        form = AuthenticationForm()
    context = {
        'form':form,
    }
    return render(request,'accounts/login.html',context)

def logout(request):    # 요청이 들어오면
    auth_logout(request)    # 장고에 있는 로그아웃 모듈로 롷그아웃하기
    return redirect('articles:index')   # 메인 화면으로 보내기

def signup(request):
    if request.method =='POST':
        form = CustomUserCreationForm(request, request.POST)
        if form.is_valid():
            user=form.save()
            auth_login(user)
            return redirect('articles:index')
    else:
        form = CustomUserCreationForm()
    context={
        'form':form,
    }
    return render(request, 'accounts/signup.html',context)

def delete(request):
    request.user.delete() # 유저 정보 삭제
    auth_logout(request)    #  유저 세션도 삭제
    return redirect('articles:index')

def update(request):
    if request.method=='POST':
        form = CustomUserChangeForm(request.POST, instance= request.user )
        if form.is_valid():
            form.save()
            return redirect('aticles:index')
    else:
        form = CustomUserChangeForm(instance = request.user)
    context = {
        'form':form,
    }
    return render(request,'accounts/update.html',context)

def change_password(request):
    if request.method =='POST':
        form = PasswordChangeForm(request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request,form.user)
            return redirect('articles:index')
    else:
        form = PasswordChangeForm(request.user)
    context= {
        'form': form,
    }
    return render(request,'accounts/password.html',context)