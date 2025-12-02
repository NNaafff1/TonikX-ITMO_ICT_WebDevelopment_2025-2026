from django.contrib import admin
from .models import Owner, DriverLicense, Car, Ownership

class OwnershipInline(admin.TabularInline):
    model = Ownership
    extra = 1

@admin.register(Owner)
class OwnerAdmin(admin.ModelAdmin):
    list_display = ("last_name", "first_name")
    inlines = [OwnershipInline]

@admin.register(DriverLicense)
class DriverLicenseAdmin(admin.ModelAdmin):
    list_display = ("license_number", "owner", "issue_date")

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ("make", "model", "reg_number", "vin")
    inlines = [OwnershipInline]

@admin.register(Ownership)
class OwnershipAdmin(admin.ModelAdmin):
    list_display = ("owner", "car", "date_start", "date_end")