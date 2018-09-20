"""User Auth URLs"""
from django.urls import path
from userAuth.views import login, logout, index

urlpatterns = [
    path('', index, name='index'),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
]
