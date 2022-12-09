from django.forms import ModelForm, TextInput
from .models import Post

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']

        widgets = {
            'title': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Назначение'
            }),
            'content': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Сумма'
            })
        }