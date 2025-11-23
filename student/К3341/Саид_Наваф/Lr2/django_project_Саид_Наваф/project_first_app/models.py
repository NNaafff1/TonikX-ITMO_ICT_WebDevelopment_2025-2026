from django.db import models

class Owner(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    date_of_birth = models.DateField(null=True, blank=True)
    
    def str(self):
        return f"{self.first_name} {self.last_name} (ID: {self.id})"

class Car(models.Model):
    license_plate = models.CharField(max_length=10, unique=True)
    brand = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    color = models.CharField(max_length=30, blank=True)
    
    # Many-to-many relationship through Ownership
    owners = models.ManyToManyField(Owner, through='Ownership')
    
    def str(self):
        return f"{self.brand} {self.model} - {self.license_plate}"

class Ownership(models.Model):
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    
    def str(self):
        return f"{self.owner} - {self.car} ({self.start_date} to {self.end_date})"

class DriverLicense(models.Model):
    # License types
    LICENSE_TYPES = [
        ('A', 'Type A - Motorcycles'),
        ('B', 'Type B - Cars'),
        ('C', 'Type C - Trucks'),
        ('D', 'Type D - Buses'),
    ]
    
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
    license_number = models.CharField(max_length=10, unique=True)
    license_type = models.CharField(max_length=10, choices=LICENSE_TYPES)
    issue_date = models.DateField()
    
    def __str__(self):
        return f"{self.license_number} - {self.owner}"