from django.urls import path
from . import views

urlpatterns = [
    path('', views.nome_musica, name='musicas_home'),
    path('api/', views.nome_musica, name='nome_musica_api'),
    path('salvar/', views.salvar_musica, name='salvar_musica'),
    path('excluir/<int:musica_id>/', views.excluir_musica, name='excluir_musica'),

    # ✅ Nova rota para visualizar as músicas salvas
    path('salvas/', views.musicas_salvas, name='musicas_salvas'),
]
