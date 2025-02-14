## Requisitos

* Python 3 ou superior - Conferir a versão: python --version
* Django 5 ou superior - Conferir a versão: django-admin --version
* GIT - Conferir a instalação: git -v
* SQL Server 2019 - Conferir a versão: 

## Habilitar Power Shell Temporário
- Se deseja permitir a execução de scripts locais (recomendado), execute:

```
Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
```

## Tema JAZZMIN_SETTINGS
Django Jazzmin https://django-jazzmin.readthedocs.io/
Instalação
pip install django-jazzmin

core/settings.py

INSTALLED_APPS = [
 'jazzmin',
 'django.contrib.admin',
 ...
]

JAZZMIN_SETTINGS = {
 'site_title': 'Core CET-Rio',
 'site_header': 'Core CET-Rio',
 'site_brand': 'Core CET-Rio',
 'icons': {
 'auth': 'fas fa-users-cog',
 'auth.user': 'fas fa-user',
 'auth.Group': 'fas fa-users',
 'products.Brand': 'fas fa-copyright',
 'products.Category': 'fas fa-object-group',
 'products.Product': 'fas fa-box',
 },
 'welcome_sign': 'Bem-vindo(a) ao Core CET-Rio',
 'copyright': 'GTS | CET-Rio',
 # 'search_model': ['products.Product',],
 'show_ui_builder': True,
}


## Bando de Dados

# Instalar dependências
Antes de conectar o Django ao SQL Server, você precisa instalar alguns pacotes necessários:

```
pip install django pyodbc django-mssql-backend

pip install mssql-django

```

# Em seguida em settings.py do core
Acrescentar as conexões DATABASES []
```
DATABASES = {  
}

## Executar migrations para criar as tabelas

```
python manage.py makemigrations
python manage.py migrate

```


## Repositório Exemplo


* https://github.com/pycodebr/sgp

## Criar venv e instalar Django
python -m venv venv
venv/Scripts/activate
pip install django

### Criar e inicializar projeto Django
django-admin startproject core .
python manage.py migrate
python manage.py createsuperuser senha unibancoA#

## Rodar o sistema e acessar o admin
python manage.py runserver

## Criar app de produtos

python manage.py startapp products

core/settings.py

INSTALLED_APPS = [
 'products',
]
LANGUAGE_CODE = 'pt-br'
TIME_ZONE = 'America/Sao_Paulo'

## Modelar o sistema


## Criar Tabela Fechamentos

python manage.py startapp closures

products/models.py

from django.db import models
class Brand(models.Model):
 name = models.CharField(max_length=100, verbose_name='Nome')
 is_active = models.BooleanField(default=True, verbose_name='Ativo')
 description = models.TextField(null=True, blank=True, verbose_name='Descrição')
 created_at = models.DateTimeField(auto_now_add=True, verbose_name='Criado em')
 updated_at = models.DateTimeField(auto_now=True, verbose_name='Atualizado em')
 class Meta:
 ordering = ['name']
 verbose_name = 'Marca'
 def __str__(self):
 return self.name

 class Category(models.Model):
 name = models.CharField(max_length=100, verbose_name='Nome')
 is_active = models.BooleanField(default=True, verbose_name='Ativo')
 description = models.TextField(null=True, blank=True, verbose_name='Descrição')
 created_at = models.DateTimeField(auto_now_add=True, verbose_name='Criado em')
 updated_at = models.DateTimeField(auto_now=True, verbose_name='Atualizado em')
 class Meta:
 ordering = ['name']
 verbose_name = 'Categoria'
 def __str__(self):
 return self.name


 class Product(models.Model):
 title = models.CharField(max_length=100, verbose_name='Título')
 brand = models.ForeignKey(Brand, on_delete=models.PROTECT,
 related_name='products', verbose_name='Marca')
 category = models.ForeignKey(Category, on_delete=models.PROTECT,
 related_name='products', verbose_name='Categoria')
 price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Preço')
 is_active = models.BooleanField(default=True, verbose_name='Ativo')
 description = models.TextField(null=True, blank=True, verbose_name='Descrição')
 created_at = models.DateTimeField(auto_now_add=True, verbose_name='Criado em')
 updated_at = models.DateTimeField(auto_now=True, verbose_name='Atualizado em')
 class Meta:
 ordering = ['title']
 verbose_name = 'Produto'
 def __str__(self):
 return self.title