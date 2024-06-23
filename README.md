# python-app-api

para saber los error de syntax en el codido

 docker compose run --rm app sh -c "flake8"
 

 Para testear Django

 docker compose run --rm app sh -c "python manage.py test"

lanzar docker para crear el proyeto, docker se para y se borra

crea el proyecto
docker compose run --rm app sh -c "django-admin startproject app ."

crea una app "core"
docker compose run --rm app sh -c "django-admin startapp core"

=====================


docker compose run --rm app sh -c "python manage.py makemigrations"

docker compose run --rm app sh -c "python manage.py migrate"


