from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.views.decorators.http import require_http_methods
from forms import StoreUserCreateForm
#from models import User

@require_http_methods(["GET"])
def main_index(request, *args, **kwargs):
    return redirect("http://google.fi/")

@require_http_methods(["GET","POST"])
def  register_view(request, *args, **kwargs):
    form = StoreUserCreateForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("http://google.fi/")
    context = {
        "form" : form
    }
    return render(request, "registration/registrationForm.html", context)


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
