from django.db import models

class Test(models.Model):
    inputs = models.JSONField()
    expected = models.JSONField()
    question = models.ForeignKey(
        Question,
        on_delete=models.CASCADE
    )

class Question(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE
    )
    difficulty = models.ForeignKey(
        Difficulty,
        on_delete=models.CASCADE
    )

class Category(models.Model):
    name = models.CharField(max_length=50)

class Difficulty(model.Model):
    name = models.CharField(max_length=50)