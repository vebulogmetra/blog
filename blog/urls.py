from django.urls import path
from django.shortcuts import redirect
from .views import posts_show, PostCreate

urlpatterns = [
    path('', lambda request: redirect('show_posts/', permanent=False)),
    path('show_posts/', posts_show, name='posts_show'),
    path('create/', PostCreate.as_view(), name='post_create'),
]
