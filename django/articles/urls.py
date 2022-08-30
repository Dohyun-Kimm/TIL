from django.urls import path
from . import views

app_name = 'articles'
urlpatterns = [
    path('articles/',views.index, name='index'),        # 같은 주소를 공유할 경우 name을 다르게 할수있음
    path('articles/',views.throw,name='throw'),
    path('articles/',views.catch, name ='catch')
]
