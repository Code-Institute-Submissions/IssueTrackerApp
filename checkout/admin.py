"""Add models to admin panel"""
from django.contrib import admin
from .models import NewFeatureUpvote

admin.site.register(NewFeatureUpvote)
