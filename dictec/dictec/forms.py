from django.forms import ModelForm
from .models import Dictamenfinal
from django.forms import *

class DictamenForm(ModelForm):
    class Meta:
        model = Dictamenfinal 
        fields = ['Titulo', 'IDuser', 'Nombre', 'Oficina', 'Direccion', 'Tipo_Equipo', 'Marca', 'Modelo', 'Num_Serie', 'Caracteristicas', 'Problema', 'Analisis',  'Proceso_Realizado', 'Dictamen_Final']
        labels = {'Titulo': 'Titulo del Dictamen', 'IDuser':'ID Congreso', 'Nombre':'Nombre Completo', 'Oficina':'Oficina o Ubicación', 'Direccion':'Dirección', 'Tipo_Equipo':'Tipo de equipo', 'Marca':'Marca del equipo', 'Modelo':'Modelo del equipo', 'Num_Serie':'Numero de serie del equipo','Caracteristicas': 'Caracteristicas','Problema': 'Problema o Falla','Analisis': 'Análisis'}
        
        widgets = {'Titulo': TextInput( attrs={'class': 'form-control', 'placeholder': 'Ingrese un titulo para identificar el dictamen', 'autocomplete': 'off'}), 'IDuser': TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese su ID del Congreso', 'autocomplete': 'off'}), 'Nombre': TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese su nombre completo', 'autocomplete': 'off'}), 'Oficina': TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese nombre de la oficina o ubicación', 'autocomplete': 'off'}), 'Direccion': TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese dirección de la oficina o ubicación', 'autocomplete': 'off'}), 'Caracteristicas': TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese Caracteristicas del Equipo', 'autocomplete': 'off'}), 'Tipo_Equipo': TextInput(attrs={'class': 'form-control', 'placeholder': 'Ejemplo: Laptop, PC, Tablet, Impresora, etc.', 'autocomplete': 'off'}), 'Marca': TextInput(attrs={'class': 'form-control', 'placeholder': 'Ejemplo: Lenovo, Dell, Php, Samsumg, etc.', 'autocomplete': 'off'}), 'Modelo': TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese modelo del equipo segun el fabricante.', 'autocomplete': 'off'}), 'Num_Serie': TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese numero de serie del equipo', 'autocomplete': 'off'}), 'Problema': Textarea(attrs={'class': 'form-control', 'placeholder': 'Describa el problema o falla del equipo', 'autocomplete': 'off'}), 'Analisis': Textarea(attrs={'class': 'form-control', 'placeholder': 'Ingrese el analisis segun su criterio de por que se presenta el problema o falla en el equipo', 'autocomplete': 'off'}), 'Proceso_Realizado': Textarea(attrs={'class': 'form-control', 'placeholder': 'Detalle el aproceso realizado para realizar su analisis', 'autocomplete': 'off'}), 'Dictamen_Final': Textarea(attrs={'class': 'form-control', 'placeholder': 'Dictamine cual es la solución o recomendacion para el problema o falla en el equipo', 'autocomplete': 'off'})}


class DictameneditForm(ModelForm):
    class Meta:
        model = Dictamenfinal 
        fields = ['Titulo', 'IDuser', 'Nombre', 'Oficina', 'Direccion', 'Tipo_Equipo', 'Marca', 'Modelo', 'Num_Serie', 'Caracteristicas', 'Problema', 'Analisis', 'Proceso_Realizado', 'Dictamen_Final']

class DictameneditadminForm(ModelForm):
    class Meta:
        model = Dictamenfinal 
        fields = [ 'Comentario','Imprimir']
        labels = {'Comentario': 'Mensaje ', 'Imprimir': 'Click en la casilla para enviar a Dictamenes En Proceso'}
        widgets = {'Comentario': TextInput( attrs={'class': 'form-control', 'placeholder': 'Escriba un mensaje para el tecnico', 'autocomplete': 'off'}),'Imprimir': CheckboxInput( attrs={'class': 'form-check-input','autocomplete': 'off'})}

