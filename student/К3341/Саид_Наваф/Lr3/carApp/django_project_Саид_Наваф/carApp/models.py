from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

class Owner(models.Model):
    # Автовладелец
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)  # optional

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.last_name} {self.first_name}"


class DriverLicense(models.Model):
    # Удостоверение водителя — OneToOne с Owner
    owner = models.OneToOneField(Owner, on_delete=models.CASCADE, related_name="driver_license")
    license_number = models.CharField(max_length=50, unique=True)
    license_type = models.CharField(max_length=20, blank=True)
    issue_date = models.DateField()

    def __str__(self):
        return f"{self.license_number} ({self.owner})"


class Car(models.Model):
    # Автомобиль
    make = models.CharField(max_length=100)    # Марка, e.g. Toyota
    model = models.CharField(max_length=100)   # Модель
    color = models.CharField(max_length=50, blank=True, null=True)
    vin = models.CharField(max_length=50, unique=True)
    reg_number = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return f"{self.make} {self.model} ({self.reg_number or self.vin})"


class Ownership(models.Model):
    # Ассоциативная сущность — владение (owner <-> car) с датами
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE, related_name="ownerships")
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name="ownerships")
    date_start = models.DateField()
    date_end = models.DateField(null=True, blank=True)  # null => current ownership

    class Meta:
        unique_together = ("owner", "car", "date_start")
        ordering = ["-date_start"]

    def clean(self):
        # Validate: for the same owner+car, date ranges must not overlap
        if self.date_end is not None and self.date_end < self.date_start:
            raise ValidationError({"date_end": _("date_end must be after date_start")})

        qs = Ownership.objects.filter(owner=self.owner, car=self.car).exclude(pk=self.pk)
        for other in qs:
            # other interval: [other.date_start, other.date_end or +inf)
            a1 = self.date_start
            a2 = self.date_end or None
            b1 = other.date_start
            b2 = other.date_end or None

            # intervals overlap if start <= other_end and other_start <= end (with None treated as +inf)
            def le_or_inf(x, y):
                if y is None:
                    return True
                if x is None:
                    return False
                return x <= y

            # Check overlap
            end_a = a2
            end_b = b2
            if (a2 is None and b2 is None):
                overl = True
            elif a2 is None:
                overl = not (b2 < a1)
            elif b2 is None:
                overl = not (a2 < b1)
            else:
                overl = not (a2 < b1 or b2 < a1)

            if overl:
                raise ValidationError(
                    _("Ownership period overlaps with existing ownership (id=%(id)s): %(s)s - %(e)s") % {
                        "id": other.pk,
                        "s": other.date_start,
                        "e": other.date_end or "present"
                    }
                )

    def save(self, *args, **kwargs):
        
        self.clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.owner} -> {self.car}: {self.date_start} - {self.date_end or 'present'}"