from django.urls import path
from.import views

app_name='mechanic'


urlpatterns=[
    path('mech_reg',views.mech_reg,name="mech_reg"),
    path('mech_login',views.mech_login,name="mech_login"),
    path('regmech',views.mechdetails,name="regmech"),
    path('mechlogin',views.mechlogin,name="mechlogin"),
    path('mechlogout',views.mechlogout,name="mechlogout"),
    path('mech_dash',views.mech_dash,name="mech_dash"),
    path('mech_contact',views.mech_contact,name="mech_contact"),
    path('mech_about',views.mech_about,name="mech_about"),
    path('mechprofile',views.mechprofile,name="mechprofile"),
    path('mecheditprofile',views.mecheditprofile,name="mecheditprofile"),
    path('editmech',views.editmech,name="editmech"),
    path('mechusername',views.mechusername,name="mechusername"),
    path('mech_user',views.mech_user,name="mech_user"),
    path('mechstat',views.mechstat,name="mechstat"),
    path('mech_status',views.mech_status,name="mech_status"),
    path('mechserv',views.mechserv,name="mechserv"),
    path('ser_approve',views.ser_approve,name="ser_approve"),
    path('acpt_serv',views.acpt_serv,name="acpt_serv"),
    path('serv_rec',views.serv_rec,name="serv_rec"),
    path('serv_update',views.serv_update,name="serv_update"),
    path('mechdelete',views.mechdelete,name="mechdelete"),
]