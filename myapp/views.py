from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect 
from django.shortcuts import render, redirect
from .models import *
from .forms import RegistrationForm


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


def details(request, id):
    motorbike = Motorbike.objects.get(ID=id)
    template = loader.get_template('details.html')
    context = {
        'motorbike': motorbike,
    }
    return HttpResponse(template.render(context, request))

def register(request):
    form = RegistrationForm()
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    return render(request, 'register.html', {'form': form})