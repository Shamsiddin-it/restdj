from django.urls import path
from .views import *

urlpatterns = [
    path("",home,name = "home"),
    path("home/",home,name = "home"),
    path("reglog",reglog,name = "reglog"),
]
