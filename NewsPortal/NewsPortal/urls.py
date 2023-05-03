
from django.urls import path, include
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('pages/', include('django.contrib.flatpages.urls')),
    path('', include('protect.urls')),
    path('posts/', include('news.urls')),
    path('accounts/', include('allauth.urls')),
    path('sign/', include('allauth.urls')),

]
