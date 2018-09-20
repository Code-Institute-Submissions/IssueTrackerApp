"""User Auth URLs"""
from django.urls import path, include
from userAuth.views import login, logout, index, registration
from userAuth import urls_reset

urlpatterns = [
    path('', index, name='index'),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    path('register/', registration, name='register'),
    path('password-reset/', include(urls_reset)),
]
