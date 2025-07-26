from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.views.decorators.cache import never_cache

# Predefined credentials
PREDEFINED_USERNAME = 'Aslah'
PREDEFINED_PASSWORD = '12345'

@never_cache
def login(request):
    if request.session.get('user'):
        return redirect('home')
    response = None
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if username == PREDEFINED_USERNAME and password == PREDEFINED_PASSWORD:
            request.session['user'] = username
            return redirect('home')
        else:
            messages.error(request, 'Incorrect username or password.')
            response = render(request, 'login.html')
    else:
        response = render(request, 'login.html')
    if response:
        return response
    

@never_cache
def home(request):
    if not request.session.get('user'):
        return redirect('login')
    response = render(request, 'index.html')
    return response

@never_cache
def signout(request):
    try:
        del request.session['user']
    except KeyError:
        pass
    return redirect('login')
def register(request):
    return render(request,'register.html')