from django.urls import path
from . import views

urlpatterns = [
    path('shop/',views.shop,name='shop'),
    path('contact/',views.contact,name="contact"),
    path('homepage/',views.homepage,name="homepage"),
    path('login/',views.login,name="login"),
    path('reigster/',views.register,name="register"),
    path('service/',views.service,name="service"),
    path('about/',views.about,name="about"),
    path('news/',views.news,name="news"),
    path('shop/details/<int:id>', views.details, name='details'),
]