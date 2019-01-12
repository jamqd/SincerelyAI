from django.db import models

# Create your models here.
class Questions(models.Model):
    question_query = models.CharField(max_length=100)
    question_answer = models.CharField(max_length=100)
    def __str__(self):
        return self.question_query
