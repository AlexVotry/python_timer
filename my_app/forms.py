from django import forms
from .models import TimeTracker

class JobForm(forms.ModelForm):
    class Meta:
        model = TimeTracker
        fields = ['job', 'location']

class LoginForm(forms.Form):
    username = forms.CharField(label='User Name', max_length= 70)
    password = forms.CharField(widget = forms.PasswordInput())

    
