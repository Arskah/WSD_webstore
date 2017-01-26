from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import StoreUser

class StoreUserCreationForm(UserCreationForm):
    publisher = forms.BooleanField(label = "Publisher?", required = False)
    email = forms.EmailField(required=True)
    
    class Meta:
        model = StoreUser
        fields = ('username','publisher')