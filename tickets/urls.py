"""Tickets URLs"""
from django.urls import path
from tickets.views import get_all_tickets, ticket_details, create_ticket

urlpatterns = [
    path('', get_all_tickets, name='tickets'),
    path('<int:pk>/', ticket_details, name='ticket_details'),
    path('new-issue/', create_ticket, name='new_issue'),
]