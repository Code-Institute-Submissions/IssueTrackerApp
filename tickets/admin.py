"""Add models to admin panel"""
from django.contrib import admin
from .models import Ticket

admin.site.register(Ticket)
