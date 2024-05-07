from django.db import models

class Quiz(models.Model):
    title = models.CharField(max_length=100)
    category = models.CharField(max_length=50)
    question = models.TextField()
    answer = models.CharField(max_length=100)
    time_limit = models.IntegerField(default=60)  # Default time limit in seconds
    
class RandomQuiz(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    answer = models.CharField(max_length=100)