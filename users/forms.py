from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import StoreUser

class UserForm(UserCreationForm):
    publisher = forms.BooleanField(label = "Publisher?", required = False)
    email = forms.EmailField(required=True)

    class Meta:
        model = StoreUser
        fields = ('username','first_name','last_name','email','publisher')
