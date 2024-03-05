from django.urls import path
from . import views
urlpatterns = [
    path('',views.Home, name='home'),
    #  login/signup/logout
 path('login/',views.handlelogin,name='handlelogin'),
 path('logout/',views.handlelogout,name='handlelogout'),
 path('signup/',views.handlesignup,name='handlesignup'),
]
