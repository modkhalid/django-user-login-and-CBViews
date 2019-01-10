from django.contrib.auth.models import User
from myapp.models import UserProfile
from django import forms

class UserBasicForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model=User
        fields=['username','password','email']

class UserProfileForm(forms.ModelForm):
    class Meta():
        model=UserProfile
        fields=['portfolio','profile_pic']
