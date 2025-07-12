from django.contrib import admin
from django.urls import path, include
from SURPISEQUIZ_NI_SER.views import *
from project.views import *

urlpatterns = [

    path('home/', home, name='home'),

    path('about/', about, name='about'),

    path('project/', include('project.urls)),'))
]