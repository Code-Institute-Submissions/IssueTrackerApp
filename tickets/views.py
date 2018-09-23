"""Views for tickets"""
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Ticket
from .forms import TicketForm

def get_all_tickets(request):
    """Render list of all tickets"""
    # Sort results by created date, descending order
    results = Ticket.objects.all().order_by('-created_date')
    return render(request, 'tickets.html', {'tickets': results})

def ticket_details(request, pk):
    """Render page with ticket details based on ID"""
    ticket = get_object_or_404(Ticket, pk=pk)
    return render(request, 'ticket_details.html', {'ticket': ticket})

@login_required
def create_ticket(request, pk=None):
    """Create a view with form to submit ticket"""
    ticket = get_object_or_404(request, pk=None) if pk else None
    if request.method == 'POST':
        form = TicketForm(request.POST, request.FILES, instance=ticket)
        if form.is_valid():
            ticket = form.save(commit=False)
            ticket.author = request.user.username
            ticket.save()
            return redirect(ticket_details, ticket.pk)
    else:
        form = TicketForm(instance=ticket)
    return render(request, 'ticket_new.html', {'ticket_form': form})
