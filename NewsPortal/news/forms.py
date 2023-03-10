from django import forms
from .models import Post
from django.core.exceptions import ValidationError




class PostForm(forms.ModelForm):
    post_text = forms.CharField(min_length=20)

    class Meta:
        model = Post
        fields = ['post_name','post_text','post_news','author',]
        labels = {
            'post_name': 'Создайте заголовок',
            'post_text': 'Введите текст',
            'post_news': 'Выберите категории',
            'author': 'Выберите автора',
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

