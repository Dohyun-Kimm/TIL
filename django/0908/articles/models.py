from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=10)
    content =models.TextField()
    # models. 에는 choicefield가 없음
    # ssafyclass = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
