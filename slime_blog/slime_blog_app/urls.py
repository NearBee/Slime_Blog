from django.urls import path
from django.views.generic import RedirectView
from . import views

urlpatterns = [
    path("", RedirectView.as_view(url="home/", permanent=False)),
    path("home/", views.homepage_view, name="homepage"),
    path("post/<int:pk>/", views.post_details_view, name="post_details"),
    path("post/new/", views.create_post, name="create_post"),
]
