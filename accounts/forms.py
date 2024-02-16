from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ["username", "email", "bio"]


class UserEditForm(ModelForm):
    class Meta:
        model = CustomUser
        fields = ["username", "email", "bio", "avatar"]
