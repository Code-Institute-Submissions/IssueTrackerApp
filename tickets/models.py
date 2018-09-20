"""Model for tickets"""
from django.db import models

class Ticket(models.Model):
    """Model to create a ticket"""
    STATUS_CHOICES = (
        ('TODO', "To do"),
        ('DOING', "In process"),
        ('DONE', "Done")
    )
    name = models.CharField(max_length=100, blank=False)
    description = models.TextField(blank=False)
    image = models.ImageField(upload_to='images', blank=True)
    status = models.CharField(choices=STATUS_CHOICES, default='TODO', max_length=10)

    def __str__(self):
        return self.name
