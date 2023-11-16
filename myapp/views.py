from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

# Create your views here.
<<<<<<< HEAD
def index(request):
    context ={}
    return render(request,'index.html',context)

def login(request):
    context={}
    return render(request,'login.html',context)

def register(request):
    context={}
    return render(request,'register.html',context)

def shop(request):
    context={}
    return render(request,'shop.html',context)

=======
def shop(request):
    template = loader.get_template('shop.html')
    return HttpResponse(template.render())


>>>>>>> Gelo

