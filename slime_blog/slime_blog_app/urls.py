from django.urls import path
from django.contrib.auth import views as auth_views
from django.views.generic import RedirectView
from . import views

urlpatterns = [
    path("", RedirectView.as_view(url="home/", permanent=False)),
    path("home/", views.homepage_view, name="homepage"),
    path("post/<int:pk>/", views.post_details_view, name="post_details"),
    path("post/new/", views.create_post, name="create_post"),
    # TODO: Add /account/ to each when account page is created
    path("account/register/", views.register, name="register"),
    path("account/profile/<str:username>/", views.profile_view, name="profile"),
    path(
        "account/login/",
        auth_views.LoginView.as_view(template_name="login.html"),
        name="login",
    ),
    path(
        "account/logout/",
        auth_views.LogoutView.as_view(next_page="homepage"),
        name="logout",
    ),
]
