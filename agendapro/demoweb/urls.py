"""demoweb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from agenda.views import api_agenda_utenti, api_utente, api_utenti, api_appuntamenti

urlpatterns = [
    #url(r'/jet', include('jet.urls', 'jet')) #django jet, python manage.py django jet
    path('/grappelli', include('grappelli.urls')),
    path('admin/', admin.site.urls),
    path('api/', api_agenda_utenti),
    path('api/rubrica/<int:id>/', api_utente),#api/1
    path('api/rubrica/', api_utenti),
    path('api/appuntamenti/<int:id>/', api_appuntamenti),
]
