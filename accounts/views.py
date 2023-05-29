from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User

def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            #check username
            if User.objects.filter(username=username).exists():
                messages.error(request, 'That username already exists')
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'That email already exists')
                    return redirect('register')
                else:
                    pass
        else:
            messages.error(request, 'Password do not match')
            return redirect('register')
    else:
        return render(request, 'accounts/register.html')

def login(request):
    if request.method == 'POST':
        #register user
        pass
    else:
        return render(request, 'accounts/login.html')


def logout(request):
    return redirect(request, 'index')

def dashboard(request):
    return render(request, 'accounts/dashboard.html')