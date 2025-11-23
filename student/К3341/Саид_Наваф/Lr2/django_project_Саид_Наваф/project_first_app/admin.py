from django.contrib import admin
from .models import Owner, Car, Ownership # Import your models

# Register your models here.
admin.site.register(Owner)
admin.site.register(Car)
admin.site.register(Ownership)