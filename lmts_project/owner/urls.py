from django.urls import path
from.import views

app_name='owner'

urlpatterns=[
    path('admin_login',views.admin_login,name="admin_login"),
    path('admlogin',views.admlogin,name="admlogin"),
    path('adlogout',views.adlogout,name="adlogout"),
    path('owner_dash',views.owner_dash,name="owner_dash"),
    path('own_contact',views.own_contact,name="own_contact"),
    path('own_about',views.own_about,name="own_about"),
    path('driv_owner_dash',views.driv_owner_dash,name="driv_owner_dash"),
    path('mech_owner_dash',views.mech_owner_dash,name="mech_owner_dash"),
    path('user_owner_dash',views.user_owner_dash,name="user_owner_dash"),
    path('driv_info',views.driv_info,name="driv_info"),
    path('driv_approve',views.driv_approve,name="driv_approve"),
    path('driv_deny',views.driv_deny,name="driv_deny"),
    path('driv_apvd',views.driv_apvd,name="driv_apvd"),
    path('stat_driver',views.stat_driver,name="stat_driver"),
    path('statviewdriv',views.statviewdriv,name="statviewdriv"),
    path('driv_work',views.driv_work,name="driv_work"),
    path('viewvehicle',views.viewvehicle,name="viewvehicle"),
    path('mech_info',views.mech_info,name="mech_info"),
    path('mech_approve',views.mech_approve,name="mech_approve"),
    path('mech_deny',views.mech_deny,name="mech_deny"),
    path('mech_apvd',views.mech_apvd,name="mech_apvd"),
    path('stat_mech',views.stat_mech,name="stat_mech"),
    path('statviewmech',views.statviewmech,name="statviewmech"),
    path('serviceapproval',views.serviceapproval,name="serviceapproval"),
    path('userinfo',views.userinfo,name="userinfo"),
    path('orderapproval',views.orderapproval,name="orderapproval"),
    path('order_approve',views.order_approve,name="order_approve"),
    path('order_apvd',views.order_apvd,name="order_apvd"),
    path('order_deny',views.order_deny,name="order_deny"),
    path('denyed_order',views.denyed_order,name="denyed_order"),
    path('maintenance',views.maintenance,name="maintenance"),
    path('histmain',views.histmain,name="histmain"),
]
