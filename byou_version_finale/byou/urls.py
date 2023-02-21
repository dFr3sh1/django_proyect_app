"""byou URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
import agenda.views

#app_name = "agenda"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accueil/', agenda.views.index, name='accueil'),
    #path('base/', agenda.views.index, name='base'),
    path('confirmation/', agenda.views.confirmation, name='confimation'),
    path('historique/', agenda.views.historial, name='historique'),
    path('login/', agenda.views.login, name='login'),
    path('logout/', agenda.views.logout_user, name='logout'),
    path('rendez-vous/', agenda.views.appointment, name='rendez-vous'),
    path('s_enregistrer/', agenda.views.signup, name='s_enregistrer'),    
]
