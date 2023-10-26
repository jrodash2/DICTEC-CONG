from django.forms import ModelForm
from .models import Dictamen

class DictamenForm(ModelForm):
    class Meta:
        model = Dictamen 
        fields = ['Titulo', 'IDuser', 'Nombre', 'Oficina', 'Direccion', 'Marca', 'Modelo', 'Num_Serie', 'Caracteristicas', 'Analisis', 'Dictamen_Final', 'Pendiente']