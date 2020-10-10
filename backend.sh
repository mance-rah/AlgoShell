cd backend
docker-compose up -d --build
docker-compose run web python manage.py migrate
docker-compose run web python create_superuser.py
docker-compose run web python save_questions.py