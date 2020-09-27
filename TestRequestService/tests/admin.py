from django.contrib import admin
from .models import Test, Question, Difficulty, Category

admin.site.register(Test)
admin.site.register(Question)
admin.site.register(Difficulty)
admin.site.register(Category)

