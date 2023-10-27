from django.forms import ModelForm
from .models import Dictamenfinal

class DictamenForm(ModelForm):
    class Meta:
        model = Dictamenfinal 
        fields = ['Titulo', 'IDuser', 'Nombre', 'Oficina', 'Direccion', 'Tipo_Equipo', 'Marca', 'Modelo', 'Num_Serie', 'Caracteristicas', 'Problema', 'Analisis', 'Proceso_Realizado', 'Dictamen_Final', 'Creado', 'Pendiente', 'Imprimir', 'Finalizado']