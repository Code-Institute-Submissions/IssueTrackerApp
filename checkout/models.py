"""Model for checkout"""
from django.db import models
from tickets.models import Ticket

class NewFeatureUpvote(models.Model):
    """Model for new feature requests"""
    username = models.CharField(max_length=50, blank=False)
    new_feature = models.ForeignKey(Ticket, on_delete=models.CASCADE, null=False)
    amount = models.IntegerField(blank=False)
    date = models.DateField(null=True)

    def __str__(self):
        return '{0} - {1} @ {2} - {3}'.format(self.date, self.username, self.amount, self.new_feature.title)
