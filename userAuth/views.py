"""Views for User Auth"""
from django.shortcuts import render, redirect, reverse

def login(request):
    """Return login page"""
    return render(request, 'login.html')

def logout(request):
    """Logout user"""
    return redirect(reverse('index.html'))
