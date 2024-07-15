# Variables
DATA_DIR = data
DATA_DIRS = ${DATA_DIR}/db ${DATA_DIR}/static/media

# Default target
all: build

# Target to create directories
create-dirs:
	@echo "Creating data directories..."
	@mkdir -p $(DATA_DIRS)

# Target to build docker-compose
build: create-dirs
	@echo "Building Docker images..."
	@docker compose build
	@docker compose run --rm app sh -c "python manage.py wait_for_db"

# Target to run and set up the application
up:
	@echo "Running setup tasks..."
	@docker compose run --rm app sh -c "python manage.py makemigrations"
	@docker compose run --rm app sh -c "python manage.py test"
	@docker compose up

super:
	@echo "Creating superuser..."
	@docker compose run --rm app sh -c "python manage.py createsuperuser"

status: 
	@echo "Control status app..."
	@docker compose ps

control:
	@echo "Control flake8.."
	@docker compose run --rm app sh -c "flake8"

mi:
	@echo "Running Migrations..."
	@docker compose run --rm app sh -c "python manage.py makemigrations"
	@docker compose run --rm app sh -c "python manage.py migrate"

test:
	@echo "Running Django test..."
	@docker compose run --rm app sh -c "python manage.py test"

down:
	@echo "Turning off everything."
	@docker compose down
# Target to clean up generated directories (optional)

clean:
	@echo "Cleaning up data directories..."
	@rm -rf $(DATA_DIR)

fclean: down clean
	@echo "Delete All..."
	@docker image prune -af
	@docker volume rm src-original_db-data
	@docker volume rm src-original_static-data

.PHONY: all create-dirs build up clean down fclean super status test control
