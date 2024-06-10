from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class TLQuiz(models.Model):
    userID = models.IntegerField()
    question = models.TextField()
    answer = models.CharField(max_length=100)
    timeLimit = models.IntegerField(default=10)  # Default time limit in seconds

#----------------------------------------------------------------

class Quiz(models.Model):
    title = models.CharField(max_length=100)
    category = models.CharField(max_length=50)
    question = models.TextField()
    answer = models.CharField(max_length=100)
    time_limit = models.IntegerField(default=60) 
    
class RandomQuiz(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    answer = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class UserQuiz(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quiz = models.ForeignKey(RandomQuiz, on_delete=models.CASCADE)
    answered_correctly = models.BooleanField(default=False)

class SubjectiveQuiz(models.Model) :
    question = models.CharField(max_length= 255)
    answer = models.TextField()

    def __str__(self) :
        return self.question