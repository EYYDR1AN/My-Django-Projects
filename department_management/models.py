from django.db import models


class Department(models.Model):
    department_code = models.CharField(max_length=10, unique=True)
    department_name = models.CharField(max_length=200)
    department_head = models.CharField(max_length=200)
    office_location = models.CharField(max_length=200)
    date_established = models.DateField()

    def __str__(self):
        return self.department_name
