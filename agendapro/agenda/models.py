from django.db import models

# Create your models here.
class UtenteRubrica(models.Model):
    nome = models.CharField(default = '',max_length=12)
    cogno = models.CharField(default = '',max_length=20)
    tele = models.CharField(default = '',max_length=10)
    email = models.CharField(default = '',max_length=20)

    def ___str___(self):
        return "%s %s"%(self.nome, self.cogno)

    class meta:
        db_table = "Utenti"
        order_with_respect_to = 'cogno'
        verbose_name = "Utente"
        verbose_name_plural = "Utenti"

class UtenteAppuntamenti(models.Model):
    nomeu = models.ForeignKey(UtenteRubrica, on_delete=models.SET_NULL,blank=True,null=True)
    dataa = models.DateTimeField()
    
    class meta:
        verbose_name = "Appuntamento"
        verbose_name_plural = "Appuntamenti"
        order_with_respect_to = 'dataa'
