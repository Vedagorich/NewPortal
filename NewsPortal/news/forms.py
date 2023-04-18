from django import forms
from .models import Post, Category, Author
from django.core.exceptions import ValidationError




class PostForm(forms.ModelForm):
    post_text = forms.CharField(min_length=2000)
    category = forms.ModelMultipleChoiceField(queryset=Category.objects.all())

    class Meta:
        model = Post
        fields = ['post_name','post_text','post_news','author', 'category', ]
        labels = {
            'post_name': 'Создайте заголовок',
            'post_text': 'Введите текст',
            'post_news': 'Выберите тип',
            'author': 'Выберите автора',
            'category': 'Выберите категорию',
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

