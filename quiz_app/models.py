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
    score = models.IntegerField(default=0)
    mod_date = models.DateTimeField(auto_now_add=True)
    
    # id = models.IntegerField(default=1,null=False,primary_key=True)

    def __str__(self):
        return f"{str(self.course)} => {str(self.score)}"


