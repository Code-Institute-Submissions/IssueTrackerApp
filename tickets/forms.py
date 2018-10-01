"""Forms for tickets and comments"""
from django import forms
from .models import Ticket, TicketComment

class TicketForm(forms.ModelForm):
    """Form for creating a ticket"""
    class Meta:
        model = Ticket
        fields = ('ticket_type', 'title', 'description', 'tags', 'image')

class TicketCommentForm(forms.ModelForm):
    """Form for creating comments"""
    class Meta:
        model = TicketComment
        fields = ('comment', )
