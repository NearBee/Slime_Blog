from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage_view, name='homepage'),
    path('post/<int:pk>/', views.post_details_view, name='post_details'),
    path('post/new/', views.create_post, name='create_post'),
]