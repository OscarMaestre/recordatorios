from django.contrib.admin.sites import AlreadyRegistered
from django.db import models

# Create your models here.



class DireccionEmail(models.Model):
    alias           =   models.CharField(max_length=240)
    direccion       =   models.EmailField()

    def __str__(self) -> str:
        return str(self.alias) + " <"+str(self.direccion)+">"

class Evento(models.Model):
    texto               = models.CharField(max_length=240, verbose_name="Evento a recordar")
    fecha               = models.DateField()  
    email_remitente     = models.ForeignKey(DireccionEmail, on_delete=models.CASCADE, related_name="Remitente")
    email_destinatario  = models.ForeignKey(DireccionEmail, on_delete=models.CASCADE, related_name="Destinatario")
    def __str__(self) -> str:
        plantilla="{0}, caduca el {1}"
        return plantilla.format(str(self.texto), str(self.fecha))




