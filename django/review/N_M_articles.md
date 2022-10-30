## settings.py

VASE_DIR / 'templates',

static_url = '/static/'

AUTH_USER_MODEL = 'accounts.User'



# acricles

## models.py

from django.conf import settings



user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

like_users = models.ManyToManyFields(settings.AUTH_USER_MODEL, related_name='like_articles')

## views

decorators

```python
# 장고안에 뷰안에 데코안에 http에 있음 
from django.views.decorators.http import require_http_methods, require_POST, require_safe
# 로그인에 대한건 어스에 있음
from django.contrib.auth.decorators import login_required

```

index

```python
@require_safe # get방식만 받음
```

detail - context에 댓글 폼과 댓글 목록 담기

```python
def detail(request, pk):
    article = Article.objects.get(pk=pk)
    comment_form = CommentForm()
    comments = article.comment_set.all()
    context = {
        'article': article,
        'comment_form': comment_form,
        'comments': comments,
    }
    return render(request, 'articles/detail.html', context)

```

create - 게시글의 작성자정보를 추가로 담아야함.

```python
@login_required   # 로그인 해야 접근 가능
@require_http_method(['GET','POST']) # get, post 방식만 받음


@login_required
@require_http_methods(['GET', 'POST'])
def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.user = request.user
            article.save()
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm()
    context = {
        'form': form,
    }
    return render(request, 'articles/create.html', context)

```

delete

```
# post방식만 받기
#
```

update - 폼에 request.post, instance인자로 가짐, context에 form. article 담기

comment_create(request, pk)

```
# 로그인이 되어 있어야 작성가능, 로그인 안되어 있으면 로그인창으로 보내기
# 댓글이 달릴 게시글 article에 저장
# form에 post방식으로 온 요청을 객체에 담기
# 유저정보 담기위해 commit = False
# 게시글 정보 담기, 유저정보 담기, 세이브 하기

```

comment_delete(request, article_pk, comment_pk)

```
# 포스트 방식만 받음
# 로그인이 되어있어야 가능
# 지울 댓글 담기
# 작성자와 로그인한사람이 같으면 지우기
```

likes