from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *
from registration.models import Categories


class SignUpForm(UserCreationForm):
    username = forms.IntegerField
    first_name = forms.CharField(max_length=100, help_text='Last Name')
    last_name = forms.CharField(max_length=100, help_text='Last Name')
    genders = (
        ('Male', 'Male'),
        ('Female', 'Female')
    )
    gender = forms.ChoiceField(choices=genders)
    email = forms.EmailField(max_length=150, help_text='Email')
    mobile = forms.CharField(max_length=10, help_text='Mobile Number')
    course = forms.ModelChoiceField(queryset=Courses.objects.all())

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'gender', 'email', 'mobile', 'course', 'password1', 'password2')

