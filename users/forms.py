from django import forms
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from .models import StoreUser

class UserForm(UserCreationForm):
    publisher = forms.BooleanField(label = "Publisher?", required = False)
    email = forms.EmailField(required=True)

    class Meta:
        model = StoreUser
        fields = ('username','first_name','last_name','email','publisher')

class editprofile_form(UserChangeForm):
    class Meta:
        model = StoreUser
        fields = ('username','first_name','last_name','email','publisher')
