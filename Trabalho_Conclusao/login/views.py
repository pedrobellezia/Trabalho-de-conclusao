from django.shortcuts import render
from django.contrib.auth.models import User
from .forms import UserForm

# Create your views here.

def index(request):
    users = User.objects.all().order_by("-id")
    
    context = {
        "users": users
    }
    
    return render(request, "users/index.html", context)

def create(request):
    # GET
    
    form = UserForm()
    
    context = {
        "form": form
    }
    
    return render(request, "users/create.html", context)

def login(request):
    return render(request, "users/login.html")