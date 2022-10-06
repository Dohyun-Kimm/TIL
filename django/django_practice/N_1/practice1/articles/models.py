from django.db import models
from django.conf import settings
# Create your models here.
# comment 가 article 참조함과 동시에 article에서도 comment에대한 접근 방법이 생김
# comment_set
class Article(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    title = models.CharField(max_length=10)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    # 누구꺼 (참조할 모델의 소문자 단수형으로 이름 만들기)
    #   1. 참조할 테이블 이름, 
    #   2. on_delete 옵션,  models.CASCADE / NO_USER_NAME < SET_DEFAULT <-거으 안씀
    #   3. related_name =  comment_set 대신에 쓸 이름을 정해줌 규칙은 참조될 클래스의 소문자 복수형
    article = models.ForeignKey(Article, on_delete = models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    # 1. 댓글정보 (문자)
    content = models.CharField(max_length = 300)
    # 2. 언제 만들어졌는지
    created_at = models.DateTimeField(auto_now_add= True)
    # 3. 수정일 
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.content