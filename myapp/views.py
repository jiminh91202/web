from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect 
from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *
from django.urls import reverse
from django.utils import timezone

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
    motorbike = Motorbike.objects.get(ID=id)
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

def search(request):
    query = request.GET.get('q')
    if query:
        brands = Brand.objects.filter(name__icontains=query)
        motorbikes = Motorbike.objects.filter(brand__in=brands)
    else:
        motorbikes = Motorbike.objects.all()
    return render(request, 'search_results.html', {'motorbikes': motorbikes})

def order_motorbike(request, motorbike_id):
    motorbike = get_object_or_404(Motorbike, pk=motorbike_id)
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        user, created = User.objects.get_or_create(username=name)
        customer, created = Customer.objects.get_or_create(user=user, phone=phone)
        Order.objects.create(customer=customer, motorbike=motorbike, order_date=timezone.now())
        return redirect('order_success')
    return render(request, 'order.html', {'motorbike': motorbike})