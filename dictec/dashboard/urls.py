"""
URL configuration for dashboard project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from dictec import views
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
       path('signup/', views.signup, name='signup',),
       path('dictamen/', views.dictamen, name='dictamen',),
       path('dictamenadmin/', views.dictamenadmin, name='dictamenadmin',),
       path('dictamenjefe/', views.dictamenjefe, name='dictamenjefe',),
       path('dictamenadmin/<int:dic_id>/', views.dicdetalleadmin, name='dicdetalleadmin',),
       path('dictamenjefe/<int:dic_id>/', views.dicdetallejefe, name='dicdetallejefe',),
       path('creado/', views.dictamen_creado, name='dictamen_creado',),
       path('creadoadmin/', views.dictamen_creadoadmin, name='dictamen_creadoadmin',),
       path('creadojefe/', views.dictamen_creadojefe, name='dictamen_creadojefe',),
       path('pendiente/', views.dictamen_pendiente, name='dictamen_pendiente',),
       path('pendienteadmin/', views.dictamen_pendienteadmin, name='dictamen_pendienteadmin',),
       path('pendientejefe/', views.dictamen_pendientejefe, name='dictamen_pendientejefe',),
       path('imprimir/', views.dictamen_imprimir, name='dictamen_imprimir',),
       path('imprimiradmin/', views.dictamen_imprimiradmin, name='dictamen_imprimiradmin',),
       path('imprimirjefe/', views.dictamen_imprimirjefe, name='dictamen_imprimirjefe',),
       path('finalizado/', views.dictamen_finalizado, name='dictamen_finalizado',),
       path('finalizadoadmin/', views.dictamen_finalizadoadmin, name='dictamen_finalizadoadmin',),
       path('finalizadojefe/', views.dictamen_finalizadojefe, name='dictamen_finalizadojefe',),
       path('dictamen/create/', views.create_dictamen, name='crear_dictamen',),
       path('dictamen/<int:dic_id>/', views.dicdetalle, name='dicdetalle',),
       path('imprimir/<int:dic_id>/', views.dicdetalleuser, name='dicdetalleuser',),
       path('dicdetalle/<int:dic_id>/complete', views.complete_dic, name='complete_dic',),
       path('dicdetalle/<int:dic_id>/deleted', views.deleted_dic, name='deleted_dic',),
       path('dicdetalle/<int:dic_id>/', views.editdictamen, name='editdictamen',),
       path('dicdetalleuser/<int:dic_id>/', views.editdictamenuser, name='editdictamenuser',),
       path('dicdetalleadmin/<int:dic_id>/', views.editdictamenadmin, name='editdictamenadmin',),
       path('dicdetallejefe/<int:dic_id>/', views.editdictamenjefe, name='editdictamenjefe',),
       path('logout/', views.signout, name='logout',),
       path('signin/', views.signin, name='signin',),
       path('dashboard/', views.dashboard, name='dashboard',)
       

]

