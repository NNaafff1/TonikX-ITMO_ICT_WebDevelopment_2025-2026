from django.contrib import admin
from .models import Owner, Car, Ownership

@admin.register(Owner)
class OwnerAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'date_of_birth']
    search_fields = ['first_name', 'last_name']

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ['license_plate', 'brand', 'model', 'color']
    search_fields = ['license_plate', 'brand', 'model']

@admin.register(Ownership)
class OwnershipAdmin(admin.ModelAdmin):
    list_display = ['owner', 'car', 'start_date', 'end_date']
    list_filter = ['start_date', 'end_date']