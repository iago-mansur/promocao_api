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

python3 -m venv .venv

. .venv/bin/activate

pip install django

pip install djangorestframework

django-admin startproject promocao_api .

python manage.py runserver

http://127.0.0.1:8000/

CONTROL-C

django-admin startapp api

pip freeze > requirements.txt

python manage.py migrate

python manage.py createsuperuser

admin / email@email.com / 123456 / y

atualizar settings.py

atualizar  model.py

atualizar admin.py

python manage.py makemigrations

python manage.py migrate

python manage.py runserver

criar serializer.py

criar views.py

criar router.py

editar urls.py

python manage.py migrate

python manage.py runserver

>Select Interpreter

Recommended