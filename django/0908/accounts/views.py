from django.shortcuts import render,redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import PasswordChangeForm
from .forms import CustomUserChangeForm, CustomUserCreationForm
# from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import  login as auth_login # 장고에서 가져온 로그인 함수
from django.contrib.auth import  logout as auth_logout # 장고에서 가져온 로그out 함수


# 내가 정리한 로그인 로직
def login(request):
    if request.method =="POST":
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user()) #유저의 정보
            return redirect('articles:index')
    else:
        form  = AuthenticationForm()

    context = {
        'form' : form,
    }
    return render(request,'accounts/login.html',context)


def logout(request):
    auth_logout(request)
    return redirect('articles:index')


def signup(request):
    if request.method =='POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.save()
            auth_login
            return redirect('articles:index')
    else:
        form = CustomUserCreationForm()
    context={
        'form': form,
    }
    return render(request,'accounts/signup.html',context)


def delete(request):
    request.user.delete()
    return redirect('articles:index')

def update(request):
    # 1. 유저의정보가 보여져야 한다.
    # GET
    if request.method =='POST':
        form =CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('articles:index')
    else:
        form = CustomUserChangeForm(instance=request.user)
    context= {
        'form' : form,
    }
    return render(request,'accounts/update.html',context)

    # 2.수정-> 요철
    #POST

def change_password(request):
    if request.method == "POST":
        form =PasswordChangeForm(user=request.user,data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('articles:index')
        # 비번저장
    else:
        form = PasswordChangeForm(request.user)
    context = {
        'form' : form,
    }
    return render(request, 'accounts/change_password.html',context)