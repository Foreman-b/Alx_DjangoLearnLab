from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm
from .models import Post


# Let handle user registration
def home(request):
    posts = Post.objects.all().order_by('-published_date')
    return render(request, "blog/home.html", {'posts':posts})

def register(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = CustomUserCreationForm()
        return render(request, "blog/register.html", {"form": form})


def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect("profile")
    else:
        form = AuthenticationForm()

        return render(request, "blog/login.html", {"form":form})

def logout_view(request):
    logout(request)
    return redirect("login")

@login_required
def profile(request):
    return render(request, "blog/profile.html")
