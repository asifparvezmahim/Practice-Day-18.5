from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib import messages
from django.contrib.auth.forms import (
    AuthenticationForm,
    PasswordChangeForm,
    SetPasswordForm,
)
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash


# Create your views here.
def signup(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            form = RegisterForm(request.POST)
            if form.is_valid():
                messages.success(request, "Account Created Sucessfully")
                form.save()
        else:
            form = RegisterForm()
        return render(request, "signup.html", {"form": form})
    else:
        return redirect("profile")


def home(request):
    return render(request, "home.html")


def user_login(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            form = AuthenticationForm(request=request, data=request.POST)
            if form.is_valid():
                name = form.cleaned_data["username"]
                userpass = form.cleaned_data["password"]
                user = authenticate(username=name, password=userpass)
                if user is not None:
                    messages.success(request, "Logged in Successfully")
                    login(request, user)
                    return redirect("profile")

                else:
                    return redirect("homepage")

        else:
            form = AuthenticationForm()
        return render(request, "login.html", {"form": form})
    else:
        return redirect("profile")


def profile(request):
    if request.user.is_authenticated:
        return render(request, "profile.html", {"user": request.user})
    else:
        return redirect("login")


def user_logout(request):
    messages.success(request, "Log Out Successsfully")
    logout(request)
    return redirect("login")


def changePassWithOlderPass(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = PasswordChangeForm(user=request.user, data=request.POST)
            if form.is_valid():
                form.save()
                update_session_auth_hash(request, form.user)
                return redirect("profile")
        else:
            form = PasswordChangeForm(user=request.user)
        return render(request, "passChange.html", {"form": form})
    else:
        return redirect("login")


def changePassWithoutOlderPass(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = SetPasswordForm(user=request.user, data=request.POST)
            if form.is_valid():
                form.save()
                update_session_auth_hash(request, form.user)
                return redirect("profile")
        else:
            form = SetPasswordForm(user=request.user)
        return render(request, "passChange.html", {"form": form})
    else:
        return redirect("login")
