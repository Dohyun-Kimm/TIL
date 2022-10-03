from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from .models import User

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = get_user_model()

class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = get_user_model()
        # 회원정보 수정할때 모든 부분을 오픈해버리면 일개 회원이 보면안될 정보들이 노출 될수 잇음
        # 따라서 필드에 들어갈 내용을 정의 해줌으로써  해결!
        fields= ('email','first_name','last_name')

class AccountForm(AuthenticationForm):

    class Meta:
        model= User
        fields = '__all__'
