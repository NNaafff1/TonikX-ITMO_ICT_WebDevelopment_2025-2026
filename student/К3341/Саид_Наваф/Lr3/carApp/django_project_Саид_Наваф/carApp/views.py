from rest_framework import generics
from .models import Owner, Car, DriverLicense, Ownership
from .serializers import (
    OwnerListSerializer, OwnerCreateUpdateSerializer,
    CarSerializer, DriverLicenseSerializer,
    OwnershipCreateSerializer
)
from rest_framework.response import Response
from rest_framework import status

# Owners

class OwnerListCreateAPIView(generics.ListCreateAPIView):
    queryset = Owner.objects.all().prefetch_related("ownerships__car").select_related("driver_license")
    def get_serializer_class(self):
        if self.request.method == "POST":
            return OwnerCreateUpdateSerializer
        return OwnerListSerializer

class OwnerRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Owner.objects.all().prefetch_related("ownerships__car").select_related("driver_license")
    def get_serializer_class(self):
        if self.request.method in ("PUT", "PATCH"):
            return OwnerCreateUpdateSerializer
        return OwnerListSerializer

# Cars

class CarListCreateAPIView(generics.ListCreateAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer

class CarRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer

# DriverLicense endpoints (optional)

class DriverLicenseListCreateAPIView(generics.ListCreateAPIView):
    queryset = DriverLicense.objects.all()
    serializer_class = DriverLicenseSerializer

class DriverLicenseRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = DriverLicense.objects.all()
    serializer_class = DriverLicenseSerializer

# Ownership creation endpoint (optional helper)
class OwnershipCreateAPIView(generics.CreateAPIView):
    queryset = Ownership.objects.all()
    serializer_class = OwnershipCreateSerializer