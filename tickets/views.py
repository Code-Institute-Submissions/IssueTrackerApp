"""Views for tickets"""
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
#from vote.models import Vote
from .models import Ticket
from .forms import TicketForm, TicketCommentForm

def get_all_tickets(request):
    """Render list of all tickets"""
    # Sort results by created date, descending order
    results = Ticket.objects.all().order_by('-created_date')
    # Get votes
    for ticket in results:
        votes = ticket.votes.count()
        ticket.votes = votes
    return render(request, 'tickets.html', {'tickets': results})

def ticket_details(request, pk):
    """Render page with ticket details based on ID"""
    ticket = get_object_or_404(Ticket, pk=pk)
    # Display comments
    comments = ticket.ticketcomment_set.all().order_by('comment_date')
    # Display votes
    votes = ticket.votes.count()
    # Form for adding a comment
    if request.method == 'POST' and request.POST.get('submit'):
        comment_form = TicketCommentForm(request.POST, request.FILES)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user.username
            comment.ticket = ticket
            comment.save()
            return redirect(ticket_details, pk=ticket.pk)
    # Form for upvoting tickets
    elif request.method == 'POST' and not request.POST.get('submit'):
        comment_form = TicketCommentForm()
        if request.user.is_authenticated:
            if ticket.ticket_type == 'BUG':
                if ticket.votes.exists(user_id=request.user.pk):
                    messages.error(request, "You already upvoted this ticket")
                else:
                    ticket.votes.up(user_id=request.user.pk)
                return redirect(ticket_details, pk=ticket.pk)
            elif ticket.ticket_type == 'NEW FEATURE':
                return redirect(upvote_new_feature, pk=ticket.pk)
        else:
            messages.error(request, "You must be logged in to upvote tickets")
    else:
        comment_form = TicketCommentForm()
    return render(request, 'ticket_details.html', {'ticket': ticket, 'votes': votes, 'comments': comments, 'comment_form': comment_form})

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

def upvote_new_feature(request, pk):
    """Create a view with form to set amount to pay"""
    ticket = get_object_or_404(Ticket, pk=pk)
    return render(request, 'ticket_upvote_new_feature.html', {'ticket': ticket})

def statistics(request):
    """Show statistics for tickets"""
    bugs_todo = len(Ticket.objects.all().filter(ticket_type='BUG', status='TODO'))
    bugs_doing = len(Ticket.objects.all().filter(ticket_type='BUG', status='DOING'))
    bugs_done = len(Ticket.objects.all().filter(ticket_type='BUG', status='DONE'))
    feat_todo = len(Ticket.objects.all().filter(ticket_type='NEW FEATURE', status='TODO'))
    feat_doing = len(Ticket.objects.all().filter(ticket_type='NEW FEATURE', status='DOING'))
    feat_done = len(Ticket.objects.all().filter(ticket_type='NEW FEATURE', status='DONE'))
    # Top voted bug currently working on
    bugs = Ticket.objects.all().filter(ticket_type='BUG', status='DOING')
    bug_votes = []
    for bug in bugs:
        num_votes = bug.votes.count()
        bug_votes.append((bug, num_votes))
    top_bug = max(bug_votes, key=lambda item: item[1])[0]
    # Highest paid feature currently working on
    feats = Ticket.objects.all().filter(ticket_type='NEW FEATURE', status='DOING')
    feat_paid = []
    for feat in feats:
        feat_paid.append((feat, feat.payments))
    top_feat = max(feat_paid, key=lambda item: item[1])[0]
    return render(request, 'statistics.html', {'top_bug': top_bug, 'top_feat': top_feat, 'bugs_todo': bugs_todo, 'bugs_doing': bugs_doing, 'bugs_done': bugs_done, 'feat_todo': feat_todo, 'feat_doing': feat_doing, 'feat_done': feat_done})
