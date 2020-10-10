import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')
os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true"
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
from django.contrib.auth.models import User

User.objects.create_superuser('admin', 'admin@algoshell.io', '1234')