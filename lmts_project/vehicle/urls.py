from django.urls import path
from.import views

app_name='vehicle'


urlpatterns=[
    path('drivissue',views.drivissue,name="drivissue"),
    path('vehicleentry',views.vehicleentry,name="vehicleentry"),
    path('vehicle_entry',views.vehicle_entry,name="vehicle_entry"),
    path('vehicleissue',views.vehicleissue,name="vehicleissue"),
]