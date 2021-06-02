from django.core.management.base import BaseCommand, CommandError
from gestionavisos.models import Evento
from datetime import date

class Command(BaseCommand):
    help="Envía avisos pendientes"
    def handle(self, *args, **options):
        fecha_hoy=date.today()
        eventos = Evento.objects.all()
        for e in eventos:
            fecha=e.fecha
            #Si la fecha del evento es futura, se envia un
            #recordatorio del futuro evento
            self.stdout.write("La fecha es:"+str(fecha))
            self.stdout.write(str(e))
            if fecha > fecha_hoy:
                self.stdout.write("Se envia aviso para esto")
