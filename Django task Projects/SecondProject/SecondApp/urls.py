from django.urls import path
from .import views

urlpatterns = [
    path('',views.SignUp,name='signup'),
    path('login/',views.Login,name='login'),
    path('homepage/',views.HomePage,name='home'),
    path('logout/',views.Logout,name='logout'),
] 