from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    date_joined = models.DateField()

    def __str__(self):
        return self.name
