"""
URL configuration for clinica_hemodialisis project.

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
from django.urls import path
from core import views as views_core
from pacientes import views as views_pacientes
from medicos import views as views_medicos
from login import views as views_login
from register import views as views_register
from medicamentos import views as views_medicine

urlpatterns = [
    path('', views_core.index, name='index'),
    path('register/', views_register.register, name='register'),
    path('login/', views_login.login_user, name='login_user'),
    path('logout/', views_login.logout_user, name='logout_user'),
    path('pacientes/', views_pacientes.pacientes, name='pacientes'),
    path('editar_paciente/<int:id_patient>/', views_pacientes.edit_patient, name='edit_patient'),
    path('confirm_delete_patient/<int:id_patient>/', views_pacientes.confirm_delete_patient, name='confirm_delete_patient'),
    path('delete_patient/<int:id_patient>/', views_pacientes.delete_patient, name='delete_patient'),
    path('agregar_paciente/', views_pacientes.agregar_paciente, name='agregar_paciente'),
    path('medicos_registrados/', views_medicos.medicos_registrados, name='medicos_registrados'),
    path('medicines/', views_medicine.medicines, name='medicines'),
    path('add_medicines/', views_medicine.add_medicines, name='add_medicines'),
    path('admin/', admin.site.urls),
]
