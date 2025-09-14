🎵 ProjetoMúsicas

Este é um projeto Django para pesquisar músicas usando a API do Deezer, salvar em músicas favoritas e organizar em playlists, tudo armazenado no banco de dados MySQL.

📦 Tecnologias e Dependências

Python 3.13

Django 5.2.6

MySQL

Conectores MySQL:

PyMySQL 1.1.2

mysqlclient 2.2.7

Bibliotecas adicionais:

requests

asgiref

certifi

charset-normalizer

idna

sqlparse

tzdata

urllib3

📄 Instalação de Dependências

O arquivo requisitos.txt contém todas as bibliotecas necessárias:

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


Para instalar, execute:

pip install -r requisitos.txt

🛠️ Configuração do Banco de Dados

Edite o arquivo ProjetoMusicas/settings.py:

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

🐍 Script para criar o banco automaticamente

No arquivo create_db_if_not_exists.py, configure:

B_NAME = 'projetomusicas'
USER = 'root'
PASSWORD = 'sua_senha'
HOST = 'localhost'


Para criar o banco automaticamente (caso não exista):

python create_db_if_not_exists.py

▶️ Executando o Projeto

Clone o repositório:

git clone https://github.com/Alecsander2005/wsBackend-Fabrica25.2.git
cd wsBackend-Fabrica25.2


Crie e ative um ambiente virtual (opcional, mas recomendado):

python -m venv venv
# Windows:
venv\Scripts\activate
# Linux/macOS:
source venv/bin/activate


Instale as dependências:

pip install -r requisitos.txt


Configure o banco no settings.py.

Adicione no __init__.py da pasta do projeto:

import pymysql
pymysql.install_as_MySQLdb()


Execute as migrações:

python manage.py makemigrations
python manage.py migrate


Inicie o servidor:

python manage.py runserver


Acesse: http://127.0.0.1:8000/

✅ Funcionalidades

🔍 Buscar músicas pela API do Deezer

⭐ Salvar músicas favoritas

🎵 Criar e gerenciar playlists

➕ Adicionar músicas às playlists diretamente da busca

❌ Remover músicas das playlists

💅 Templates organizados com base.html

🗂️ Estrutura do Projeto
ProjetoMusicas/
│
├── ProjetoMusicas/         # Configurações do projeto Django
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── app/                    # App principal
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── templates/
│       ├── base.html
│       ├── exibição_resultados/
│       │   └── resultado.html
│       ├── musicas/
│       │   └── musicas_salvas.html
│       └── playlists/
│           ├── criar.html
│           ├── detalhe.html
│           └── lista.html
│
├── create_db_if_not_exists.py
├── manage.py
└── requisitos.txt

⚠️ Observações

Certifique-se de que o MySQL esteja instalado e funcionando corretamente.

O projeto é compatível com mysqlclient e PyMySQL — ambos podem ser usados, mas se optar pelo PyMySQL, adicione o trecho de código no __init__.py como mostrado acima.

Para rodar em outro computador, basta:

Clonar o repositório

Instalar as dependências

Configurar o banco de dados

👤 Autor

Desenvolvido por Petrus
