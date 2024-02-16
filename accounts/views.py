from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import CustomUser
from .forms import CustomUserCreationForm, UserEditForm


# Create your views here.
def login_view(request):
    if request.method == "POST":
        print(request.POST)
        username = request.POST.get("username")
        password = request.POST.get("password")
        try:
            user = CustomUser.objects.get(username=username)
        except:
            messages.error(request, "Invalid Username")
        else:
            user = authenticate(request, username=username, password=password)
            if not user:
                messages.error(request, f"Invalid password for username '{username}'")
            else:
                login(request, user)
                return redirect("home")

    return render(request, "accounts/login.html")


def logout_view(request):
    logout(request)
    return redirect("home")


def signup_view(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
        else:
            messages.error(request, "An error occured during registration.")
    form = CustomUserCreationForm()
    return render(request, "accounts/signup.html", {"form": form})


def edit_user(request):
    if request.method == "POST":
        print(request.POST.get("avatar"))
        form = UserEditForm(
            data=request.POST, files=request.FILES, instance=request.user
        )
        if form.is_valid():
            form.save()
            return redirect("home")
        else:
            messages.error("You submitted an invalid form.")
    form = UserEditForm(instance=request.user)
    return render(request, "accounts/edit-user.html", {"form": form})
