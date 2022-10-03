from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleForm
from django.views.decorators.http import require_POST
# 장고안에 뷰 관련된 모듈중에 함수 위에 쓰는거니까 데코가 필요하고, http에대한거 그중에서도 포스트방식만 허용하는
# Create your views here.
def index(request):
    # DB에 전체 데이터를 조회
    articles = Article.objects.all() # <- model에 있는 메소드임
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html',context)
def create(request):
    form = ArticleForm()    # ArticleForm 인스턴스 생성
    if request.method=='POST':# 만약 psot형식이면
        form = ArticleForm(request.POST) # 요청에 포스트 형식으로 들어온정보를 폼에 저장 
        if form.is_valid(): # 폼에 들어온 정보가 오류가 없다면
            article = form.save() # article이라는 변수에 그정보를 담음
            return redirect('articles:detail',article.pk) # pk에 해당하는 정보를 디테일 페이지로 재전송
    #그렇지 않은 정보들은 콘텍스트에 담아서 원래 입력이 왔던 페이지인 create 페이지로 그대로 돌려보냄
    # 입력했었던 정보를 보여주기위해 콘텍스트변수에 담에서 보내줌
    print(f'error: {form.errors}') # is_valid 토과 못하면 원인을 알려줌
    context = {
        'form':form,
    }
    return render(request,'articles/create.html',context)

def detail(request, pk): # variable 라우팅값으로 받는 pk값으로 데이터 반환
    # 전체 데이터를 반환 하는것이 아니라 개별 데이터를 반환 할때는 고유 값인 pk값 활용
    article = Article.objects.get(pk=pk)
    context = {
        'article': article,
    }
    return render(request,'articles/detail.html',context)

def delete(request, pk):
    # 지우려면, 지우려고 하는 데이터를 먼저조회해야한다. pk 값으로 조회
    article =Article.objects.get(pk=pk)
    if request.method =="POST":
        article.delete()
        return redirect('articles:index')
    return render(request,'articles/detail.html',article.pk)

@require_POST
def update(request,pk):
    # 개별 데이터를 수정항려고 하는 것이기 때문에 pk값으로 데이터를받아와ㅓㅅ article에저장
    article = Article.objects.get(pk=pk)
    if request.method =="POST":
        form = ArticleForm(request.POST,instance= article)
        if form.is_valid():
            form.save()
            return redirect('articles:detail',article.pk)
    else:
        form = ArticleForm(instance=article)
    context = {
        'article':article,
        'form':form,
    }
    return render(request,'articles/update.html',context)