from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages


def register(request):
    if request.user.is_authenticated:
        return redirect('index')

    if request.method == 'POST':
        first = request.POST['first']
        last = request.POST['last']
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']

        if len(first) < 3 or len(last) < 3 or len(email) < 8 or len(username) < 3 or len(password) < 5:
            messages.error(request, 'Invalid Form!')
            return redirect('register')

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already taken')
            return redirect('register')

        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email already exists')
            return redirect('register')

        user = User.objects.create_user(
            first_name=first,
            last_name=last,
            email=email,
            username=username,
            password=password,
        )

        return redirect('login')
    else:
        return render(request, 'accounts/register.html')


def login(request):
    if request.user.is_authenticated:
        return redirect('index')


    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        attempt = User.objects.filter(email=email).first()
        if not attempt:
            messages.error(request, 'Invalid Credentials')
            return redirect('login')

        username = attempt.username
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('index')
        else:
            messages.error(request, 'Invalid Credentials')
            return redirect('login')
    else:
        return render(request, 'accounts/login.html')


def logout(request):
    if not request.user.is_authenticated:
        return redirect('index')
    
    if request.method == 'POST':
        auth.logout(request)
        messages.info(request, 'Logged out')
    return redirect('index')


def profile(request):
    if not request.user.is_authenticated:
        return redirect('index')
    return render(request, 'accounts/profile.html')