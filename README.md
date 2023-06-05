# promocao_api
====================Uso==================================

cd ~

git clone https://github.com/iago-mansur/promocao_api.git

cd promocao_api

code .

python3 -m venv .venv

. .venv/bin/activate

pip install -r requirements.txt

python manage.py makemigrations promocao_api 

python manage.py migrate

python manage.py runserver


==================Desenvolvimento========================

mkdir promocao_api

cd promocao_api

python --version

-----commit: 75b82ca96b1e65764cc37f21a36b64877c5232d4---
python3 -m venv .venv

. .venv/bin/activate
--------------------------------------------------------

pip install django

pip install djangorestframework

django-admin startproject promocao_api .

python manage.py runserver

http://127.0.0.1:8000/

CONTROL-C

git init

git config user.name iago-mansur

git config user.email iagoma@gmail.com

git add .

git commit -m "inicializando promocao_api"

git branch -M main

code .

python manage.py migrate

python manage.py createsuperuser

admin / email@email.com / 123456 / y

criar models.py

CONTROL-S

atualizar settings.py

python manage.py makemigrations promocao_api

python manage.py migrate

criar admin.py	

CONTROL-S

CONTROL-C

python manage.py runserver

git add .

git commit -m "criacao do modelo de promocao_api"

criar serializer.py
CONTROL-S

criar views.py
CONTROL-S

atualizar settings.py
CONTROL-S

atualizar urls.py
CONTROL-S

python manage.py migrate

python manage.py runserver

git add .

git commit -m "teste lista de objetos da promocao_api"

editar views.py
CONTROL-S

editar urls.py
CONTROL-S

python manage.py migrate

python manage.py runserver

git add .

git commit -m "lista detalhada de objetos da promocao_api"

editar urls.py

git add .

git commit -m "add format_suffix_patterns"

python3 -m venv .venv

. .venv/bin/activate

pip install django

pip install djangorestframework

CRTL + SHIFT + P

>Select Interpreter

Recommended

git add .

git commit -m "Insert venv"

Editar views.py

pip freeze > requirements.txt

git add .

git commit -m "Fix PUT."
