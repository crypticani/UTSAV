"""UTSAV URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from events.views import Events as Ev
from records.views import *
from registration.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('events', Ev, name='events'),
    path('records', Records, name='records'),
    path('records/athletics', Athletics, name='athletics'),
    path('records/badminton', Badminton, name='badminton'),
    path('records/basketball', Basketball, name='basketball'),
    path('records/carrom', Carrom, name='carrom'),
    path('records/chess', Chess, name='chess'),
    path('records/cricket', Cricket, name='cricket'),
    path('records/football', Football, name='football'),
    path('records/kabaddi', Kabaddi, name='kabaddi'),
    path('records/khokho', KhoKho, name='khokho'),
    path('records/powerlifting', Powerlifting, name='powerlifting'),
    path('records/table-tennis', TableTennis, name='table-tennis'),
    path('records/volleyball', Volleyball, name='volleyball'),
    path('registeration', Registeration, name='registeration'),
    path('IndRegister', IndRegisteration, name='IndRegister'),
    path('TeamRegister', TeamRegisteration, name='TeamRegister'),
]

handler404 = 'main.views.error_404_view'