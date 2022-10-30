from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from .forms import CustomUserCreationForm, CustomUserChangeForm

# Create your views here.
def login(request):
    if request.user.is_authenticated:
        return redirect('articles:index')
    if request.method =="POST":
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect("articles:index")
    else:
        form = AuthenticationForm(request)
        context = {
            'form':form,
        }
        return render(request, "accounts/login.html",context)

def logout(request):
    if request.user.is_authenticated:
        auth_logout(request)
    return redirect("articles:index")

def signup(request):

    if request.method =="POST":
        form = CustomUserCreationForm(request)
        if form.is_valid():
            user =form.save()
            auth_login(user)
            return redirect("articles:index")
    else:
        form = AuthenticationForm(request)
    context = {
        'form': form,
    }
    return render(request, "accounts/signin.html", context)


def delete(request):
    if request.user.is_authenticated:
        request.user.delete()
        auth_logout(request)
    return redirect('aritcles:index')

def update(request):
    if request.method =='POST':
        form = CustomUserChangeForm(request.POST, instance = request.user)
        if form.is_valid():
            form.save()
            return redirect('articles:index')

    else:
        form = CustomUserChangeForm(instance = request.user)
    context = {
        'form': form,
    }
    return render(request, "articles/update.html", context)


