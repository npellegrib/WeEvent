from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User

class Evento(models.Model):
    nombre = models.CharField(max_length=255)
    ubicacion = models.CharField(max_length=255)
    fechaInicio = models.DateField()
    fechaFin = models.DateField()
    organizador = models.ForeignKey(User, on_delete=models.CASCADE)
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to='pagina/static/pagina/event_images/', null=True, blank=True)
    videos = models.URLField()
    precio = models.FloatField()
    capacidad = models.IntegerField()
    asistencia = models.IntegerField(default=0)
    categorias = models.CharField(max_length=255)
    etiquetas = models.CharField(max_length=255)
    calificacion = models.IntegerField(default=0)
    puntuacion = models.FloatField(default=0)
    # comentarios = models.ManyToManyField(User, through='Comentario')

class Comentario(models.Model):
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    texto = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comentario por {self.usuario.username} en {self.evento.nombre}'
    

class Like(models.Model):
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.usuario.username} le gusta {self.evento.nombre}'

class Attendance(models.Model):
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.usuario.username} irá al evento {self.evento.nombre}'
