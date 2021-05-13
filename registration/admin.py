from django.contrib import admin
from . import models

# Register your models here.

class PermanentTeamsI(admin.TabularInline):
    model = models.PermanentTeam


class IndRegister(admin.ModelAdmin):
    list_display = ('idnum', 'year', 'name', 'course', 'event')
    list_filter = ('event', 'course', 'year', 'event__category')

class TeamRegister(admin.ModelAdmin):
    list_display = ('year', 'team_name', 'event_name')
    list_filter = ('event_name', 'team_name', 'year', 'category')


class TeamRegistrationA(admin.ModelAdmin):
    list_display = ['reg_id', 'year', 'category', 'get_event_name', 'get_team_name', 'get_captain_name']

    def get_team_name(self, obj):
        return obj.team_name.team_name
    get_team_name.admin_order_field  = 'reg_id'  #Allows column order sorting
    #get_team_name.short_description = 'Team Name'  #Renames column head

    def get_event_name(self, obj):
        return obj.team_name.event_name
    get_event_name.admin_order_field  = 'reg_id'  #Allows column order sorting
    #get_event_name.short_description = 'Event Name'  #Renames column head

    def get_captain_name(self, obj):
        return obj.team_name.captain
    get_event_name.admin_order_field  = 'reg_id'  #Allows column order sorting
    #get_event_name.short_description = 'Captain'  #Renames column head
 
    list_filter = ['year', 'category', 'team_name__event_name']
    search_fields = ['team_name__team_name', 'team_name__captain']


class TeamPlayersI(admin.TabularInline):
    model = models.TeamPlayers
    extra = 0


class PermanentTeamA(admin.ModelAdmin):
    list_display = ['id', 'event_name', 'team_name', 'captain']
    list_filter = ['event_name__category__category', 'event_name']
    search_fields = ['team_name', 'captain', 'vice_captain']
    inlines = [TeamPlayersI]


class TeamPlayersA(admin.ModelAdmin):
    list_display = ['get_team_name', 'get_event_name', 'player_name', 'id_number', 'is_active']

    def get_team_name(self, obj):
        return obj.team_id.team_name
    get_team_name.admin_order_field  = 'team_id'  #Allows column order sorting
    #get_team_name.short_description = 'Team Name'  #Renames column head

    def get_event_name(self, obj):
        return obj.team_id.event_name
    get_event_name.admin_order_field  = 'team_id'  #Allows column order sorting
    #get_event_name.short_description = 'Event Name'  #Renames column head

    def get_category(self, obj):
        return obj.team_id.id.category
    get_event_name.admin_order_field  = 'team_id'  #Allows column order sorting
    #get_event_name.short_description = 'Category'  #Renames column head

    list_filter = ['team_id__event_name__category__category', 'team_id__event_name', 'team_id__team_name', 'is_active']
    search_fields = ['player_name', 'id_number']


class EventsA(admin.ModelAdmin):
    list_display = ['events', 'category', 'type', 'active']
    list_filter = ['category', 'type', 'active']
    search_fields = ['events']


class RulesA(admin.ModelAdmin):
    list_display = ['rule', 'is_active']
    list_filter = ['is_active']
    search_fields = ['rule']

admin.site.register(models.IndividualRegistration, IndRegister)
admin.site.register(models.TeamRegistrationmodel, TeamRegistrationA)
# admin.site.register(models.TeamEventList, TeamEventsListA)

admin.site.register(models.PermanentTeam, PermanentTeamA)
admin.site.register(models.TeamPlayers, TeamPlayersA)
admin.site.register(models.Categories)
admin.site.register(models.Events, EventsA)
admin.site.register(models.Rules, RulesA)