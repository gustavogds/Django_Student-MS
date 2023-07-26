from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Student(models.Model):
    student_number = models.PositiveIntegerField()
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
    field_of_study = models.CharField(max_length=50)
    gpa = models.DecimalField(max_digits=3, decimal_places=2)

    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.first_name + " " + self.last_name