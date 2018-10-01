"""Model for tickets and comments"""
from django.db import models

class Ticket(models.Model):
    """Model to create a ticket"""
    STATUS_CHOICES = (
        ('TODO', 'To do'),
        ('DOING', 'In process'),
        ('DONE', 'Done')
    )
    TYPE_CHOICES = (
        ('BUG', 'Bug'),
        ('NEW FEATURE', 'New feature')
    )
    author = models.CharField(max_length=150, default='')
    ticket_type = models.CharField(choices=TYPE_CHOICES, default='BUG', max_length=11)
    created_date = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=False)
    description = models.TextField(blank=False)
    tags = models.CharField(max_length=30, blank=True, null=True)
    image = models.ImageField(upload_to='images', blank=True, null=True)
    status = models.CharField(choices=STATUS_CHOICES, default='TODO', max_length=10)
    upvotes = models.IntegerField(default=0)

    def __str__(self):
        return self.title

class TicketComment(models.Model):
    """Model to create comments"""
    author = models.CharField(max_length=150, default='')
    comment = models.TextField(blank=False)
    comment_date = models.DateTimeField(auto_now_add=True)
    ticket = models.ForeignKey(Ticket, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.author
