"""Cart URLs"""
from django.urls import path
from .views import view_cart, add_to_cart, adjust_amount

urlpatterns = [
    path('', view_cart, name='view_cart'),
    path('add/<int:id>', add_to_cart, name='add_to_cart'),
    path('<int:id>', adjust_amount, name='adjust_amount'),
]
