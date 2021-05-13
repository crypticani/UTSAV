from django.contrib import admin
from . import models
# Register your models here.


class TeamRecordA(admin.ModelAdmin):
    list_display = ['record_id', 'event_id', 'get_winner']
    list_filter = ['event_id__event_name__category__category', 'event_id__year', 'winner']
    search_fields = ['event_id__team1__team_name__team_name', 'event_id__team2__team_name__team_name']

    # def get_team1(self, obj):
    #     return obj.event_id.team1
    # get_team1.admin_order_field  = 'record_id'  #Allows column order sorting
    # #get_team1.short_description = 'Team 1'  #Renames column head

    # def get_team2(self, obj):
    #     return obj.event_id.team2
    # get_team2.admin_order_field  = 'record_id'  #Allows column order sorting
    # #get_team2.short_description = 'Team 2'  #Renames column head

    def get_winner(self, obj):
        return obj.winner
    get_winner.admin_order_field  = 'record_id'  #Allows column order sorting
    #get_winner.short_description = 'Winner'  #Renames column head


class IRecord(admin.ModelAdmin):
    list_display = ['record_id', 'event_id', 'category', 'winner']
    list_filter = ['category']
    search_fields = ['winner']


class IRecord1(admin.ModelAdmin):
    list_display = ['record_id', 'event_id', 'category','player_name', 'result']
    list_filter = ['category', 'result']
    search_fields = ['player_name']


admin.site.register(models.TeamRecordModel, TeamRecordA)
admin.site.register(models.AthleticsModel, IRecord1)
admin.site.register(models.BadmintonModel, IRecord)
admin.site.register(models.CarromModel, IRecord)
admin.site.register(models.ChessModel, IRecord)
admin.site.register(models.PowerliftingModel, IRecord1)
admin.site.register(models.TableTennisModel, IRecord)
