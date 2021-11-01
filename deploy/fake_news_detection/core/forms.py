from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,UsernameField
from django.utils.translation import gettext,gettext_lazy as _
from django.contrib.auth.models import User

class LoginForm(AuthenticationForm):
    username=UsernameField(widget=forms.TextInput(attrs={'autofocus':True,'class':'form-control','placeholder':'enter username'}))
    password=forms.CharField(label=_('Password'),strip=False,widget=forms.PasswordInput(attrs={'autocomplete':'current-password','class':'form-control','placeholder':'enter password'}))

class SignUpForm(UserCreationForm):
    password1=forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'enter password'}))
    password2=forms.CharField(label='Confirm Password(again)',widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'confirm password'}))
    class Meta:
        model=User
        fields=['username','first_name','last_name','email']
        labels={'first_name':'First Name','last_name':'Last Name','email':'Email'}
        widgets={
            'username':forms.TextInput(attrs={'class':'form-control','placeholder':'enter username'}),
            'first_name':forms.TextInput(attrs={'class':'form-control','placeholder':'enter first name'}),
            'last_name':forms.TextInput(attrs={'class':'form-control','placeholder':'enter last name'}),
            'email':forms.EmailInput(attrs={'class':'form-control','placeholder':'enter email'}),
        }