from django.urls import path
from . import views

app_name ='aricles'
urlpatterns = [
    path('aticles/', views.article_list),
    path('aticles/<int:pk>', views.article_detail),
    path('aticles/<int:pk>/comment/', views.comment_list),
    
]
