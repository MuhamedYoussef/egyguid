from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib.auth.decorators import login_required
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

        if User.objects.filter(username=username.lower()).exists():
            messages.error(request, 'Username already taken')
            return redirect('register')

        if User.objects.filter(email=email.lower()).exists():
            messages.error(request, 'Email already exists')
            return redirect('register')

        user = User.objects.create_user(
            first_name=first,
            last_name=last,
            email=email.lower(),
            username=username.lower(),
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

        attempt = User.objects.filter(email=email.lower()).first()
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


@login_required
def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.info(request, 'Logged out')
    return redirect('index')


@login_required
def profile(request):
    return render(request, 'accounts/profile.html')


@login_required
def edit(request):
    if request.method == 'POST':
        first = request.POST['first']
        last = request.POST['last']
        email = request.POST['email']
        username = request.POST['username']
        image = request.FILES.get('img', False)
        # password = request.POST['password']

        if len(first) < 3 or len(last) < 3 or len(email) < 8 or len(username) < 3:
            messages.error(request, 'Invalid Form!')
            return redirect('edit')

        if User.objects.filter(username=username.lower()).exclude(id=request.user.id).exists():
            messages.error(request, 'Username already taken')
            return redirect('edit')

        # if password:
        #     if len(password) < 5:
        #         messages.error(request, 'Invalid Form!')
        #         return redirect('edit')

        if User.objects.filter(email=email.lower()).exclude(id=request.user.id).exists():
            messages.error(request, 'Email already exists')
            return redirect('edit')

        request.user.first_name = first
        request.user.last_name = last
        request.user.email = email.lower()
        request.user.username = username.lower()
        if image:
            request.user.profile.image = image
        # if password:
        #     request.user.password = password

        request.user.save()
        messages.info(request, 'Profile updated')
        return redirect('edit')
    else:
        return render(request, 'accounts/edit.html')
