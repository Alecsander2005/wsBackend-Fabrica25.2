from django.urls import path
from . import views

urlpatterns = [
    path('', views.nome_musica, name='musicas_home'),
    path('musicas-salvas/', views.musicas_salvas, name='musicas_salvas'),
    path('salvar-musica/', views.salvar_musica, name='salvar_musica'),
    path('excluir-musica/<int:musica_id>/', views.excluir_musica, name='excluir_musica'),

    # Playlists
    path('playlists/', views.listar_playlists, name='listar_playlists'),
    path('playlists/criar/', views.criar_playlist, name='criar_playlist'),
    path('playlists/<int:playlist_id>/', views.detalhes_playlist, name='detalhes_playlist'),
    path('playlists/<int:playlist_id>/adicionar/<int:musica_id>/', views.adicionar_musica_playlist, name='adicionar_musica_playlist'),
    path('playlists/<int:playlist_id>/remover/<int:musica_id>/', views.remover_musica_playlist, name='remover_musica_playlist'),

    # Adicionar música direto da busca
    path('adicionar-musica-busca/', views.adicionar_musica_busca, name='adicionar_musica_busca'),
]
