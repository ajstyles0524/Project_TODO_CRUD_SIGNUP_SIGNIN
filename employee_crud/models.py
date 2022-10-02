from django.db import models


# Create your models here.

class Employee(models.Model):
    E_id = models.CharField(max_length=20)
    E_name = models.CharField(max_length=100)
    E_email = models.EmailField()
    E_contact = models.CharField(max_length=15)

    class Meta:
        db_table = "employee_crud"
