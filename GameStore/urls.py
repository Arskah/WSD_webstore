"""GameStore URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from .views import main_index
from .views import register_view
from .views import inventory_view
#from GameStore.views import login_view
#from GameStore.views import logout_view
#from views import api

urlpatterns = [
  url(r'^$', main_index),
  url(r'^admin/', admin.site.urls),
  url(r'^login/$', auth_views.login, name='login'),
  url(r'^logout/$', auth_views.logout, {'next_page': '/'}, name='logout'),
  url(r'^registration/$', register_view, name='registration'),
  url(r'^inventory/$', inventory_view, name='inventory'),
  #url(r'^login$', login_view),
  #url(r'^logout$', logout_view),
  #url(r'^api', api),
]
