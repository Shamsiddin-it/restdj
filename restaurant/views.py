from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from .models import User
# Create your views here.
def home(request):
    template = loader.get_template("home.html")
    return HttpResponse(template.render())
def reglog(request):
    template = loader.get_template("reglog.html")
    return HttpResponse(template.render())

def tables(request):
    users = User.objects.prefetch_related('orders').all()
    return render(request, 'tables.html', {"users": users})
