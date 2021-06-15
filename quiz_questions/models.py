from django.db import models
from quiz_app.models import Course

# Create your models here.
class Question(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    question_text = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.question_text

    def get_answers(self):
        return self.answer_set.all()   

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer_text = models.CharField(max_length=300)   
    correct = models.BooleanField(default=False) 

    def __str__(self):
        return f"{self.question} >>>>> {self.correct}"




