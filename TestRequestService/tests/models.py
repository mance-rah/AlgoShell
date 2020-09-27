from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Difficulty(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

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

    def __str__(self):
        return self.name

class Test(models.Model):
    inputs = models.JSONField()
    expected = models.JSONField()
    question = models.ForeignKey(
        Question,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return 'Question: {}, Inputs: {}, Expected: {}'.format(question.name, inputs, expected)