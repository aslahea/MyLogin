from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages

# Predefined credentials
PREDEFINED_USERNAME = 'Aslah'
PREDEFINED_PASSWORD = '12345'

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if username == PREDEFINED_USERNAME and password == PREDEFINED_PASSWORD:
            request.session['user'] = username
            return redirect('home')
        else:
            messages.error(request, 'Incorrect username or password.')
            return render(request, 'login.html')
    else:
        return render(request, 'login.html')

def home(request):
    if not request.session.get('user'):
        # Prevent caching so back button doesn't show home after signout
        response = redirect('login')
        response['Cache-Control'] = 'no-cache, no-store, must-revalidate'
        response['Pragma'] = 'no-cache'
        response['Expires'] = '0'
        return response
    response = render(request, 'index.html')
    response['Cache-Control'] = 'no-cache, no-store, must-revalidate'
    response['Pragma'] = 'no-cache'
    response['Expires'] = '0'
    return response

def signout(request):
    try:
        del request.session['user']
    except KeyError:
        pass
    response = redirect('login')
    response['Cache-Control'] = 'no-cache, no-store, must-revalidate'
    response['Pragma'] = 'no-cache'
    response['Expires'] = '0'
    return response

def register(request):
    return render(request,'register.html')