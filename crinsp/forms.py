from django.contrib.auth.forms import AuthenticationForm
from django.contrib.admin import widgets
from django import forms
from django.forms import ModelForm
from . models import *
from bootstrap_datepicker_plus import DatePickerInput
from django.forms.models import inlineformset_factory 

class LoginForm (AuthenticationForm):
    Emp_num = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    Password= forms.CharField(widget =forms.PasswordInput(attrs={'class':'form-control'}))


    








        