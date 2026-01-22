from django.urls import path
from.import views


urlpatterns=[
    path('',views.home,name="home"),
    path('home',views.front,name="front"),
    path('about', views.about,name="about"),
    path('contact', views.contact,name="contact"),
    # path('driver_reg',views.driver_reg,name="driver_reg"),
]