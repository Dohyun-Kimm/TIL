from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User
# Register your models here.
admin.site.register(User, UserAdmin)
# 어드민을 사이트에 등록한다( 내가만든 모델이랑 장고유저 어드민을)