from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from .forms import DictamenForm
from .forms import DictameneditForm
from .models import Dictamenfinal
from django.utils import timezone

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
    dictamens = Dictamenfinal.objects.filter(user=request.user, Datecompleted__isnull=True)
    return render(request, 'dictamen.html', {'dictamens': dictamens})

def dictamen_creado(request):
    dictamens = Dictamenfinal.objects.filter(user=request.user, Datecompleted__isnull=True, Creado__isnull=False)
    return render(request, 'dictamen_creado.html', {'dictamens': dictamens})

def dictamen_pendiente(request):
    dictamens = Dictamenfinal.objects.filter(user=request.user, Datecompleted__isnull=True)
    return render(request, 'dictamen_pendiente.html', {'dictamens': dictamens})

def dictamen_imprimir(request):
    dictamens = Dictamenfinal.objects.filter(user=request.user, Datecompleted__isnull=True, Imprimir__isnull=False)
    return render(request, 'dictamen_imprimir.html', {'dictamens': dictamens})

def dictamen_finalizado(request):
    dictamens = Dictamenfinal.objects.filter(user=request.user, Datecompleted__isnull=True, Finalizado__isnull=False)
    return render(request, 'dictamen_finalizado.html', {'dictamens': dictamens})





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
        form = DictameneditForm(instance=dictamen)
        return render(request, 'editdictamen.html', {'dictamen': dictamen, 'form': form})  
    else:
        try:
            dictamen = get_object_or_404(Dictamenfinal, pk=dic_id)
            form = DictameneditForm(request.POST, instance=dictamen)
            form.save()
            return redirect('dictamen')
        except: ValueError
        return render(request, 'editdictamen.html', {'dictamen': dictamen, 'form': form, 'error': "Error actualiando Dictamen"})
    


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
       

