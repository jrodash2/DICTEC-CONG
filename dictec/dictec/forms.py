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
        fields = [ 'Comentario', 'Creado', 'Imprimir','Pendiente']

class DictameneditjefeForm(ModelForm):
    class Meta:
        model = Dictamenfinal 
        fields = [ 'Creado', 'Comentariojefe', 'Revisionjefe', 'Pendiente']

class Dictameneditjefe2Form(ModelForm):
    class Meta:
        model = Dictamenfinal 
        fields = [ 'Comentariojefe', 'Revisionjefe']

class RespaldoForm(ModelForm):
    class Meta:
        model = Dictamenfinal 
        fields = ['imagen']

class RevisionForm(ModelForm):
    class Meta:
        model = Dictamenfinal 
        fields = ['Titulo', 'IDuser', 'Nombre', 'Oficina', 'Direccion', 'Tipo_Equipo', 'Marca', 'Modelo', 'Num_Serie', 'Caracteristicas', 'Problema', 'Analisis', 'Proceso_Realizado', 'Dictamen_Final', 'Revision']