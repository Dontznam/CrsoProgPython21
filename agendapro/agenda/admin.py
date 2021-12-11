from django.contrib import admin
from .models import UtenteRubrica, UtenteAppuntamenti

# Register your models here.
class UtenteRubricaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cogno', 'tele', 'email')
    
class UtenteAppuntamentiAdmin(admin.ModelAdmin):
    list_display = ('nomeu', 'dataa')

admin.site.register(UtenteRubrica)
admin.site.register(UtenteAppuntamenti)
