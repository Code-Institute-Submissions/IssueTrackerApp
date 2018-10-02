"""Add models to admin panel"""
from django.contrib import admin
from vote.models import Vote
from .models import Ticket, TicketComment

admin.site.register(Ticket)
admin.site.register(TicketComment)
admin.site.register(Vote)
