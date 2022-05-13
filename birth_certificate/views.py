from urllib.request import parse_keqv_list
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages

# Create your views here.

def index(request):
    return render(request, "index.html")

def about(request):
    return render(request, 'about.html')

def gallery(request):
    return render(request, 'gallery.html')

def contact(request):
    return render(request, 'contact.html')

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:

            if User.objects.filter(email=email).exists():
                messages.info(request, 'email already exist')
                return redirect('birth_certificate:register')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username already assigned to another user')
                return redirect('birth_certificate:register')
            else:
                user = User.objects.create_user(username = username, email = email, password = password)
                user.save();
                return redirect('birth_certificate:login')
        else:
            messages.info(request, 'Password not the same')
            return redirect('birth_certificate:register')

    else:
        return render(request, 'register.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username = username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('')
        else:
            messages.info(request, "invalid username or password")
            return redirect("birth_certificate:login")

    else:
        return render(request, 'login.html')

def logout(request):
    return render(request, 'logout.html')