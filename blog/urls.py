# blog/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Route for the home page
    path('posts/', views.post_list, name='post_list'),  # Route for listing posts
    path('post/<slug:slug>/', views.post_detail, name='post_detail'),  # Route for post details
]

