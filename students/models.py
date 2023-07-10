from django.db import models

# Create your models here.
class Student(models.Model):
    student_id = models.PositiveIntegerField()
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
    field_of_study = models.CharField(max_length=50)
    gpa = models.DecimalField(max_digits=3, decimal_places=2)

    def __str__(self):
        return self.first_name + " " + self.last_name