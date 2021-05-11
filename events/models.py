from django.db import models
from registration.models import *
from registration import models as R
import datetime

# Create your models here.

class TeamEventList(models.Model):
    id = models.IntegerField(primary_key=True)
    event_name = models.ForeignKey(Events, on_delete=models.CASCADE, limit_choices_to={'type':'T'})
    team1 = models.ForeignKey(TeamRegistrationmodel, related_name='team11', on_delete=models.CASCADE, limit_choices_to={'year': datetime.date.today().year})
    team2 = models.ForeignKey(TeamRegistrationmodel, related_name='team12', on_delete=models.CASCADE, limit_choices_to={'year': datetime.date.today().year})
    datetime = models.DateTimeField()
    venue = models.CharField(max_length=30)
    # today = datetime.today()

    class Meta:
        verbose_name_plural = "Team Event List"

    def __str__(self):
        return str('{} vs {}, {}'.format(self.team1, self.team2, self.datetime.date()))

    @property
    def is_past_event(self):
        return self.today <= self.datetime


class IndividualEventsList(models.Model):
    id = models.IntegerField(primary_key=True)
    event = models.ForeignKey(Events, on_delete=models.CASCADE, limit_choices_to={'type':'I'})
    fix = models.CharField(blank=True, max_length=100)
    # categories = (('Male', 'Male'), ('Female', 'Female'))
    # category = models.CharField(blank=True, max_length=10, choices=categories)
    category = models.ForeignKey(R.Categories, on_delete=models.SET_NULL, null=True)
    datetime = models.DateTimeField(blank=True)
    venue = models.CharField(blank=True, max_length=100)
    # today = datetime.today()

    class Meta:
        verbose_name_plural = "Individual Events"

    def __str__(self):
        return str(self.event)

    @property
    def is_past_event(self):
        return self.today <= self.datetime