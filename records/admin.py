from django.contrib import admin
from . import models
# Register your models here.


class TeamRecordA(admin.ModelAdmin):
    list_display = ['event_id', 'get_winner']
    list_filter = ['event_id__event_name__category__category', 'winner']

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


admin.site.register(models.TeamRecordModel, TeamRecordA)
admin.site.register(models.AthleticsModel)
admin.site.register(models.BadmintonModel)
admin.site.register(models.CarromModel)
admin.site.register(models.ChessModel)
admin.site.register(models.PowerliftingModel)
admin.site.register(models.TableTennisModel)