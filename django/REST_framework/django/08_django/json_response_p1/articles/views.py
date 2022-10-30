from http.client import HTTPResponse
from .models import Article
from django.shortcuts import render
from django.core import serializers
from .serializers import ArticleSerializer
from rest_framework.response import Response
def article_html(request):
    articles = Article.objects.all()
    context = {
        'articles' : articles,
    }
    return render(request, 'articles/index.html',context)


def article_json1(request):
    articles = Article.objects.all()
    article_json = []

    for article in articles:
        # 리스트에 추가하기
        article_json.append(
            {
                'id': article.pk,
                'title': article.title,
                'content': article.content,
                'created_at': article.created_at,
                'updated_at': article.updated_at,
            }
        )
        # 키-벨류 타입으로
        # 리턴 받기 
        pass
def article_json2(request):
    articles = Article.objects.all()
    # datatype 지정해주어야한다. 
    data = serializers.serialize('json',articles)
    return HTTPResponse(data, safe=False)

def article_json3(request):
    articles = Article.objects.all()
    serializer = ArticleSerializer(articles, many=True)
    return Response(serializer.data)