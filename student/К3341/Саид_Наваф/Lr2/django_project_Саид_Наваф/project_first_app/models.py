from django.db import models

class Owner(models.Model):
    # Example fields for an owner
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    # You can add more fields like passport number, address, etc.

    def str(self):
        return f"{self.first_name} {self.last_name}"

class Car(models.Model):
    # Example fields for a car
    license_plate = models.CharField(max_length=10, unique=True)
    brand = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    color = models.CharField(max_length=30, blank=True) # 'blank=True' means the field is optional in forms.

    def str(self):
        return f"{self.brand} {self.model} ({self.license_plate})"

# This is the associative entity to link Owners and Cars with dates
class Ownership(models.Model):
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True) # 'null=True' for DB, 'blank=True' for form. A car can be currently owned.

    def str(self):
        return f"{self.owner} owned {self.car} from {self.start_date} to {self.end_date}"