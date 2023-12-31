from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User, Group, GroupManager
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from .forms import DictamenForm
from .forms import DictameneditForm
from .forms import DictameneditadminForm
from .forms import DictameneditjefeForm
from .forms import Dictameneditjefe2Form
from .forms import RevisionForm
from .forms import RespaldoForm
from .models import Dictamen, Dictamenfinal
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.hashers import make_password
from django. contrib import messages
from datetime import datetime

# Create your views here.



def signup(request):

    if request.method == 'GET':
        return render(request, 'signup.html', {
            'form': UserCreationForm
        })
    else:
        if request.POST['password1'] == request.POST['password2']:
            # register user
            try:
                user = User.objects.create_user(
                    username=request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('dashboard')
            except IntegrityError:
                return render(request, 'signup.html', {
                    'form': UserCreationForm,
                    "error": 'El usuario ya existe'
                })

        return render(request, 'signup.html', {
            'form': UserCreationForm,
            "error": 'Password no coninciden'
        })


def home(request):
    return render(request, 'home.html')

def dictamen(request):
    dictamens = Dictamenfinal.objects.filter(user=request.user, Datecompleted__isnull=True).order_by("-Creacion")
    return render(request, 'dictamen.html', {'dictamens': dictamens})

def dictamenadmin(request):
    dictamens = Dictamenfinal.objects.filter(Datecompleted__isnull=True).order_by("-Creacion")
    return render(request, 'dictamenadmin.html', {'dictamens': dictamens})

def dictamenjefe(request):
    dictamens = Dictamenfinal.objects.filter(Datecompleted__isnull=True).order_by("-Creacion")
    return render(request, 'dictamenjefe.html', {'dictamens': dictamens})

def dictamen_creado(request):
    dictamens = Dictamenfinal.objects.filter(user=request.user, Datecompleted__isnull=True,Creado__isnull=False).exclude(Pendiente=True).order_by("-Creacion")
   
    return render(request, 'dictamen_creado.html', {'dictamens': dictamens})

def dictamen_creadoadmin(request):
    dictamens = Dictamenfinal.objects.filter(Datecompleted__isnull=True, Creado__isnull=False).exclude(Pendiente=True).order_by("-Creacion")
    return render(request, 'dictamen_creadoadmin.html', {'dictamens': dictamens})

def dictamen_creadojefe(request):
    dictamens = Dictamenfinal.objects.filter(Datecompleted__isnull=True, Creado__isnull=False).exclude(Pendiente=True).order_by("-Creacion")
    return render(request, 'dictamen_creadojefe.html', {'dictamens': dictamens})

def dictamen_pendiente(request):
    dictamens = Dictamenfinal.objects.filter(user=request.user, Datecompleted__isnull=True).exclude(Imprimir=True).order_by("-Creacion")
    return render(request, 'dictamen_pendiente.html', {'dictamens': dictamens})

def dictamen_pendienteadmin(request):
    dictamens = Dictamenfinal.objects.filter(Datecompleted__isnull=True).exclude(Imprimir=True).order_by("-Creacion")
    return render(request, 'dictamen_pendienteadmin.html', {'dictamens': dictamens})

def dictamen_pendientejefe(request):
    dictamens = Dictamenfinal.objects.filter(Datecompleted__isnull=True).exclude(Imprimir=True).order_by("-Creacion")
    return render(request, 'dictamen_pendientejefe.html', {'dictamens': dictamens})

def dictamen_imprimir(request):
    dictamens = Dictamenfinal.objects.filter(user=request.user, Datecompleted__isnull=True, Imprimir__isnull=False).order_by("-Creacion")
    return render(request, 'dictamen_imprimir.html', {'dictamens': dictamens})

def dictamen_imprimiradmin(request):
    dictamens = Dictamenfinal.objects.filter(Datecompleted__isnull=True, Imprimir__isnull=False).order_by("-Creacion")
    return render(request, 'dictamen_imprimiradmin.html', {'dictamens': dictamens})

def dictamen_imprimirjefe(request):
    dictamens = Dictamenfinal.objects.filter(Datecompleted__isnull=True, Imprimir__isnull=False).order_by("-Creacion")
    return render(request, 'dictamen_imprimirjefe.html', {'dictamens': dictamens})

def dictamen_finalizado(request):
    dictamens = Dictamenfinal.objects.filter(user=request.user, Datecompleted__isnull=False).order_by("-Creacion")
    return render(request, 'dictamen_finalizado.html', {'dictamens': dictamens})

def dictamen_finalizadoadmin(request):
    dictamens = Dictamenfinal.objects.filter(Datecompleted__isnull=False, Finalizado__isnull=False).order_by("-Creacion")
    return render(request, 'dictamen_finalizadoadmin.html', {'dictamens': dictamens})

def dictamen_finalizadojefe(request):
    dictamens = Dictamenfinal.objects.filter(Datecompleted__isnull=False, Finalizado__isnull=False).order_by("-Creacion")
    return render(request, 'dictamen_finalizadojefe.html', {'dictamens': dictamens})


def dicdetalle(request, dic_id):
    if request.method == 'GET':
        dictamen = get_object_or_404(Dictamenfinal, pk=dic_id)
        form = DictamenForm(instance=dictamen)
        return render(request, 'dicdetalle.html', {'dictamen': dictamen, 'form': form})   
    else:
        dictamen = get_object_or_404(Dictamenfinal, pk=dic_id)
        form = DictamenForm(request.POST, instance=dictamen)
        form.save()
        return redirect('dictamen')

def dicdetalleuser(request, dic_id):
    if request.method == 'GET':
        dictamen = get_object_or_404(Dictamenfinal, pk=dic_id)
        form = DictamenForm(instance=dictamen)
        return render(request, 'dicdetalleuser.html', {'dictamen': dictamen, 'form': form})   
    else:
        dictamen = get_object_or_404(Dictamenfinal, pk=dic_id)
        form = DictamenForm(request.POST, instance=dictamen)
        form.save()
        return redirect('dictamen')

def dicdetalleadmin(request, dic_id):
    if request.method == 'GET':
        dictamen = get_object_or_404(Dictamenfinal, pk=dic_id)
        form = DictamenForm(instance=dictamen)
        form = DictameneditadminForm(instance=dictamen)
        return render(request, 'dicdetalleadmin.html', {'dictamen': dictamen, 'form': form})   
    elif request.method == 'POST':
        dictamen = get_object_or_404(Dictamenfinal, pk=dic_id)
        form = DictameneditadminForm(request.POST, instance=dictamen)
        form.save()
        return redirect('dictamenadmin')
        return render(request, 'dicdetalleadmin.html', {'dictamen': dictamen, 'form': form, 'error': "Error actualiando Dictamen"})
    else:
        dictamen = get_object_or_404(Dictamenfinal, pk=dic_id)
        form = DictamenForm(request.POST, instance=dictamen)
        form.save()   
        return redirect('dictamenadmin')

def dicdetallejefe(request, dic_id):
    if request.method == 'GET':
        dictamen = get_object_or_404(Dictamenfinal, pk=dic_id)
        form = DictamenForm(instance=dictamen)
        form = DictameneditjefeForm(instance=dictamen)
        return render(request, 'dicdetallejefe.html', {'dictamen': dictamen, 'form': form})   
    elif request.method == 'POST':
        dictamen = get_object_or_404(Dictamenfinal, pk=dic_id)
        form = DictameneditjefeForm(request.POST, instance=dictamen)
        form.save()
        return redirect('dictamenjefe')
        return render(request, 'dicdetallejefe.html', {'dictamen': dictamen, 'form': form, 'error': "Error actualiando Dictamen"})
    else:
        dictamen = get_object_or_404(Dictamenfinal, pk=dic_id)
        form = DictamenForm(request.POST, instance=dictamen)
        form.save()
        return redirect('dictamenjefe')
    
def complete_dic(request, dic_id):
     dictamen = get_object_or_404(Dictamenfinal, pk=dic_id)
     if request.method == 'POST':
         dictamen.Datecompleted = timezone.now()
         dictamen.save()
         return redirect('dictamen')
    
def deleted_dic(request, dic_id):
    dictamen = get_object_or_404(Dictamenfinal, pk=dic_id)
    if request.method == 'POST':
        dictamen.delete()
        return redirect('dictamen')

def editdictamen(request, dic_id):
    if request.method == 'GET':
        dictamen = get_object_or_404(Dictamenfinal, pk=dic_id)
        form = RevisionForm(instance=dictamen)
        return render(request, 'editdictamen.html', {'dictamen': dictamen, 'form': form})  
    else:
        try:
            dictamen = get_object_or_404(Dictamenfinal, pk=dic_id)
            form = RevisionForm(request.POST, instance=dictamen)
            form.save()
            return redirect('dictamen')
        except: ValueError
        return render(request, 'editdictamen.html', {'dictamen': dictamen, 'form': form, 'error': "Error actualiando Dictamen"})
    
def editdictamenuser(request, dic_id):
    if request.method == 'GET':
        dictamen = get_object_or_404(Dictamenfinal, pk=dic_id)
        form = RespaldoForm(instance=dictamen)
        return render(request, 'editdictamenuser.html', {'dictamen': dictamen, 'form': form})  
    else:
        dictamen = get_object_or_404(Dictamenfinal, pk=dic_id)
        form = RespaldoForm(request.POST, request.FILES, instance=dictamen)
        form.save()
        return redirect('dictamen')
      
  
    
def editdictamenadmin(request, dic_id):
    if request.method == 'GET':
        dictamen = get_object_or_404(Dictamenfinal, pk=dic_id)
        form = DictameneditadminForm(instance=dictamen)
        return render(request, 'editdictamenadmin.html', {'dictamen': dictamen, 'form': form})  
    else:
        try:
            dictamen = get_object_or_404(Dictamenfinal, pk=dic_id)
            form = DictameneditadminForm(request.POST, instance=dictamen)
            form.save()
            return redirect('dictamenadmin')
        except: ValueError
        return render(request, 'editdictamenadmin.html', {'dictamen': dictamen, 'form': form, 'error': "Error actualiando Dictamen"})
    
def editdictamenjefe(request, dic_id):
    if request.method == 'GET':
        dictamen = get_object_or_404(Dictamenfinal, pk=dic_id)
        form = Dictameneditjefe2Form(instance=dictamen)
        return render(request, 'editdictamenjefe.html', {'dictamen': dictamen, 'form': form})  
    else:
        try:
            dictamen = get_object_or_404(Dictamenfinal, pk=dic_id)
            form = Dictameneditjefe2Form(request.POST, instance=dictamen)
            form.save()
            return redirect('dictamenjefe')
        except: ValueError
        return render(request, 'editdictamenjefe.html', {'dictamen': dictamen, 'form': form, 'error': "Error actualiando Dictamen"})
    


def dashboard(request):
    return render(request, 'dashboard.html')


def signout(request):
    logout(request)
    return redirect('home')


def signin(request):
    if request.method == 'GET':
        return render(request, 'signin.html', {
            'form': AuthenticationForm
        })
    else:
        user = authenticate(
            request, username=request.POST['username'], password=request.POST['password']
        )
        if user is None:
            return render(request, 'signin.html', {
            'form': AuthenticationForm,
            'error': 'Usuario o Password es Incorecto'
        })

        else:
            login(request, user)
            data = user.groups.all()
            for g in data:
                print(g.name)
                if g.name=='Administrador':
                   return redirect('dictamenadmin')
                elif g.name=='jefe_tecnicos':
                   return redirect('dictamenjefe')
                else:
                    return redirect('dashboard')
        




def create_dictamen(request):
    
    if request.method == 'GET':
        return render(request, 'crear_dictamen.html', {
            'form': DictamenForm
        })
    else:
        form = DictamenForm(request.POST)
        new_dic = form.save(commit=False)
        new_dic.user = request.user
        new_dic.save()
        return redirect('dictamen')
       

