from django import forms
from .models import Article

# forms.Form 에서 ModelForm으로 바꾸는 이유
# 그냥 폼 클래스는 모델 폼이랑 중복 되는 부분이 너무 많고
# 이미 Article Model Class에 필드에 대한 정보를 작성 했는데 
# 폼 에 맵핑하기위해 폼 ㅍ클래스를 재정의 해야 했음 이걸 쉽게 만들기 위해 모델폼 작성
class ArticleForm(forms.ModelForm):
    # 필드 > 위젯 > 위젯 attrs
    title = forms.CharField(
        label = "Title",        # 필드 이름
        widget= forms.TextInput(    # 위젯에서 입력 형태를 정해주고, 구체적인 속성들 지정을 입력 형태안에 설정
            attrs={
                'placeholder' : '제목',
                'maxlength':10,
            }
        ),
        error_messages={
            'required' :'give me a title',
        },
    )
    
    content = forms.CharField(
        label = "comment",
        widget=forms.Textarea(
            attrs={
                'placeholder': 'comment',
                'rows' : 5,
                'cols' : 30,
            }
        ),
        error_messages={
            'required':'content needed',
        }
    )

    NATION_A = 'kr'
    NATION_B = 'ch'
    NATION_C = 'jp'
    NATIONS_CHOICES = [
        (NATION_A, '한국'),
        (NATION_B, '중국'),
        (NATION_C, '일본'),
    ]

    nation = forms.ChoiceField(
        label = "Nation",
        choices = NATIONS_CHOICES,
        widget = forms.Select(

        ),

    )
    # 메타 클래스는 ModelForm에 대한 정보를 작성하는곳
    # 작성하려면 참조하는 모델이 있어야하는데 그게 아까 만든 models.py의 Article
    # 거기에 들어있는 fields 정보들을 다 가지고옴
    class Meta:
        model = Article 
        # 참조 값을 사용할때 : 함수를 호출하는 것이아니라 
        # 다른 함수에서 필요한 시점에 호출하는 경우 참조값을 그대로 넘겨 사용할수 있게
        fields = '__all__'
        