from datetime import datetime

from django.db import models


# Create your models here.


class District(models.Model):
    district_name = models.CharField(max_length=100)
    district_status = models.BooleanField(default=False)
    district_created_date = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.district_name


class Species_Category(models.Model):
    district_name = models.ForeignKey(District, on_delete=models.CASCADE, default=True, null=False)
    species_category_name = models.CharField(max_length=100)
    species_category_status = models.BooleanField(default=False)
    species_category_created_date = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.species_category_name


class Species(models.Model):
    district_name = models.ForeignKey(District, on_delete=models.CASCADE, default=True, null=False)
    species_category_name = models.ForeignKey(Species_Category, on_delete=models.CASCADE, default=True, null=False)
    species_name = models.CharField(max_length=100)
    species_quantity = models.CharField(max_length=100)
    species_sub_quantity = models.CharField(max_length=100)
    species_date = models.DateField()
    species_depots = models.CharField(max_length=100)
    species_address_line_1 = models.CharField(max_length=100)
    species_address_line_2 = models.CharField(max_length=100)
    species_phone_number = models.CharField(max_length=100)
    species_email = models.EmailField()
    species_status = models.BooleanField(default=False)
    species_created_date = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.species_name
