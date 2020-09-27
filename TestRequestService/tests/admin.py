from django.contrib import admin
from .models import Question, Difficulty, Category

admin.site.register(Question)
admin.site.register(Difficulty)
admin.site.register(Category)

