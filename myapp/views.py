from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect 
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *
from .forms import RegistrationForm, LoginForm
from django.contrib.auth import authenticate, login as auth_login
from .models import Customer

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

def service(request):
    template = loader.get_template('service.html')
    return HttpResponse(template.render())

def news(request):
    template = loader.get_template('news.html')
    return HttpResponse(template.render())

def details(request, id):
    motorbike = Motorbike.objects.get(id=id)
    template = loader.get_template('details.html')
    context = {
        'motorbike': motorbike,
    }
    return HttpResponse(template.render(context, request))

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth_login(request, user)
                return redirect('homepage')
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form': form})

def login(request):  
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth_login(request, user)
                return redirect('homepage')
    else:
        form = LoginForm()
    return render(request,'login.html',{'form' : form })
