
from .models import Register, Seat, BusDetail
from django.shortcuts import render, redirect
from django.contrib import messages


def register(request):
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        address = request.POST['address']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        if password == confirm_password:
            if Register.objects.filter(email=email).exists():
                messages.info(request, 'Email already registered')
                return redirect("login")
            else:
                user = Register.objects.create(first_name=first_name, last_name=last_name,
                                              email=email, password=password, address=address)
                user.save()
            return redirect("login")
        else:
            messages.info(request, 'Password do not match')
            return redirect('register')
    else:
        return render(request, 'index2.html')

def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = Register.objects.get(email=email)
        if user.password == password:
            # request.session[''] = request.POST['username']
            return redirect('seat')
        else:
            messages.info(request, 'Invalid Credentials')
            return redirect('login')
    else:
        return render(request, 'login.html')

def index(reqest):
    bus = BusDetail.objects.get(id=2)
    model = Seat.objects.filter(bus=bus)
    return render(reqest, 'seat.html', {"model": model})

