"""
Run from project root:
python populate_lab3_practice3_1.py

Replace DJANGO_SETTINGS_MODULE with your project settings module name if needed.
"""
import os
import django
from datetime import date

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_project_Саид_Наваф.settings")  # <- replace
django.setup()

from carApp.models import Owner, DriverLicense, Car, Ownership

def run():
    # Optional: clear existing test data (uncomment any deletes you want)
    # Ownership.objects.all().delete()
    # DriverLicense.objects.all().delete()
    # Car.objects.all().delete()
    # Owner.objects.all().delete()

    owners_data = [
        ("Ivan", "Ivanov", date(1985, 5, 10)),
        ("Oleg", "Petrov", date(1990, 1, 2)),
        ("Maria", "Sidorova", date(1992, 7, 23)),
        ("Alexey", "Kuznetsov", date(1980, 3, 3)),
        ("Elena", "Vasilieva", date(1988, 11, 11)),
        ("Dmitry", "Smirnov", date(1979, 6, 6)),
        ("Natalia", "Morozova", date(1995, 9, 9)),
    ]
    owners = []
    for idx, (first, last, dob) in enumerate(owners_data, 1):
        o = Owner.objects.create(first_name=first, last_name=last, date_of_birth=dob)
        owners.append(o)
        DriverLicense.objects.create(owner=o, license_number=f"DL{1000+idx}", license_type="B", issue_date=date(2010+idx, 1, 1))

    cars_data = [
        ("Toyota", "Camry", "red", "VIN0001", "A111AA"),
        ("Toyota", "Corolla", "blue", "VIN0002", "B222BB"),
        ("Ford", "Focus", "red", "VIN0003", "C333CC"),
        ("BMW", "X5", "black", "VIN0004", "D444DD"),
        ("Lada", "Granta", "white", "VIN0005", "E555EE"),
        ("Hyundai", "Solaris", "red", "VIN0006", "F666FF"),
    ]
    cars = []
    for make, model, color, vin, reg in cars_data:
        cars.append(Car.objects.create(make=make, model=model, color=color, vin=vin, reg_number=reg))

    # Give each owner 1..3 cars
    base_year = 2010
    for i, owner in enumerate(owners):
        n = (i % 3) + 1
        for j in range(n):
            car = cars[(i + j) % len(cars)]
            ds = date(base_year + i + j, 1, 1)
            de = None if (i + j) % 2 else date(base_year + i + j + 1, 1, 1)
            Ownership.objects.create(owner=owner, car=car, date_start=ds, date_end=de)

    print("Populate done. Owners:", Owner.objects.count(), "Cars:", Car.objects.count(), "Ownerships:", Ownership.objects.count())

if __name__ == "__main__":
    run()