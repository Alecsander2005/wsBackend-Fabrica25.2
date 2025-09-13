ProjetoMusicas

Este é um projeto Django para pesquisar músicas no Deezer, salvar em músicas favoritas e organizar em playlists no banco de dados.

Tecnologias e Dependências

Python 3.13

Django 5.2.6

MySQL

PyMySQL 1.1.2

mysqlclient 2.2.7

Outras bibliotecas: requests, asgiref, certifi, charset-normalizer, idna, sqlparse, tzdata, urllib3

O arquivo requirements.txt contém todas as versões usadas:

asgiref==3.9.1
certifi==2025.8.3
charset-normalizer==3.4.3
Django==5.2.6
idna==3.10
mysqlclient==2.2.7
PyMySQL==1.1.2
requests==2.32.5
sqlparse==0.5.3
tzdata==2025.2
urllib3==2.5.0


Para instalar todas as dependências:

pip install -r requirements.txt

Configuração do Banco de Dados

O projeto utiliza MySQL. Configure o settings.py do Django com os dados do seu banco:

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'projetomusicas',
        'USER': 'root',
        'PASSWORD': 'sua_senha',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}


No create_db_if_not_exists.py, adicione a sua senha do banco de dados:

B_NAME = 'projetomusicas'
USER = 'root'
PASSWORD = 'suasenha'
HOST = 'localhost'


Caso queira que o banco seja criado automaticamente se não existir, você precisará criar um script externo em Python que conecte ao MySQL.

Criando o Banco de Dados
python create_db_if_not_exists.py

Rodando o Projeto

Clone o repositório.

Ative seu ambiente virtual.

Instale as dependências (pip install -r requirements.txt).

Configure o banco de dados no settings.py.

Execute as migrações:

python manage.py makemigrations
python manage.py migrate


Execute o servidor:

python manage.py runserver


Acesse em http://127.0.0.1:8000/
.

Funcionalidades Adicionadas

Busca de músicas no Deezer.

Salvar músicas favoritas no banco.

Criar, listar e visualizar playlists.

Adicionar músicas às playlists direto da área de busca.

Remover músicas das playlists.

Templates estilizados de forma consistente usando base.html.

Estrutura do Projeto
ProjetoMusicas/
│
├── ProjetoMusicas/       # Configurações do projeto Django
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── app/                  # Aplicativo principal
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── templates/
│       ├── base.html           # Template base
│       ├── exibição_resultados/
│       │   └── resultado.html
│       ├── musicas/
│       │   └── musicas_salvas.html
│       └── playlists/
│           ├── criar.html
│           ├── detalhe.html
│           └── lista.html
│
├── manage.py
└── requirements.txt

Observações

Certifique-se de que o MySQL está instalado e funcionando.

Para rodar em outro computador, basta clonar o projeto, instalar as dependências e configurar o banco.

Se estiver usando PyMySQL, adicione no __init__.py do projeto:

import pymysql
pymysql.install_as_MySQLdb()


Isso garante compatibilidade com o Django.

Autor

Petrus