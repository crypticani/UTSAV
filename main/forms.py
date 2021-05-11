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
    # courses = (
    #     ('BCA', 'BCA'),
    #     ('BSc. IT', 'BSc. IT'),
    #     ('BBA', 'BBA'),
    #     ('BSc', 'BSc'),
    #     ('BA', 'BA'),
    #     ('BAJMC', 'BAJMC'),
    #     ('MCA', 'MCA'),
    #     ('MBA', 'MBA'),
    #     ('Masters', 'Masters'),
    #     ('BRS', 'BRS'),
    #     ('Animation', 'Animation'),
    #     ('Certificate', 'Certificate')
    # )
    course = forms.ModelChoiceField(queryset=Courses.objects.all())

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'gender', 'email', 'mobile', 'course', 'password1', 'password2')


# class IndRegisterform(forms.ModelForm):
#     idnum = forms.IntegerField()
#     year = forms.IntegerField()
#     name = forms.CharField(max_length=100)
#     categories = (('Male', 'Male'), ('Female', 'Female'))
#     category = forms.ChoiceField(choices=categories)
#     event = forms.CharField(max_length=100)
#     course = forms.CharField(max_length=100)
#     mobile = forms.CharField(max_length=10)
#     email = forms.EmailField()

#     class Meta:
#         model = IndividualRegistration
#         fields = ('idnum', 'year', 'name', 'category', 'event', 'course', 'mobile', 'email')
