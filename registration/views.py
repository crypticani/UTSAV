from django.shortcuts import render
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, request
from django.template.loader import render_to_string
from UTSAV import settings
from .models import *
from main.models import Courses

# Create your views here.

def Registeration(requests):
    data1 = PermanentTeam.objects.all()
    # data2 = IndividualRegistration.objects.all()
    # data3 = Categories.objects.all()
    data4 = Events.objects.filter(type='I')
    data5 = Courses.objects.all()
    rules = Rules.objects.all()
    context = {
                'data1' : data1,
                # 'data2' : data2,
                # 'data3' : data3,
                'data4' : data4,
                'data5' : data5,
                'rules' : rules
            }
    return render(requests, 'registeration.html', context)


def IndRegisteration(request):
    if request.method == 'POST':
        idnum = request.POST.get('idnum')
        # year = request.POST.get('year')
        name = request.POST.get('name')
        # category = request.POST.get('category')
        event = request.POST.get('event')
        course = request.POST.get('course')
        mobile = request.POST.get('mobile')
        email = request.POST.get('email')
        
        count = IndividualRegistration.objects.filter(idnum=idnum).count()
        # print(count)
        if(IndividualRegistration.objects.filter(idnum=idnum, event=event)):
            return HttpResponse("Error!<br>Player already registered.")
        elif(count > 2):
            return HttpResponse("Error!<br>You have reached the maximum limit of registration.")
        else:
            # event = Events.objects.filter(tevent_id=event)
            indreg = IndividualRegistration(idnum=idnum, name=name, event_id=event, course=course,
                                                mobile=mobile, email=email)
            indreg.save()
            subject = "Registered Successfully"
            message = "Hi " + request.POST.get('name') + ", You have been successfully registered for "+ request.POST.get('event') +". Check Your Profile for more details."
            try:
                send_mail(subject, message, settings.EMAIL_HOST_USER, [email], fail_silently=False, )
                return HttpResponseRedirect('/accounts/profile')
            except:
                return HttpResponse("Error! <br>Mail could not be sent.")
    return render(request, 'registeration.html')


def TeamRegisteration(request):
    if request.method == 'POST':
        team_id = request.POST.get('team_id')
        player_name = request.POST.get('player_name')
        id_number = request.POST.get('id_number')
        email = request.POST.get('email')

        count = TeamPlayers.objects.filter(idnum=idnum).count()
        if(TeamPlayers.objects.filter(id_number=id_number, team_id=team_id)):
            return HttpResponse("Error!<br>Player already registered.")
        elif(count > 2):
            return HttpResponse("Error!<br>You have reached the maximum limit of registration.")
        else:
            teamreg = TeamPlayers(team_id_id=team_id, player_name=player_name, id_number=id_number)
            teamreg.save()
            subject = "Registered Successfully"
            message = "Hi " + request.POST.get('player_name') + ".<br> You have been successfully registered for "+ request.POST.get('team_id') + ". Contact your team captain to make your status active."
            try:
                send_mail(subject, message, settings.EMAIL_HOST_USER, [email], fail_silently=False, )
                return HttpResponseRedirect('/accounts/profile')
            except:
                return HttpResponse("Error! <br>Mail could not be sent.")
    return render(request, 'registeration.html')


