from django.contrib import admin
from django.urls import path,include
from shopApp.views import *


urlpatterns = [
    path('get_persons/', get_persons)

] 