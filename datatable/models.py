from django.db import models

# Create your models here.
class Companies(models.Model):
    company_name = models.CharField(max_length=255)
    company_location = models.CharField(max_length=255)
    employee_no = models.IntegerField()
    valuation_in_dollars = models.DecimalField(max_digits=10, decimal_places=2)