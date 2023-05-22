from django.contrib.admin import site
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def signup(request):
    if request.method == "POST":
        get_email = request.POST.get('email')
        get_password = request.POST.get('pass1')
        get_confirm_password = request.POST.get('pass2')

        if get_password != get_confirm_password:
            messages.error(request, 'Passwords do not match')
            return redirect('/auth/signup/')

        if User.objects.filter(username=get_email).exists():
            messages.warning(request, 'Email is already taken')
            return redirect('/auth/signup/')

        myuser = User.objects.create_user(get_email, get_email, get_password)
        login(request, myuser)
        messages.success(request, 'User created and logged in successfully')
        return redirect('/')

    return render(request, 'signup.html')

def handleLogin(request):
    if request.method == "POST":
        get_email = request.POST.get('email')
        get_password = request.POST.get('pass1')

        myuser = authenticate(username=get_email, password=get_password)

        if myuser is not None:
            if myuser.is_superuser or myuser.username == 'admin':
                messages.success(request, 'Admin logged in successfully')
            else:
                messages.success(request, 'User logged in successfully')
            login(request, myuser)
            return redirect('/')
        else:
            messages.error(request, 'Invalid credentials')

    site_name = site.site_title if site.site_title else 'Django administration'
    return render(request, 'login.html', {'site_name': site_name})

def handleLogout(request):
    logout(request)
    messages.success(request, 'Logged out successfully')
    return render(request, 'login.html')
