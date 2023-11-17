from django.template import loader
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import *
# Create your views here.
def shop(request):
    brands = Brand.objects.all()
    context = {'brands': brands}
    return render(request, 'shop.html', context)

def about(request):
    template = loader.get_template('about.html')
    return HttpResponse(template.render())

def contact(request):
    template = loader.get_template('contact.html')
    return HttpResponse(template.render())

def homepage(request):
    template = loader.get_template('homepage.html')
    return HttpResponse(template.render())

def login(request):
    template = loader.get_template('login.html')
    return HttpResponse(template.render())

def register(request):
    template = loader.get_template('register.html')
    return HttpResponse(template.render())

def service(request):
    template = loader.get_template('service.html')
    return HttpResponse(template.render())

def news(request):
    template = loader.get_template('news.html')
    return HttpResponse(template.render())

def members(request):
  mymembers = Motorbike.objects.all().values()
  template = loader.get_template('all_members.html')
  context = {
    'motor': mymembers,
  }
  return HttpResponse(template.render(context, request))
  
def details(request, id):
  mymember = Motorbike.objects.get(ID=id)
  template = loader.get_template('details.html')
  context = {
    'motor': mymember,
  }
  return HttpResponse(template.render(context, request))