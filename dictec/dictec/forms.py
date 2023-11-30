from django.forms import ModelForm
from .models import Dictamenfinal

class DictamenForm(ModelForm):
    class Meta:
        model = Dictamenfinal 
        fields = ['Titulo', 'IDuser', 'Nombre', 'Oficina', 'Direccion', 'Tipo_Equipo', 'Marca', 'Modelo', 'Num_Serie', 'Caracteristicas', 'Problema', 'Analisis', 'Proceso_Realizado', 'Dictamen_Final']

class DictameneditForm(ModelForm):
    class Meta:
        model = Dictamenfinal 
        fields = ['Titulo', 'IDuser', 'Nombre', 'Oficina', 'Direccion', 'Tipo_Equipo', 'Marca', 'Modelo', 'Num_Serie', 'Caracteristicas', 'Problema', 'Analisis', 'Proceso_Realizado', 'Dictamen_Final']

class DictameneditadminForm(ModelForm):
    class Meta:
        model = Dictamenfinal 
        fields = [ 'Comentario', 'Creado', 'Imprimir','Revision']

class DictameneditjefeForm(ModelForm):
    class Meta:
        model = Dictamenfinal 
        fields = [ 'Pendiente']

class RespaldoForm(ModelForm):
    class Meta:
        model = Dictamenfinal 
        fields = ['imagen']

class RevisionForm(ModelForm):
    class Meta:
        model = Dictamenfinal 
        fields = ['Titulo', 'IDuser', 'Nombre', 'Oficina', 'Direccion', 'Tipo_Equipo', 'Marca', 'Modelo', 'Num_Serie', 'Caracteristicas', 'Problema', 'Analisis', 'Proceso_Realizado', 'Dictamen_Final', 'Revision']