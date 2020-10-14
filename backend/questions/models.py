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
    function_name = models.CharField(max_length=50)
    parameters = models.JSONField()
    test_cases = models.JSONField()
    
    def test_suite(self):
        suite = []

        for case in test_cases:
            curr_input = {}
            for param_name, param_value in zip(case['input'], parameters):
                curr_input[param_name] = param_value
            suite.append(curr_input)

        return suite

    def __str__(self):
        return self.name