from django.db import models

class MusicaFavorita(models.Model):
    titulo = models.CharField(max_length=255)
    artista = models.CharField(max_length=255)
    album = models.CharField(max_length=255, blank=True, null=True)
    link = models.URLField(blank=True, null=True)
    data_adicao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.titulo} - {self.artista}"


class Playlist(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True, null=True)
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome


class MusicaNaPlaylist(models.Model):
    playlist = models.ForeignKey(Playlist, on_delete=models.CASCADE, related_name='musicas')
    musica = models.ForeignKey(MusicaFavorita, on_delete=models.CASCADE)
    data_adicao = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('playlist', 'musica')  # Evita músicas repetidas na mesma playlist

    def __str__(self):
        return f"{self.musica} na playlist {self.playlist}"
