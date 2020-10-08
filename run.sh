cd backend
docker-compose up -d --build
docker-compose run web python manage.py migrate
docker-compose run web python createsuperuser.py

cd ../frontend
docker-compose up -d --build
