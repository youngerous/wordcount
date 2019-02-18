from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('<int:blog_id>/', views.detail, name="detail"), #blog_id는 models.py에 넘겨주는 인자
    path('new/', views.new, name="new"),
    path('create/', views.create, name="create"),
    path('newblog/', views.blogpost, name="newblog"),
]