class DictameneditjefeForm(ModelForm):
    class Meta:
        model = Dictamenfinal 
        fields = [ 'Comentariojefe', 'Revisionjefe', 'Pendiente']
        labels = {'Comentariojefe': 'Mensaje', 'Revisionjefe': 'Estado de la Revision', 'Pendiente': 'Click en la casilla para enviar a Dictamenes Pendinetes'}
        widgets = {'Comentariojefe': TextInput( attrs={'class': 'form-control', 'placeholder': 'Escriba un mensaje para el tecnico', 'autocomplete': 'off'}),'Revisionjefe': Select( attrs={'class': 'form-control', 'placeholder': 'Seleccion Estado de la Revision', 'autocomplete': 'off'}), 'Pendiente': CheckboxInput( attrs={'class': 'form-check-input', 'placeholder': 'Seleccion Estado de la Revision','autocomplete': 'off'})}

class Dictameneditjefe2Form(ModelForm):
    class Meta:
        model = Dictamenfinal 
        fields = [ 'Comentariojefe', 'Revisionjefe', 'Pendiente']

class RespaldoForm(ModelForm):
    class Meta:
        model = Dictamenfinal 
        fields = ['imagen']
        labels = { 'imagen':'Archivo que Raspalda la entrega al usuario'}
        widgets = {'imagen': ClearableFileInput(attrs={'class': 'form-control'})}

class RevisionForm(ModelForm):
    class Meta:
        model = Dictamenfinal 
        fields = ['Titulo', 'IDuser', 'Nombre', 'Oficina', 'Direccion', 'Tipo_Equipo', 'Marca', 'Modelo', 'Num_Serie', 'Caracteristicas', 'Problema', 'Analisis', 'Proceso_Realizado', 'Dictamen_Final', 'Revision']
        labels = {'Titulo': 'Titulo del Dictamen', 'IDuser':'ID Congreso', 'Nombre':'Nombre Completo', 'Oficina':'Oficina o Ubicación', 'Direccion':'Dirección', 'Tipo_Equipo':'Tipo de equipo', 'Marca':'Marca del equipo', 'Modelo':'Modelo del equipo', 'Num_Serie':'Numero de serie del equipo','Caracteristicas': 'Caracteristicas','Problema': 'Problema o Falla','Analisis': 'Análisis','Revision': 'Estado'}
        
        widgets = {'Titulo': TextInput( attrs={'class': 'form-control', 'placeholder': 'Ingrese un titulo para identificar el dictamen', 'autocomplete': 'off'}), 'IDuser': TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese su ID del Congreso', 'autocomplete': 'off'}), 'Nombre': TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese su nombre completo', 'autocomplete': 'off'}), 'Oficina': TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese nombre de la oficina o ubicación', 'autocomplete': 'off'}), 'Direccion': TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese dirección de la oficina o ubicación', 'autocomplete': 'off'}), 'Caracteristicas': TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese Caracteristicas del Equipo', 'autocomplete': 'off'}), 'Tipo_Equipo': TextInput(attrs={'class': 'form-control', 'placeholder': 'Ejemplo: Laptop, PC, Tablet, Impresora, etc.', 'autocomplete': 'off'}), 'Marca': TextInput(attrs={'class': 'form-control', 'placeholder': 'Ejemplo: Lenovo, Dell, Php, Samsumg, etc.', 'autocomplete': 'off'}), 'Modelo': TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese modelo del equipo segun el fabricante.', 'autocomplete': 'off'}), 'Num_Serie': TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese numero de serie del equipo', 'autocomplete': 'off'}), 'Problema': Textarea(attrs={'class': 'form-control', 'placeholder': 'Describa el problema o falla del equipo', 'autocomplete': 'off'}), 'Analisis': Textarea(attrs={'class': 'form-control', 'placeholder': 'Ingrese el analisis segun su criterio de por que se presenta el problema o falla en el equipo', 'autocomplete': 'off'}), 'Proceso_Realizado': Textarea(attrs={'class': 'form-control', 'placeholder': 'Detalle el aproceso realizado para realizar su analisis', 'autocomplete': 'off'}), 'Dictamen_Final': Textarea(attrs={'class': 'form-control', 'placeholder': 'Dictamine cual es la solución o recomendacion para el problema o falla en el equipo', 'autocomplete': 'off'}), 'Revision': Select(attrs={'class': 'form-control', 'placeholder': 'Dictamine', 'autocomplete': 'off'})}
        
