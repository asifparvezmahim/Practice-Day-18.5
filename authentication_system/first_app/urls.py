from django.urls import path
from . import views

urlpatterns = [
    path("signup/", views.signup, name="signup"),
    path("", views.home, name="homepage"),
    path("profile/", views.profile, name="profile"),
    path("login/", views.user_login, name="login"),
    path("logout/", views.user_logout, name="logout"),
    path(
        "pass_change_with_older/",
        views.changePassWithOlderPass,
        name="pass_change_with_older",
    ),
    path(
        "pass_change_without_older/",
        views.changePassWithoutOlderPass,
        name="pass_change_without_older",
    ),
]
