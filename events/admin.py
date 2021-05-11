from django.contrib import admin
from . import models
from registration.admin import PermanentTeamsI

# Register your models here.

# class TeamEventsA(admin.ModelAdmin):
#     list_display = ['tevent_id', 'events', 'active']
#     inlines = [PermanentTeamsI]

class TeamEventsListA(admin.ModelAdmin):
    list_filter = ['event_name__events', 'event_name__category__category']
    list_display = ['id', 'team1', 'team2', 'datetime', 'venue']

    def get_team1(self, obj):
        return obj.team1

    def get_team2(self, obj):
        return obj.team2


class Event(admin.ModelAdmin):
    list_display = ('event', 'fix', 'datetime')
    list_filter = ('event', 'datetime', 'category')


admin.site.register(models.TeamEventList, TeamEventsListA)
admin.site.register(models.IndividualEventsList, Event)