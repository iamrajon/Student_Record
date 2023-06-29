from django.db import models

# Create your models here.

#model for Student
class Student(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    roll = models.IntegerField()
    address = models.CharField(max_length=100)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
