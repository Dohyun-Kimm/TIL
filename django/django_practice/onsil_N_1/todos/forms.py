from django import forms
from .models import Todo
#####################Form checkbox 완성하기부터 ################
class TodoForm(forms.ModelForm):
    title = forms.CharField(
        label = 'Title',
        widget = forms.CharField(
            attrs = {
                'maxlength': 100,
            }
        ),
    )

    completed = forms.BooleanField( 
        label = 'Title',
        widget = forms.CheckboxInput(
            attrs={
                'checked': False,
            }
        ),     
    )