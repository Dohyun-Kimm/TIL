from django.db import models
from django.conf import settings

class Article(models.Model):
    # 유저정보를 저장하기 위한 필드 추가 -> 모델에 변경사항 생겼기떄문에 해야할일
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=10)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
