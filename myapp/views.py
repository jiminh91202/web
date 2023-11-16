from django.shortcuts import render

# Create your views here.
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


