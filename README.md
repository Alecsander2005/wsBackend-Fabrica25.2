# ProjetoMusicas

Este é um projeto Django Para pesquisar suas musicas do dreezer e salvar em uma playlist para o banco de dados
---

## Tecnologias e Dependências

- Python 3.13
- Django 5.2.6
- MySQL
- PyMySQL 1.1.2
- mysqlclient 2.2.7
- Outras bibliotecas: requests, asgiref, certifi, charset-normalizer, idna, sqlparse, tzdata, urllib3

O arquivo `requirements.txt` contém todas as versões usadas:

```txt
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

bash
Copiar código
pip install -r requirements.txt
Configuração do Banco de Dados
O projeto utiliza MySQL. Configure o settings.py do Django com os dados do seu banco:

python
Copiar código
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'nome_do_banco',
        'USER': 'root',
        'PASSWORD': 'sua_senha',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
Caso queira que o banco seja criado automaticamente se não existir, você precisará criar um script externo em Python que conecte ao MySQ:

Criando o Banco De Dados
python create_db_if_not_exists.py


Rodando o Projeto
Clone o repositório

Ative seu ambiente virtual

Instale as dependências

Configure o banco de dados

Execute as migrações:

bash
python manage.py makemigrations
python manage.py migrate



bash
python manage.py runserver
Acesse em http://127.0.0.1:8000/.

Estrutura do Projeto
bash
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
│
├── manage.py
└── requirements.txt
Observações
Certifique-se de que o MySQL está instalado e funcionando no seu computador.

Para rodar em outro computador, basta clonar o projeto, instalar as dependências e configurar o banco.

Se estiver usando PyMySQL, adicione no __init__.py do projeto:

python
Copiar código
import pymysql
pymysql.install_as_MySQLdb()
Isso garante compatibilidade com o Django.

Autor
Petrus
