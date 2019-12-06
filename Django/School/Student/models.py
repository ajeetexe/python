from django.db import models
from django.urls import reverse
# Create your models here.
class RegisterStudent(models.Model):
    student_id = models.AutoField(primary_key=True,unique=True) 
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    dob = models.DateField()
    address = models.CharField(max_length=100)
    standard = models.CharField(max_length=5)


    def __str__(self):
        return self.first_name + self.last_name
        print(self.student_id)

    def get_absolute_url(self):
        return reverse("student_home")