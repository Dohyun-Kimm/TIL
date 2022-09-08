from django import forms
from .models import Article
# class ArticleForm(forms.Form):
#     title = forms.CharField(max_length=10)
#     content = forms.CharField(widget=forms.Textarea)
#     CLASS_A = 's1'
#     CLASS_B = 's2'
#     CLASS_C = 's3'
#     CLASS_D = 's4'
#     CLASS_E = 's5'
#     CLASS_F = 's6'
    
#     CLASS_CHOICES = [
#         (CLASS_A, '1반'),
#         (CLASS_B, '2반'),
#         (CLASS_C, '3반'),
#         (CLASS_D, '4반'),
#         (CLASS_E, '5반'),
#         (CLASS_F, '6반'),
#     ]
#     ssafyclass = forms.ChoiceField(choices = CLASS_CHOICES)
    
#     # 


class ArticleForm(forms.ModelForm):
    title = forms.CharField(
        label = "title",
        widget= forms.TextInput(
            attrs={
                # 'class': 'my-title',
                'placeholder' : '제목 입력 하게요',
                'maxlength' : 10,
            }
        ),
        error_messages = {
            'required' : '반드시 입력행합니다.',
        }
    )
    content = forms.CharField(
        label= "Content",
        widget = forms.Textarea(
            attrs={
                'placeholder': '내용 입력하기',
                'rows': 4,
            }
        )

    )
    class Meta:
        model = Article
        # fields = '__all__'
        exclude = ('safyclass',) # 쉼표가 있어야 튜플로 인식한다
