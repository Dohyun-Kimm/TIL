from django.contrib.auth import get_user_model # 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import UserChangeForm #수정할떄

class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = get_user_model()



class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = get_user_model()
        fields= ('email','first_name','last_name',)