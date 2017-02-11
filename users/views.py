from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods
from .forms import UserForm,editprofile_form
from django.contrib.auth.forms import SetPasswordForm
from .models import StoreUser

@require_http_methods(["GET","POST"])
def register_view(request, *args, **kwargs):
    form = UserForm(request.POST or None)
    if form.is_valid():
        form.save()
#       Login the user after registration...
#       login(form.cleaned_data["storeuser")
        return redirect("/")
    context = {
        "form" : form
    }
    return render(request, "registration/registrationForm.html", context)

@require_http_methods(["GET","POST"])
def  editprofile_view(request, *args, **kwargs):
        profile = request.user
        edit_profile_form = editprofile_form(request.POST or None, instance= request.user)

        if request.method == 'POST':
            if edit_profile_form.is_valid():
                edit_profile_form.save()
                return redirect('profile')

        context = {'form': editprofile_form}
        return render(request, "profile/editprofile.html", context)

def  change_password(request, *args, **kwargs):
        profile = request.user
        changepassword_form = SetPasswordForm(request.POST or None)

        if request.method == 'POST':
            if changepassword_form.is_valid():
                changepassword_form.save()
                return redirect('profile')

        context = {'form': changepassword_form}
        return render(request, "profile/changepassword.html", context)



@require_http_methods(["GET"])
def profile_view(request, *args, **kwargs):
    if(request.user.is_authenticated):
        context = {
        'storeuser' : request.user
        }
    else:
        return redirect('/login/?next=' + request.path)

    return render(request, "profile/userprofile.html", context)
