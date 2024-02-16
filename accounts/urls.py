from django.urls import path, include
from .views import login_view, logout_view, signup_view, edit_user

urlpatterns = [
    path("signup/", signup_view, name="signup"),
    path("login/", login_view, name="login"),
    path("edit_user/", edit_user, name="edit-user"),
    path("logout/", logout_view, name="logout"),
]
