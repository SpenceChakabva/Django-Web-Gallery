from django.urls import path
from . import views

"""Base_App 
    urls patterns main views and CRUD views
"""
urlpatterns = [
    path('', views.home, name="home"),
    path('post/<str:pk>/', views.post, name="post"),
    path('about/', views.about, name="about"),

    # CRUD Paths
    path('create_post/', views.createPost, name="create_post"),
    path('update_post/<str:pk>/', views.updatePost, name="update_post"),
    path('delete_post/<str:pk>/', views.deletePost, name="delete_post"),
]