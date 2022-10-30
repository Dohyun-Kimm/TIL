from django.views.decorators.http import require_http_methods, require_POST, require_safe
from django.shortcuts import render, redirect

from .models import Article, Comment
from .forms import ArticleForm, CommmentForm
# Create your views here.

@require_safe
def index(request):
    articles = Article.objects.all()
    forms = ArticleForm(articles)
    context = {
        'forms':forms,
    }
    return render(request,'articles/index.html',context)
    

def detail(request,pk):
    article = Article.objects.get(pk=pk)
    form = ArticleForm(article)
    context = {
        'form': form,
    }
    return render(request,'articles/detail.html',context)


def create(request):    
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save()
            return redirect('article:detail', article.pk)
    else:
        form = ArticleForm()
    context = {
        'form':form,
    }
    return render(request, 'articles/create/', context)


def update(request,pk):
    article = Article.objects.get(pk=pk)
    if request.method =='POST':
        form = ArticleForm(article, instance = request.POST)
        if form.is_valid():
            form.save()
            return redirect('articles:detail',pk)
    form  =ArticleForm(instance = article)
    context={
        'form':form,
        'article':article,
    }
    return render(request,'articles/update.html',context)


def delete(request,pk):
    article = Article.objects.get(pk=pk)
    article.delete()
    return redirect("article:index")

def comment_create(request):
    pass
def comment_delete(request):
    pass