from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import StoreUser
from django.contrib.auth.models import User

class StoreUserCreateForm(forms.ModelForm):

        publisher = forms.BooleanField(label = "Publisher?", required = False)
        email = forms.EmailField(required=True)
        password = forms.CharField(widget = forms.PasswordInput)
        password2 = forms.CharField(widget = forms.PasswordInput)

        class Meta:
            model = User
            fields = ('username','email','publisher','password','password2')

        def clean_password2(self):
            pass1 = self.cleaned_data["password"]
            pass2 = self.cleaned_data["password2"]
            if pass1 != pass2:
                raise forms.ValidationError("Passwords dont match!")
            return pass1

        def clean_email(self):
            email_qs = User.objects.filter(email = self.cleaned_data["email"])
            if email_qs.exists():
                raise forms.ValidationError("There already is a user with this email.")
            return self.cleaned_data["email"]


        def save(self, commit=True):
            newUser = super(StoreUserCreateForm, self).save(commit=False)
            newUser.email = self.cleaned_data["email"]
            if commit:
                newUser.save()
                newStoreUser = StoreUser.objects.create(user = newUser, publisher = self.cleaned_data["publisher"],)
                newStoreUser.save()

            return newUser
