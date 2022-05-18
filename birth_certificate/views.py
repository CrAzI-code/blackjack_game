from urllib.request import parse_keqv_list
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
import random

from birth_certificate.models import PaymentToken, PersonalData

# Create your views here.

def index(request):
    if request.method == 'POST':
        person_name = request.POST['person_name']
        card_number = request.POST['card_number']
        expirydate = request.POST['expirydate']
        cvv =  request.POST['cvv']

        token = random.randbytes(15).hex()
        paymentCode = PaymentToken.objects.create(user = request.user, token = token)       
        paymentCode.save()

        return render(request, 'index.html', {'generated':True, 'show_token':paymentCode.token})
    if request.method == "GET" and request.GET.get('token', None) is not None:
        token = request.GET['token']
        
        if PaymentToken.objects.filter(token=token).exists():
            return render(request, "index.html", {"success": True, "token": token})
        else:
            return render(request, "index.html", {"success": False})
    
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
                auth.authenticate(username=username, password=password)
                return redirect('birth_certificate:index')
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
            return redirect('birth_certificate:index')
        else:
            messages.info(request, "invalid username or password")
            return redirect("birth_certificate:login")

    else:
        return render(request, 'login.html')

def generate(request):
    print(request.user)
    if request.method == 'POST':
        fullname = request.POST['fullname']
        fathername = request.POST['fathername']
        gender = request.POST['gender']
        mothername = request.POST['mothername']
        place_of_birth = request.POST['placeofbirth']
        state = request.POST['state']
        time = request.POST['time']
        date = request.POST['date']

        userPersonalData = PersonalData(fullname = fullname, fathername = fathername, gender = gender, mothername = mothername, place_of_birth = place_of_birth, state = state, time = time, date = date)
        userPersonalData.save()
        messages.info(request, "User Data Has Been Saved Successfully")
        return redirect('birth_certificate:generate')
    else:
        return render(request, "generate_certificate.html")

def logout(request):
    auth.logout(request)
    return redirect( 'birth_certificate:index')