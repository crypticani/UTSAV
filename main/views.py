from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, request
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.utils.encoding import force_text, force_bytes
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.contrib.auth.models import User
from django.contrib.sites.shortcuts import get_current_site
from UTSAV import settings
from .forms import SignUpForm
from . import models, filters
from .models import Notice as notices
from .models import ImageGallery as gallery
from .tokens import account_activation_token
from django.template.loader import render_to_string
from registration.models import *
from django.shortcuts import render, get_object_or_404, redirect
from django import forms


def Home(request):
    data = notices.objects.filter(is_active=True)
    context = {
        'data': data
    }
    return render(request, 'index.html', context)


def activation_sent_view(request):
    return render(request, 'activation_sent.html')


def activate(request, uidb64, token, account_activation_token=None):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    # checking if the user exists, if the token is valid.
    if user is not None and account_activation_token.check_token(user, token):
        # if valid set active true 
        user.is_active = True
        # set signup_confirmation true
        user.profile.signup_confirmation = True
        user.save()
        login(request, user)
        return redirect('home')
    else:
        return render(request, 'accounts/activation_invalid.html')


def activation_invalid_view(request):
    return render(request, 'accounts/activation_invalid.html')


def signup_view(request):
    if request.method  == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            user.profile.first_name = form.cleaned_data.get('first_name')
            user.profile.last_name = form.cleaned_data.get('last_name')
            user.profile.gender = form.cleaned_data.get('gender')
            user.profile.email = form.cleaned_data.get('email')
            user.profile.course_id = form.cleaned_data.get('course')
            user.profile.mobile = form.cleaned_data.get('mobile')
            # user can't login until link confirmed
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            subject = 'Please Activate Your Account'
            # load a template like get_template()
            # and calls its render() method immediately.
            message = render_to_string('activation_request.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                # method will generate a hash value with user related data
                'token': account_activation_token.make_token(user),
            })
            print(message)
            try:
                send_mail(subject, message, settings.EMAIL_HOST_USER, [user.profile.email], fail_silently=False,)
                return redirect('activation_sent')
            except:
                return HttpResponse("Error! <br>Mail could not be sent.")
    else:
        form = SignUpForm()
    return render(request, 'user/register.html', {'form': form})


################ login forms###################################################
def Login(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            fm = AuthenticationForm(request=request, data = User.objects.filter(user=request.user))
            if fm.is_valid():
                uname = fm.cleaned_data['username']
                upass = fm.cleaned_data['password']
                user = authenticate(username=uname, password=upass)
                if user is not None:
                    login(request, user)
                    messages.success(request, 'Logged in successfully!!!')
                    return HttpResponseRedirect('/profile/')
                else:
                    raise forms.ValidationError('Invalid Credentials')
        else:
            fm = AuthenticationForm()
        return render(request, 'user/login.html', {'form': fm})
    else:
        return HttpResponseRedirect('/login/')


def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(id=uid)
    except (TypeError, ValueError, OverflowError):
        user = None
    # checking if the user exists, if the token is valid.
    if user is not None and account_activation_token.check_token(user, token):
        # if valid set active true
        user.is_active = True
        # set signup_confirmation true
        user.profile.signup_confirmation = True
        user.save()
        return HttpResponseRedirect('user/login')
    else:
        return render(request, 'accounts/activation_invalid.html')


# Edit Profile View
def Profile(request):
    if request.user.is_authenticated:
        data1 = IndividualRegistration.objects.order_by('year')
        return render(request, 'accounts/profile.html', {'name': request.user, "revent_info": data1})
    else:
        return HttpResponseRedirect('/login/')

def Logout(request):
    logout(request)
    messages.success(request, "Logged out successfully!")
    return HttpResponseRedirect('/')

def user_logout(request):
    return render(request, 'user/logout.html')

def nav(requests):
    return render(requests, 'nav.html')

def Records(request):
    return render(request, 'records.html')


def Gallery(request):
    Images = gallery.objects.all()
    myFilter = filters.GalleryFilter(request.GET, queryset=Images)
    Images = myFilter.qs
    context = {'myFilter': myFilter,
                'Images': Images}
    return render(request, 'gallery.html', context)


def Contact(requests):
    return render(requests, 'contact.html')

def Feedback(requests):
    return render(requests, 'feedback.html')

def error_404_view(request,exception):
    return render(request,'404.html')

def Display(request):
    email = request.user.email
    allTeams = PermanentTeam.objects.filter(email=email)
    choice = 0
    players = TeamPlayers.objects.filter(team_id__id=choice)
    context = {
        'allTeams' : allTeams,
        'data' : players,
    }
    if request.method == "POST":
        if 'choiceButton' in request.POST:
            choice = request.POST.get('choice')
            request.session['choice'] = choice
            players = TeamPlayers.objects.filter(team_id__id=choice)
            context = {
                'allTeams' : allTeams,
                'data' : players,
                'mychoice': choice,
            }
            return render(request, 'display.html', context)
        if 'active' in request.POST:
            pl_id = request.POST.get('active')
            choice = request.session['choice']
            obj = get_object_or_404(TeamPlayers ,player_id=pl_id)
            if obj.is_active == True:
                TeamPlayers.objects.filter(player_id=pl_id).update(is_active=False)
                messages.info(request, "Removed!")
            elif obj.is_active == False:
                TeamPlayers.objects.filter(player_id=pl_id).update(is_active=True)
                messages.info(request, "Added!")
            players = TeamPlayers.objects.filter(team_id__id=choice)
            context = {
                'data' : players,
                'allTeams' : allTeams,
                'mychoice': choice,
            }
            return render(request, 'display.html', context)
    return render(request, 'display.html', context)


def Prediction(request):
    t1 = get_object_or_404(PermanentTeam, id=180005)
    t2 = get_object_or_404(PermanentTeam, id=240105)
    ct1 = TeamRecordModel.objects.filter(winner__team_name=t1)
    ct2 = TeamRecordModel.objects.filter(winner__team_name=t2)
    a1 = ct1.count()
    a2 = ct2.count()
    print(ct1)
    total = a1 + a2
    if total > 1:
        p1 = round(a1/total*100)
        p2 = round(a2/total*100)
        return HttpResponse("Winning Chances of<br>"+ str(t1) + " is "+ str(p1) + "%  <br>"+ str(t2) + " is "+ str(p2) + "%.")
    else:
        return HttpResponse("Not Enough Data to Predict")

# def RecordView(request):
#     data = TeamRecordModel.objects.all()
#     context = {
#                 'data' : data,
#             }
#     return render(request, 'test.html', context)
