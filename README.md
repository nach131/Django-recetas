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

====================

# AWS

sudo yum install git -y

$-> sudo yum install docker -y
$-> sudo service docker start

sudo usermod -a -G docker ec2-user

sudo usermod -aG docker $USER

# make docker  autostart
$-> sudo chkconfig docker on
# I strongly recommend install also: git (sudo yum install -y git)

$-> sudo reboot # only if for you it is neccesary


# docker-compose (latest version)
$-> sudo curl -L https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m) -o /usr/local/bin/docker-compose
# Fix permissions after download
$-> sudo chmod +x /usr/local/bin/docker-compose
# Verify success
$-> docker-compose version

# run server
docker-compose -f docker-compose-deploy.yml up -d
