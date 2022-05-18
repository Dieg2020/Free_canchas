from django.contrib import admin
from django.urls import path,include
from app.forms import UserLoginForm
from django.contrib.auth import views as auth_views
#from django.contrib.auth.views import LoginView,LogoutView
from .views import *

urlpatterns = [
    path('',inicio, name="inicio"),

    path('login/',auth_views.LoginView.as_view(template_name='login.html', redirect_authenticated_user=True, authentication_form=UserLoginForm), name="iniciar_sesion"),
    path('logout/',auth_views.LogoutView.as_view(template_name='index.html'), name="cerrar_sesion"),
    path('register/',user_register, name="register"),
    path('password-reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),


    path('oauth/',include('social_django.urls',namespace='social')),


]

