from django.db import models

# Create your models here.
class Student(models.Model):
    roll=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=99)
    city=models.CharField(max_length=99)
    marks=models.FloatField()
    recorded_on=models.DateTimeField()

    def __str__(self):
        return self.name
    