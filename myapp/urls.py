# mysite/urls.py

from django.conf.urls import include, url
from django.contrib import admin
from login.views import *
from django.contrib.auth import views
urlpatterns =[
    url(r'^$', views.login, name='login'),
    url(r'^logout/$', logout_page),
    #url(r'^accounts/login/$', views.login, name='login2'), # If user is not login it will redirect to login page
    url(r'^register/$', register),
    url(r'^register/success/$', register_success),
    url(r'^home/$', home),

    url(r'^admin/', include(admin.site.urls)),
    
]