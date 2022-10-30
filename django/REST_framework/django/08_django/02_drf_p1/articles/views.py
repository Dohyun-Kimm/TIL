from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import Article
from .serializers import ArticleListSerializer, ArticleSerializer
from articles import serializers

@api_view(['GET'])
def article_list(request):
    articles = Article.objects.all()
    serializers = ArticleListSerializer(articles, many=True)
    return Response(serializers.data)


@api_view(['GET', 'POST','DELETE','PUT'])
def article_detail(request, pk):
    article = article.objects.get(pk= pk)
    if request.method=='GET':
        serializer = ArticleSerializer(article)
        return Response(serializer.data)
    elif request.method=="POST":
        # 요청으로 들어온 데이터를 가진 인스턴스 생성
        serializer = ArticleSerializer(data=request.data)
        # 유효성 검사 오류가 있는 경우 예외를 발생시킴.
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    elif request.method == 'DELETE':
        # 지워야하는 대상이 어디에 저장되어 있는지 생각하기
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    elif request.method == "PUT":
        # 새로담을 정보와 기존에 있던 정보 둘다 가지고 있는 serilaizer 선언해야함.
        serializer = ArticleSerializer(article, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
