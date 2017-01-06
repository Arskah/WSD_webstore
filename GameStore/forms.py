from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import StoreUser
from django.contrib.auth.models import User

#Add blocking for existing usernames and emails.
#Add password check

class StoreUserCreateForm(forms.ModelForm):
        publisher = forms.BooleanField(label = "Publisher?", required = False)
        email = forms.EmailField(required=True)
        password = forms.CharField(widget = forms.PasswordInput)

        class Meta:
            model = User
            fields = ('username','email','publisher','password')

        def save(self, commit=True):
            user = super(StoreUserCreateForm, self).save(commit=False)
            user.email = self.cleaned_data["email"]
            if commit:
                user.save()
            return user
