from django import forms
from django.contrib.auth.models import User
from django.forms import widgets
from .models import Profile
from profiles import models


class UserForm(forms.ModelForm):
    email = forms.EmailField()
    password = forms.PasswordInput()

    class Meta:
        model = User
        fields = ['username', 'email']
        exclud = ['password',]


class ProfileForm(forms.ModelForm):
    # dob = forms.DateField(required=False)
    class Meta:
        model = models.Profile
        fields = ['image', 'phone_number', 'city', 'dob', 'gender', 'education',
                  'experience', 'language', 'tecskill', 'softskill', 'bio', 'cv', 'file' , 'face']
        widgets = {
            'image': widgets.FileInput(attrs={
                'class': 'fa fa-camera'
            }),
            'dob': widgets.DateInput(attrs={
                'type': 'date'
            }),
            'cv': widgets.FileInput(attrs={
                'class': 'cv_input'
            }),
            'file': widgets.FileInput(attrs={
                'class': 'file_input'
            })
        }
