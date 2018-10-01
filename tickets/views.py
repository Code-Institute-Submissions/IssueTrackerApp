"""Views for tickets"""
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Ticket, TicketComment
from .forms import TicketForm, TicketCommentForm

def get_all_tickets(request):
    """Render list of all tickets"""
    # Sort results by created date, descending order
    results = Ticket.objects.all().order_by('-created_date')
    return render(request, 'tickets.html', {'tickets': results})

def ticket_details(request, pk):
    """Render page with ticket details based on ID"""
    ticket = get_object_or_404(Ticket, pk=pk)
    # Display comments
    comments = ticket.ticketcomment_set.all().order_by('comment_date')

    # Form for adding a comment
    if request.method == 'POST':
        comment_form = TicketCommentForm(request.POST, request.FILES)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user.username
            comment.ticket = ticket
            comment.save()
            # comment_form = TicketCommentForm()
            return redirect(ticket_details, pk=ticket.pk)
    else:
        comment_form = TicketCommentForm()
    return render(request, 'ticket_details.html', {'ticket': ticket, 'comments': comments, 'comment_form': comment_form})

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
