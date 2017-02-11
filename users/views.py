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

        data = {
        'username': profile.username ,
        'email': profile.email ,
        'first_name': profile.first_name ,
        'last_name': profile.email ,
        'publisher': profile.publisher,
        }

        edit_profile_form = editprofile_form(request.POST or None, instance=profile, initial = data)

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



# if request.POST["next"] is Not "":
#     HttpResponseRedirect(request.POST["next"])
# else:
#     HttpResponseRedirect(settings.LOGIN_REDIRECT_URL)

# @require_http_methods(["GET", "POST"])
# def login_view(request, *args, **kwargs):
#     if request.method == "POST":
#         uname = request.POST.get("username", None)
#         pw = request.POST.get("passwd", None)
#         user = authenticate(username=uname, password=pw)
#         if user is not None:
#             login(request, user)
#             original_site = request.GET.get("next",None) or "/"
#             return redirect(original_site)
#         return render(request, "login.html", {"error":"kirjautuminen kosahti. koita uudelleen"})
#     # user got here by a get request
#     user = request.user
#     if user.is_authenticated():
#         return redirect("/") # user shoud not be here authenticated with get but get rid if is
#     return render(request, "login.html", {})

# @require_http_methods(["POST"])
# def logout_view(request, *args, **kwargs):
#     logout(request)
#     return redirect("/")
