<<<<<<< Updated upstream
from django.contrib import messages, auth
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.urls import reverse
from .forms import UserForm
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.

def index(request):
    users = User.objects.all().order_by("-id")
    
    context = {
        "users": users
    }
    
    return render(request, "users/index.html", context)

def create(request):
    
    form_action = reverse("users:create")
    
    #POST
    if request.method == "POST":
        form = UserForm(request.POST)
        
        if form.is_valid():
            form.save()
            
            messages.success(request, "O usuário foi cadastrado com sucesso!")
            
            return redirect("users:index")
        
        context = {
            "form": form
        }
        
        return render(request, "users/create.html", context)
    
    # GET
    
    form = UserForm()
    
    context = {
        "form": form
    }
    
    return render(request, "users/create.html", context)

def login(request):
    #POST
    
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        
        if form.is_valid():
            user = form.get_user()
            auth.login(request, user)

            return redirect("homepage:index")
        
    #GET
    form = AuthenticationForm(request)
    
    context = {
        "form": form
    }
    
    return render(request, "users/login.html", context)
=======
from django.shortcuts import render
from django.contrib.auth.models import User

def create(request):
    return render(request, "users/create.html")

def login(request):
    return render(request, "users/login.html")
>>>>>>> Stashed changes
