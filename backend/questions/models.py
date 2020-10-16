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
    _test_cases = models.JSONField()
    
    @property
    def test_cases(self):
        suite = []

        for case in self._test_cases:
            curr_input = {'input':{}}
            for param_name, param_value in zip(case['input'], self.parameters):    
                curr_input['input'][param_value] = param_name
                curr_input['output'] = case['output']
            suite.append(curr_input)

        return suite
    
    @test_cases.setter
    def test_cases(self, test_cases):
        self._test_cases = test_cases


    


    def __str__(self):
        return self.name