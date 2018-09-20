"""Views for User Auth"""
from django.shortcuts import render, redirect, reverse
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from userAuth.forms import LoginForm

def index(request):
    """Return index page"""
    return render(request, 'index.html')

def login(request):
    """Return login page"""
    if request.user.is_authenticated:
        return redirect(reverse('index'))
    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            user = auth.authenticate(username=request.POST['username'], password=request.POST['password'])
            if user:
                auth.login(user=user, request=request)
                messages.success(request, "You have successfully logged in!")
                return redirect(reverse('index'))
            else:
                login_form.add_error(None, "Your username or password is incorrect")
    else:
        login_form = LoginForm()
    return render(request, 'login.html', {'login_form': login_form})

@login_required
def logout(request):
    """Logout user"""
    auth.logout(request)
    messages.success(request, "You have successfully logged out!")
    return redirect(reverse('index'))
