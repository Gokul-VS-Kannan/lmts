from django.urls import path
from.import views

app_name='driver'


urlpatterns=[
    path('driver_reg',views.driver_reg,name="driver_reg"),
    path('regdriv',views.drivdetails,name="regdriv"),
    path('driver_login',views.driver_login,name="driver_login"),
    path('drivlogin',views.drivlogin,name="drivlogin"),
    path('drivlogout',views.drivlogout,name="drivlogout"),
    path('driver_dash',views.driver_dash,name="driver_dash"),
    path('driv_contact',views.driv_contact,name="driv_contact"),
    path('driv_about',views.driv_about,name="driv_about"),
    path('driv_contact',views.driv_contact,name="driv_contact"),
    path('driv_about',views.driv_about,name="driv_about"),
    path('drivprofile',views.drivprofile,name="drivprofile"),
    path('driveditprofile',views.driveditprofile,name="driveditprofile"),
    path('editdriv',views.editdriv,name="editdriv"),
    path('drivusername',views.drivusername,name="drivusername"),
    path('driv_user',views.driv_user,name="driv_user"),
    path('drivstat',views.drivstat,name="drivstat"),
    path('driv_status',views.driv_status,name="driv_status"),
    path('drivdelete',views.drivdelete,name="drivedelete"),
    path('drivvehicle',views.drivvehicle,name="drivvehicle"),
    path('vehicle_selection',views.vehicle_selection,name="vehicle_selection"),
    path('vehicle_details',views.vehicle_details,name="vehicle_details"),
]