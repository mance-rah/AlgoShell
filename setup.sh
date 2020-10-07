cd backend
docker-compose run web python manage.py migrate
docker-compose run web python manage.py createsuperuser --email admin@algoshell.io --username admin