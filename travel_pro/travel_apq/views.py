from django.contrib import messages, auth
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User


# Create your views here.


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, "Invalid Username or Password")

            return redirect('login')

    return render(request, 'login.html')


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['cpassword']

        if password == cpassword:

            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username already exist')

                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, "email already exist")

                return redirect('register')
            else:
                user = User.objects.create_user(username=username, password=password, email=email, first_name=firstname,
                                                last_name=lastname)
                user.save()

                return redirect('login')
        else:
            messages.info(request, "Password not matching")

            return redirect('register')

    return render(request, 'register.html')


def logout(request):
    auth.logout(request)

    return redirect('/')
