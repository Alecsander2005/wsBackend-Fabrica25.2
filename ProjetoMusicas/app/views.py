from django.shortcuts import render, redirect, get_object_or_404
from .models import MusicaFavorita, Playlist, MusicaNaPlaylist
import requests
import urllib.parse

# ==========================
#       MÚSICAS
# ==========================

def nome_musica(request):
    nome = request.GET.get('nome', '').strip()
    musicas = []
    mensagem = ''

    if nome:
        nome_encoded = urllib.parse.quote(nome)
        url = f'https://api.deezer.com/search?q={nome_encoded}'

        try:
            response = requests.get(url, timeout=5)
            response.raise_for_status()
            data = response.json()

            for musica in data.get('data', []):
                musicas.append({
                    'titulo': musica.get('title', 'Desconhecido'),
                    'artista': musica.get('artist', {}).get('name', 'Desconhecido'),
                    'album': musica.get('album', {}).get('title', 'Desconhecido'),
                    'link': musica.get('link', '#')
                })

            if not musicas:
                mensagem = 'Nenhuma música encontrada.'

        except requests.exceptions.RequestException:
            mensagem = 'Erro ao conectar com a API de músicas.'
    elif request.GET.get('nome') == '':
        mensagem = 'Digite o nome de uma música.'

    playlists = Playlist.objects.all()  # Para permitir adicionar músicas a playlists

    return render(request, 'exibição_resultados/resultado.html', {
        'musicas': musicas,
        'mensagem': mensagem,
        'playlists': playlists
    })


def salvar_musica(request):
    if request.method == 'POST':
        titulo = request.POST.get('titulo')
        artista = request.POST.get('artista')
        album = request.POST.get('album')
        link = request.POST.get('link')

        if titulo and artista:
            MusicaFavorita.objects.get_or_create(
                titulo=titulo,
                artista=artista,
                defaults={'album': album, 'link': link}
            )

    return redirect('musicas_home')


def excluir_musica(request, musica_id):
    musica = get_object_or_404(MusicaFavorita, id=musica_id)
    musica.delete()
    return redirect('musicas_salvas')


def musicas_salvas(request):
    favoritas = MusicaFavorita.objects.all()
    return render(request, 'musicas/musicas_salvas.html', {'favoritas': favoritas})


# ==========================
#       PLAYLISTS
# ==========================

def listar_playlists(request):
    playlists = Playlist.objects.all()
    return render(request, 'playlist/lista.html', {'playlists': playlists})


def criar_playlist(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        descricao = request.POST.get('descricao', '')
        if nome:
            Playlist.objects.create(nome=nome, descricao=descricao)
        return redirect('listar_playlists')
    return render(request, 'playlist/criar.html')


def detalhes_playlist(request, playlist_id):
    playlist = get_object_or_404(Playlist, id=playlist_id)
    musicas_disponiveis = MusicaFavorita.objects.exclude(
        id__in=playlist.musicas.values_list('musica_id', flat=True)
    )
    return render(request, 'playlist/detalhe.html', {
        'playlist': playlist,
        'musicas_disponiveis': musicas_disponiveis
    })


def adicionar_musica_playlist(request, playlist_id, musica_id):
    playlist = get_object_or_404(Playlist, id=playlist_id)
    musica = get_object_or_404(MusicaFavorita, id=musica_id)
    MusicaNaPlaylist.objects.get_or_create(playlist=playlist, musica=musica)
    return redirect(request.META.get('HTTP_REFERER', 'listar_playlists'))


def remover_musica_playlist(request, playlist_id, musica_id):
    playlist = get_object_or_404(Playlist, id=playlist_id)
    musica = get_object_or_404(MusicaFavorita, id=musica_id)
    MusicaNaPlaylist.objects.filter(playlist=playlist, musica=musica).delete()
    return redirect(request.META.get('HTTP_REFERER', 'detalhes_playlist', playlist_id=playlist.id))


# ==========================
#   ADICIONAR MÚSICA DA BUSCA
# ==========================

def adicionar_musica_busca(request):
    if request.method == 'POST':
        playlist_id = request.POST.get('playlist_id')
        titulo = request.POST.get('musica_titulo')
        artista = request.POST.get('musica_artista')
        album = request.POST.get('musica_album')
        link = request.POST.get('musica_link')

        # Salva a música no banco se ainda não existir
        musica, created = MusicaFavorita.objects.get_or_create(
            titulo=titulo,
            artista=artista,
            defaults={'album': album, 'link': link}
        )

        # Adiciona à playlist
        playlist = get_object_or_404(Playlist, id=playlist_id)
        MusicaNaPlaylist.objects.get_or_create(playlist=playlist, musica=musica)

    return redirect(request.META.get('HTTP_REFERER', 'musicas_home'))
