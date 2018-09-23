"""Forms for tickets"""
from django import forms
from .models import Ticket

class TicketForm(forms.ModelForm):
    """Form for creating a ticket"""
    class Meta:
        model = Ticket
        fields = ('ticket_type', 'title', 'description', 'tags', 'image')
