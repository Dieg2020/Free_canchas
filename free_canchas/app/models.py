from django.db import models
from django.contrib.auth.models import User




class RolUsuario1(models.Model):
    DescipcionRol = models.CharField(max_length=100)
  

class Usuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    DireccionUsuario = models.CharField(max_length=250)
    FechaRegistroUsuario = models.DateTimeField()
    IdRol = models.ForeignKey(RolUsuario1,null=True,blank=True,on_delete=models.CASCADE)
    