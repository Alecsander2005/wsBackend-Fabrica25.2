from django.db import models

class MusicaFavorita(models.Model):
    titulo = models.CharField(max_length=255)
    artista = models.CharField(max_length=255)
    album = models.CharField(max_length=255, blank=True, null=True)
    link = models.URLField(blank=True, null=True)
    data_adicao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.titulo} - {self.artista}"
