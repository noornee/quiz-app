# import random
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Course(models.Model):
    course_title = models.CharField(max_length=150)
    number_of_questions = models.IntegerField()
    duration = models.IntegerField(help_text='duration of course in minutes')

    def __str__(self):
        return self.course_title

    def get_questions(self):
        '''
        ---do this to get random questions---
        questions = list(self.question_set.all()) 
        random.shuffle(questions)
        return questions[:self.number_of_questions]
        '''
        questions = self.question_set.all()  
        return questions[:self.number_of_questions]



class Result(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE) 
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.FloatField(default=0)

    def __str__(self):
        return self.score


