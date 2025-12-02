from rest_framework import serializers
from .models import Owner, DriverLicense, Car, Ownership

class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ["id", "make", "model", "color", "vin", "reg_number"]

class DriverLicenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = DriverLicense
        fields = ["id", "license_number", "license_type", "issue_date"]

class OwnershipCarSerializer(serializers.ModelSerializer):
    # nested representation of the car inside ownership
    car = CarSerializer(read_only=True)

    class Meta:
        model = Ownership
        fields = ["id", "car", "date_start", "date_end"]

class OwnershipCreateSerializer(serializers.ModelSerializer):
    # used when creating ownerships (car and owner provided by id)
    class Meta:
        model = Ownership
        fields = ["id", "owner", "car", "date_start", "date_end"]

class OwnerListSerializer(serializers.ModelSerializer):
    # minimal nested info for list endpoints
    driver_license = DriverLicenseSerializer(read_only=True)
    ownerships = OwnershipCarSerializer(many=True, read_only=True)

    class Meta:
        model = Owner
        fields = ["id", "first_name", "last_name", "date_of_birth", "driver_license", "ownerships"]

class OwnerCreateUpdateSerializer(serializers.ModelSerializer):
    # used for create/update: allow nested creation of license optionally
    driver_license = DriverLicenseSerializer(required=False, allow_null=True)

    class Meta:
        model = Owner
        fields = ["id", "first_name", "last_name", "date_of_birth", "driver_license"]

    def create(self, validated_data):
        license_data = validated_data.pop("driver_license", None)
        owner = Owner.objects.create(**validated_data)
        if license_data:
            DriverLicense.objects.create(owner=owner, **license_data)
        return owner

    def update(self, instance, validated_data):
        license_data = validated_data.pop("driver_license", None)
        for attr, val in validated_data.items():
            setattr(instance, attr, val)
        instance.save()
        if license_data is not None:
            # create or update license
            DriverLicense.objects.update_or_create(owner=instance, defaults=license_data)
        return instance