from django_filters import FilterSet, DateFilter, CharFilter, ModelChoiceFilter, ChoiceFilter, NumberFilter
from django import forms
from .models import Post, Author, Category


class PostFilter(FilterSet):
    search_title = CharFilter(
        field_name='post_name',
        label='Заголовок',
        lookup_expr='icontains'
    )

    search_rating = NumberFilter(
        field_name='rating_post',
        label='Рейтинг',
        lookup_expr='exact'
    )

    search_author = ModelChoiceFilter(
        empty_label='Все авторы',
        field_name='author',
        label='Автор',
        queryset=Author.objects.all()
    )

    search_category = ModelChoiceFilter(
        empty_label='Все категории',
        field_name='post_category',
        label='Категория',
        queryset=Category.objects.all()
    )

    search_type = ChoiceFilter(
        empty_label='Все типы',
        field_name='post_news',
        label='Тип',
        choices=Post.POSITIONS
    )

    post_date = DateFilter(
        field_name='time_post_add',
        widget=forms.DateInput(attrs={'type': 'date'}),
        label='Дата',
        lookup_expr='date__gte'
    )
