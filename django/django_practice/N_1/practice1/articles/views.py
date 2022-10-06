from django.views.decorators.http import require_POST
from django.shortcuts import render, redirect, get_object_or_404
from .models import Article, Comment
from .forms import ArticleForm, CommentForm



# Create your views here.
def index(request):
    # DB에 전체 데이터를 조회
    articles = Article.objects.all()
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)


def create(request): # 로그인정보가 리퀘안에 다 들어가있음
    form = ArticleForm()
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save(commit= False)
            article.user = request.user
            article.save()
            return redirect('articles:detail', article.pk)
    
    context = {
        'form': form,
    } 
    return render(request, 'articles/create.html', context)
    


def detail(request, pk):
    # variable routing으로 받은 pk 값으로 데이터를 조회
    article = Article.objects.get(pk=pk)
    comment_form = CommentForm()
    # 역참조
    comments = article.comment_set.all()
        # 1. 댓글 보여주기 위한
        # 2. 역참조

    context = {
        'article': article,
        'comment_form':comment_form,
        'comments': comments,
    }
    return render(request, 'articles/detail.html', context)


def delete(request, pk):
    article = Article.objects.get(pk=pk)
    if request.user.is_authenticated:
        if request.user == article.user:
            article.delete()
            return redirect('articles:index')
    return render(request, 'articles/detail.html')


def update(request, pk):
    article = Article.objects.get(pk=pk)
    if request.user == article.user:
        if request.method == 'POST':
            form = ArticleForm(data=request.POST, instance=article)
            if form.is_valid():
                form.save()
                return redirect('articles:detail', article.pk)
        else:
            form = ArticleForm(instance=article)
    else:
        return redirect('articles:index')

    context = {
        'article': article,
        'form': form,
    }

    return render(request, 'articles/update.html', context)

@require_POST
def comments_create(request,pk):
    if request.user.is_authenticated:
    # 데이터 받을 판을 만들어 주는 것 form
        comment_form = CommentForm(request.POST)
    article = Article.objects.get(pk=pk) # article_pk 내가 얻어온 pk 값
    
    if comment_form.is_valid():
        comment = comment_form.save(commit=False) # 저장 잠시 대기시키기
        # 필수 값 넣어주기 article
        # print(comment.content)
        comment.article = article
        comment.user = request.user
        comment.save()
    return redirect('articles:detail', article.pk)

    # GET -> 보여주기
    # POST -> 저장
# def comments_delete(request,comment_pk):
#     comment = Comment.object.get(pk= comment_pk)
#     article_pk = comment.article.pk
#     comment.delete()
#     return redirect('articles:detail',article_pk)

def comments_delete(request,article_pk, comment_pk):
    comment = get_object_or_404(Comment, pk= comment_pk)
    if request.user == comment.user :
        comment.delete()
    return redirect('articles:detail',article_pk)