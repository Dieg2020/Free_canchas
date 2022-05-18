from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django import forms
from django.utils import timezone
from .models import RolUsuario1,User
from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV2Invisible

class UserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)

    username = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control', 
            'placeholder': 'Ingrese su Usuario', 
            'id': 'username'
        }))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Contraseña',
            'id': 'password',
        }))
    captcha = ReCaptchaField()

class RegisterForm(UserCreationForm):
    username = forms.CharField(label='Nombre de usuario', widget=forms.TextInput(
        attrs={
            'class': 'form-control', 
            'placeholder': 'Nombre de usuario', 
            'id': 'username'
        }))
    email = forms.EmailField(label='Email', widget=forms.TextInput(
        attrs={
            'class': 'form-control', 
            'placeholder': 'Email', 
            'id': 'username'
        }))
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Contraseña',
            'id': 'password',
        }))
    password2 = forms.CharField(label='Confirme su contraseña', widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Confirme su contraseña',
            'id': 'password',
        }))

    DireccionUsuario = forms.CharField(label='Direccion', widget=forms.TextInput(
        attrs={
            'class': 'form-control', 
            'placeholder': 'Direccion', 
            'id': 'direccion'
        }))
    firstname = forms.CharField(label='Nombre', widget=forms.TextInput(
        attrs={
            'class': 'form-control', 
            'placeholder': 'Nombre', 
            'id': 'nombre'
        }))
    lastname = forms.CharField(label='Apellido', widget=forms.TextInput(
        attrs={
            'class': 'form-control', 
            'placeholder': 'Apellido', 
            'id': 'apellido'
        }))

    Query = RolUsuario1.objects.get(DescipcionRol = 'Cliente')
    IdRol = Query[0].id
    

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
