from django.urls import path
from.import views

app_name = 'user'

urlpatterns=[
    path('user_reg',views.user_reg,name="user_reg"),
    path('user_login',views.user_login,name="user_login"),
    path('reguser',views.reguser,name="reguser"),
    path('userlogin',views.userlogin,name="userlogin"),
    path('userlogout',views.userlogout,name="userlogout"),
    path('usercon',views.usercon,name="usercon"),
    path('userabt',views.userabt,name="userabt"),
    path('user_dash',views.user_dash,name="user_dash"),
    path('viewprofile',views.viewprofile,name="viewprofile"),
    path('editprofile',views.editprofile,name="editprofile"),
    path('edituser',views.edituser,name="edituser"),
    path('placeorder',views.placeorder,name="placeorder"),
    path('orderplacing',views.orderplacing,name="orderplacing"),
    path('orderstatus',views.orderstatus,name="orderstatus"),
    path('orderhistory',views.orderhistory,name="orderhistory"),
    path('editusername',views.editusername,name="editusername"),
    path('editlogin',views.editlogin,name="editlogin"),
    path('userdelete',views.userdelete,name="userdelete"),
]