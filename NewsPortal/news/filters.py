import django_filters
from django.forms import DateInput
from django_filters import FilterSet, DateFilter
from .models import Post


class PostFilter(FilterSet):
    written_after = django_filters.DateFilter(field_name='time_post_add', lookup_expr='gte')

    class Meta:
        model = Post
        fields = {
            'post_name': ['icontains'],
            'author': ['exact'],


        }
