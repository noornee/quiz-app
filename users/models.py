from django.db import models
from django.contrib.auth.models import User
from quiz_app.models import Course

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    department = models.CharField(max_length=100,blank=True, null=True)
    level = models.IntegerField(blank=True, null=True)
    profile_image = models.ImageField(default='placeholder.jpg',upload_to='profile_pictures')

    def __str__(self):
        return self.user.username


class Result(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE) 
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.FloatField(default=0)
    mod_date = models.DateTimeField(auto_now_add=True)
    
    def save(self, *args, **kwargs):
        self.score = round(self.score, 2)
        super(Result, self).save(*args, **kwargs)
        
    def __str__(self):
        return f"{str(self.user)}: {str(self.course)} => {str(self.score)}"
