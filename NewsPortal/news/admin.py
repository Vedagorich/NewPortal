from django.contrib import admin
from .models import Category, Post, Author, Post_Category


class PostAdmin(admin.ModelAdmin):
    # list_display — это список или кортеж со всеми полями, которые вы хотите видеть в таблице
    list_display = ('post_name', 'rating_post', 'post_news', 'author')
    # генерируем список имён всех полей для более красивого отображения


admin.site.register(Category)
admin.site.register(Post)
admin.site.register(Author)
admin.site.register(Post_Category)
