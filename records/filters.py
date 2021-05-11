import django_filters
from django.forms import DateInput
from . import models


class AthleticsFilter(django_filters.FilterSet):
    date = django_filters.DateFilter(
        widget=DateInput(
           attrs={
                'id': 'datepicker',
                'type': 'text'
            }
        )
    )
    class Meta:
        model = models.AthleticsModel
        fields = {
                'date': ['gt', 'lt'],
                'category': ['exact'],
                'player_name': ['icontains'],
                'idnum': ['exact'],
                'result': ['exact']
        }


class BadmintonFilter(django_filters.FilterSet):
    class Meta:
        model = models.BadmintonModel
        fields = {
                'date': ['gt', 'lt'],
                'category': ['exact'],
                'winner': ['icontains']
        }


class BasketballFilter(django_filters.FilterSet):
    class Meta:
        model = models.TeamRecordModel
        fields = {
                'event_id__datetime': ['gt','lt'],
                'event_id__event_name__category': ['exact'],
                'winner__team_name__team_name': ['icontains']
        }
        # fields = '__all__'


class CarromFilter(django_filters.FilterSet):
    class Meta:
        model = models.CarromModel
        fields = {
                'date': ['gt', 'lt'],
                'category': ['exact'],
                'winner': ['icontains']
        }


class ChessFilter(django_filters.FilterSet):
    class Meta:
        model = models.ChessModel
        fields = {
                'date': ['gt', 'lt'],
                'category': ['exact'],
                'winner': ['icontains']
        }


class CricketFilter(django_filters.FilterSet):
    class Meta:
        model = models.TeamRecordModel
        fields = {
                'event_id__datetime': ['gt','lt'],
                'event_id__event_name__category': ['exact'],
                'winner__team_name__team_name': ['icontains']
        }
        # fields = '__all__'


class FootballFilter(django_filters.FilterSet):
    class Meta:
        model = models.TeamRecordModel
        fields = {
                'event_id__datetime': ['gt','lt'],
                'event_id__event_name__category': ['exact'],
                'winner__team_name__team_name': ['icontains']
        }
        # fields = '__all__'


class KabaddiFilter(django_filters.FilterSet):
    class Meta:
        model = models.TeamRecordModel
        fields = {
                'event_id__datetime': ['gt','lt'],
                'event_id__event_name__category': ['exact'],
                'winner__team_name__team_name': ['icontains']
        }
        # fields = '__all__'


class KhoKhoFilter(django_filters.FilterSet):
    class Meta:
        model = models.TeamRecordModel
        fields = {
                'event_id__datetime': ['gt','lt'],
                'event_id__event_name__category': ['exact'],
                'winner__team_name__team_name': ['icontains']
        }
        # fields = '__all__'


class PowerliftingFilter(django_filters.FilterSet):
    class Meta:
        model = models.PowerliftingModel
        fields = {
                'date': ['gt', 'lt'],
                'category': ['exact'],
                'player_name': ['icontains'],
                'result': ['icontains']
        }


class TableTennisFilter(django_filters.FilterSet):
    class Meta:
        model = models.TableTennisModel
        fields = {
                'date': ['gt', 'lt'],
                'category': ['exact'],
                'winner': ['icontains']
        }


class VolleyballFilter(django_filters.FilterSet):
    class Meta:
        model = models.TeamRecordModel
        fields = {
                'event_id__datetime': ['gt','lt'],
                'event_id__event_name__category': ['exact'],
                'winner__team_name__team_name': ['icontains']
        }
        # fields = '__all__'


# class GalleryFilter(django_filters.FilterSet):
#     class Meta:
#         model = models.GalleryModel
#         fields = {'image_name': ['icontains']
#         }