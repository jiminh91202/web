from django.urls import path
from . import views
from django.contrib.auth import views as auth_views




urlpatterns = [    
    path('',views.homepage,name="homepage"),
    path('shop/',views.shop,name='shop'),
    path('contact/',views.contact,name="contact"),
    path('login/',views.login,name="login"),
    path('reigster/',views.register,name="register"),
    path('service/',views.service,name="service"),
    path('about/',views.about,name="about"),
    path('news/',views.news,name="news"),
    path('shop/details/<int:id>', views.details, name='details'),

]

