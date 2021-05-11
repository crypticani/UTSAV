from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, request
from . import models, filters

# Create your views here.
def Records(request):
    return render(request, 'records.html')


def Athletics(request):
    data = models.AthleticsModel.objects.order_by('event_id')
    myFilter = filters.AthleticsFilter(request.GET, queryset=data)
    data = myFilter.qs
    eventdata = {'myFilter': myFilter,
                 'record': data}
    return render(request, 'records/athletics.html', eventdata)


def Badminton(request):
    data = models.BadmintonModel.objects.order_by('event_id')
    myFilter = filters.BadmintonFilter(request.GET, queryset=data)
    data = myFilter.qs
    eventdata = {'myFilter': myFilter,
                 'record': data}
    return render(request, 'records/badminton.html', eventdata)


def Basketball(request):
    data = models.TeamRecordModel.objects.filter(event_id__event_name__events='Basketball')
    myFilter = filters.BasketballFilter(request.GET, queryset=data)
    data = myFilter.qs
    table = 'Basketball'
    eventdata = {'myFilter': myFilter,
                 'record': data,
                 'table': table}
    return render(request, 'records/teamrecords.html', eventdata)


def Carrom(request):
    data = models.CarromModel.objects.order_by('event_id')
    myFilter = filters.CarromFilter(request.GET, queryset=data)
    data = myFilter.qs
    eventdata = {'myFilter': myFilter,
                 'record': data}
    return render(request, 'records/carrom.html', eventdata)


def Chess(request):
    data = models.ChessModel.objects.order_by('event_id')
    myFilter = filters.ChessFilter(request.GET, queryset=data)
    data = myFilter.qs
    eventdata = {'myFilter': myFilter,
                 'record': data}
    return render(request, 'records/chess.html', eventdata)


def Cricket(request):
    data = models.TeamRecordModel.objects.filter(event_id__event_name__events='Cricket')
    myFilter = filters.CricketFilter(request.GET, queryset=data)
    data = myFilter.qs
    table = 'Cricket'
    eventdata = {'myFilter': myFilter,
                 'record': data,
                 'table': table}
    return render(request, 'records/teamrecords.html', eventdata)


def Football(request):
    data = models.TeamRecordModel.objects.filter(event_id__event_name__events='Basketball')
    myFilter = filters.FootballFilter(request.GET, queryset=data)
    data = myFilter.qs
    table = 'Football'
    eventdata = {'myFilter': myFilter,
                 'record': data,
                 'table': table}
    return render(request, 'records/teamrecords.html', eventdata)


def Kabaddi(request):
    data = models.TeamRecordModel.objects.filter(event_id__event_name__events='Basketball')
    myFilter = filters.KabaddiFilter(request.GET, queryset=data)
    data = myFilter.qs
    table = 'Kabaddi'
    eventdata = {'myFilter': myFilter,
                 'record': data,
                 'table': table}
    return render(request, 'records/teamrecords.html', eventdata)


def KhoKho(request):
    data = models.TeamRecordModel.objects.filter(event_id__event_name__events='Basketball')
    myFilter = filters.KhoKhoFilter(request.GET, queryset=data)
    data = myFilter.qs
    table = 'KhoKho'
    eventdata = {'myFilter': myFilter,
                 'record': data,
                 'table': table}
    return render(request, 'records/teamrecords.html', eventdata)

def Powerlifting(request):
    data = models.PowerliftingModel.objects.order_by('event_id')
    myFilter = filters.PowerliftingFilter(request.GET, queryset=data)
    data = myFilter.qs
    eventdata = {'myFilter': myFilter,
                 'record': data}
    return render(request, 'records/powerlifting.html', eventdata)


def TableTennis(request):
    data = models.TableTennisModel.objects.order_by('event_id')
    myFilter = filters.TableTennisFilter(request.GET, queryset=data)
    data = myFilter.qs
    eventdata = {'myFilter': myFilter,
                 'record': data}
    return render(request, 'records/tabletennis.html', eventdata)


def Volleyball(request):
    data = models.TeamRecordModel.objects.filter(event_id__event_name__events='Basketball')
    myFilter = filters.VolleyballFilter(request.GET, queryset=data)
    data = myFilter.qs
    table = 'Volleyball'
    eventdata = {'myFilter': myFilter,
                 'record': data,
                 'table': table}
    return render(request, 'records/teamrecords.html', eventdata)
