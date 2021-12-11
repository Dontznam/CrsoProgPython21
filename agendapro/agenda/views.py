from django.http.response import HttpResponse
from django.shortcuts import render
from django.core.serializers import serialize
from django.http import HttpResponse,JsonResponse
from .models import UtenteRubrica, UtenteAppuntamenti
from django.forms.models import model_to_dict
import json

def api_agenda_utenti(request):
    output = "<hl>Agenda utenti</hl>"
    return HttpResponse(output)

def api_utente(request, id):
    output = "<hl>Richiesta Utente:</hl> "+ str(id)
    utente = UtenteRubrica.objects.get(pk=id)
    json_dict = json.dumps(model_to_dict(utente))
    return HttpResponse(json_dict, content_type="application/json")

def api_utenti(request):
    utenti = UtenteRubrica.objects.all()
    utenti_dic = []
    for u in utenti:
        utenti_dic.append(model_to_dict(u))
    return JsonResponse(utenti_dic, safe=False)

def api_appuntamenti(request, id):
    output = "<hl>Richiesta Appuntamento:</hl> "+ str(id)
    appuntamento = UtenteAppuntamenti.objects.get(pk=id)
    app_dic = { 'data' : str(UtenteAppuntamenti.dataa), 'utente' : str(UtenteAppuntamenti.nomeu), 'email' : str(UtenteAppuntamenti.UtenteRubrica.email) }#'email' : str(UtenteAppuntamenti.utente.email)
    json_dict = json.dumps(model_to_dict(appuntamento))
    return HttpResponse(json_dict, content_type="application/json")
# Create your views here.
