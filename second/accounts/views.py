from django.shortcuts import render, redirect

from django.contrib.auth.models import User
from django.contrib import auth, messages

# Create your views here.
def signup(request):
    if request.method == 'POST':
        if request.POST['password'] == request.POST['password_check']:
            user = User.objects.create_user(username=request.POST['username'], password=request.POST['password'])
            auth.login(request, user)
            return redirect('home')
    return render(request, 'signup.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            messages.add_message(request, messages.SUCCESS, 'Successfully logged in!')
            return redirect('home')
        else:
            messages.add_message(request, messages.ERROR, 'Login Failed')
            return render(request, 'login.html', {'error': 'Username or password is incorrect'})
    else:
        return render(request, 'login.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.add_message(request, messages.INFO, 'You just logged out!')
        return redirect('home')
    return render(request, 'login.html')