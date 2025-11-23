from django import forms
from .models import Owner, Car, DriverLicense

# REMOVE all model classes from this file - they should only be in models.py
# Keep only the form classes:

class OwnerForm(forms.ModelForm):
    class Meta:
        model = Owner
        fields = ['first_name', 'last_name', 'date_of_birth']
        widgets = {
            'first_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter first name'
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter last name'
            }),
            'date_of_birth': forms.DateInput(attrs={
                'type': 'date',
                'class': 'form-control'
            })
        }
        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'date_of_birth': 'Date of Birth'
        }

class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ['license_plate', 'brand', 'model', 'color']
        widgets = {
            'license_plate': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'e.g., ABC123'
            }),
            'brand': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'e.g., Toyota'
            }),
            'model': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'e.g., Camry'
            }),
            'color': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'e.g., Red'
            })
        }
        labels = {
            'license_plate': 'License Plate',
            'brand': 'Brand',
            'model': 'Model',
            'color': 'Color'
        }

class DriverLicenseForm(forms.ModelForm):
    class Meta:
        model = DriverLicense
        fields = ['owner', 'license_number', 'license_type', 'issue_date']
        widgets = {
            'owner': forms.Select(attrs={
                'class': 'form-control'
            }),
            'license_number': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'e.g., AB123456'
            }),
            'license_type': forms.Select(attrs={
                'class': 'form-control'
            }),
            'issue_date': forms.DateInput(attrs={
                'type': 'date',
                'class': 'form-control'
            })
        }
        labels = {
            'owner': 'Owner',
            'license_number': 'License Number',
            'license_type': 'License Type',
            'issue_date': 'Issue Date'
        }