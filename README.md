# python-app-api

## **GitHub/Build a Backend REST API with Python & Django - Advanced/src-upgrade**

para saber los error de syntax en el codido

 docker compose run --rm app sh -c "flake8"
 

 Para testear Django

 docker compose run --rm app sh -c "python manage.py test"

lanzar docker para crear el proyeto, docker se para y se borra

crea app 
docker compose run --rm app sh -c "django-admin startproject app ."

crea core
docker compose run --rm app sh -c "django-admin startapp core"

=====================

python manage.py makemigrations

python manage.py migrate

