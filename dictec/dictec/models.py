from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Dictamen(models.Model):
  Titulo = models.CharField(max_length=200)
  IDuser = models.CharField(max_length=20)
  Nombre = models.CharField(max_length=80)
  Oficina = models.CharField(max_length=80)
  Direccion = models.CharField(max_length=80)  
  Marca = models.CharField(max_length=80)
  Modelo = models.CharField(max_length=80)
  Num_Serie = models.CharField(max_length=80)
  Caracteristicas = models.CharField(max_length=200)
  Comentario = models.CharField(max_length=300)
  Analisis = models.TextField(max_length=1000)
  Dictamen_Final = models.TextField(max_length=1000)
  Creacion = models.DateTimeField(auto_now_add=True)
  Datecompleted = models.DateTimeField(null=True, blank=True)
  Pendiente = models.BooleanField(default=False)
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  
  def __str__(self):
    return self.Titulo + ' - ' + self.user.username
status_Revision = [
  ('Corregido','Corregido'),
  ('Corregido 2','Corregido 2'),
  ('Corregido 3','Corregido 3'),
  ('Modifcado','Modificado')
]
status_Revisionjefe = [
  ('Pendiente','Pendiente'),
  ('Pendiente 2','Pendiente 2'),
  ('Pendiente 3','Pendiente 3'),
  ('Aprobado','Aprobado')
]
  
class Dictamenfinal(models.Model):
  Titulo = models.CharField(max_length=200)
  IDuser = models.CharField(max_length=20)
  Nombre = models.CharField(max_length=80)
  Oficina = models.CharField(max_length=80)
  Direccion = models.CharField(max_length=80) 
  Tipo_Equipo = models.CharField(max_length=80) 
  Marca = models.CharField(max_length=80)
  Modelo = models.CharField(max_length=80)
  Revision = models.CharField(max_length=80, null=False, blank=True,choices=status_Revision)
  Revisionjefe = models.CharField(max_length=80, null=False, blank=True,choices=status_Revisionjefe)
  Num_Serie = models.CharField(max_length=80)
  Caracteristicas = models.CharField(max_length=200)
  Comentario = models.CharField(max_length=300, blank=True)
  Comentariojefe = models.CharField(max_length=300, blank=True)
  Problema = models.TextField(max_length=1000)  
  Analisis = models.TextField(max_length=1000)
  Proceso_Realizado = models.TextField(max_length=1000)
  Dictamen_Final = models.TextField(max_length=1000)
  Creacion = models.DateTimeField('%Y/%m/%d', auto_now_add=True)
  Datecompleted = models.DateTimeField(null=True, blank=True)
  Pendiente = models.BooleanField(default=False)
  Imprimir = models.BooleanField(default=False)
  Creado = models.BooleanField(default=True)
  imagen = models.ImageField(upload_to='media', null=True, blank=True)
  Finalizado = models.BooleanField(default=False)
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  
  def __str__(self):
    return self.Titulo + ' - ' + self.user.username

