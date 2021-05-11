from django.shortcuts import render
from . import models
import datetime

# Create your views here.
def Events(request):
    ind_past = models.IndividualEventsList.objects.filter(datetime__lte = datetime.date.today())[:10:1]
    ind_upcoming = models.IndividualEventsList.objects.filter(datetime__gte = datetime.date.today())
    team_past = models.TeamEventList.objects.filter(datetime__lte = datetime.date.today())[:10:1]
    team_upcoming = models.TeamEventList.objects.filter(datetime__gte = datetime.date.today())
    
    EventData = {"ind_past": ind_past,
                 "ind_upcoming": ind_upcoming,   
                 "team_past": team_past,
                 "team_upcoming":team_upcoming,
    }
    return render(request, 'events.html', EventData)
