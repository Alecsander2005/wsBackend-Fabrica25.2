from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from .models import MusicaFavorita
import requests
import urllib.parse


# Página de busca de músicas
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

    return render(request, 'exibição_resultados/resultado.html', {
        'musicas': musicas,
        'mensagem': mensagem
    })


# Salvar música no banco
def salvar_musica(request):
    if request.method == 'POST':
        titulo = request.POST.get('titulo')
        artista = request.POST.get('artista')
        album = request.POST.get('album')
        link = request.POST.get('link')

        if titulo and artista:
            MusicaFavorita.objects.create(
                titulo=titulo,
                artista=artista,
                album=album,
                link=link
            )

    return redirect('musicas_home')


# Excluir música salva
def excluir_musica(request, musica_id):
    musica = get_object_or_404(MusicaFavorita, id=musica_id)
    musica.delete()
    return redirect('musicas_salvas')


# Página separada com músicas salvas
def musicas_salvas(request):
    favoritas = MusicaFavorita.objects.all()
    return render(request, 'musicas/musicas_salvas.html', {'favoritas': favoritas})
