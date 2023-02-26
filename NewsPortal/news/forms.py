from django import forms
from .models import Post
from django.core.exceptions import ValidationError




class PostForm(forms.ModelForm):
    post_text = forms.CharField(min_length=20)

    class Meta:
        model = Post
        fields = ['post_name','post_text','post_news','author',]
        label = {
            'post_name': 'Название',
            'post_text': 'Текст',
            'post_news': 'Категория',
            'author': 'Автор',
        }

    def clean(self):
        cleaned_data = super().clean()
        post_text = cleaned_data.get("post_text")
        post_name = cleaned_data.get("post_name")
        if post_name == post_text:
            raise ValidationError(
                "Текст статьи не должен быть идентичен названию."
            )

        return cleaned_data

