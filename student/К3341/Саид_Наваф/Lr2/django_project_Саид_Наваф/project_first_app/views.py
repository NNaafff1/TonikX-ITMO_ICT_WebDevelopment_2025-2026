from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Owner, Car, Ownership, DriverLicense
from .forms import OwnerForm, CarForm, DriverLicenseForm
# Functional views for Owners
def owner_list(request):
    """Display all owners"""
    owners = Owner.objects.all()
    return render(request, 'project_first_app/owner_list.html', {'owners': owners})

def owner_detail(request, owner_id):
    """Display details of a specific owner"""
    owner = get_object_or_404(Owner, pk=owner_id)
    ownerships = Ownership.objects.filter(owner=owner)
    try:
        driver_license = DriverLicense.objects.get(owner=owner)
    except DriverLicense.DoesNotExist:
        driver_license = None
    
    return render(request, 'project_first_app/owner_detail.html', {
        'owner': owner,
        'ownerships': ownerships,
        'driver_license': driver_license
    })

def create_owner(request):
    if request.method == 'POST':
        form = OwnerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('owner_list')
    else:
        form = OwnerForm()
    return render(request, 'project_first_app/owner_form.html', {'form': form})

def home(request):
    """Home page with navigation"""
    return render(request, 'project_first_app/home.html')

# Class-based views for Cars - update template_name
class CarListView(ListView):
    model = Car
    template_name = 'project_first_app/car_list.html'
    context_object_name = 'cars'

class CarDetailView(DetailView):
    model = Car
    template_name = 'project_first_app/car_detail.html'
    context_object_name = 'car'

class CarCreateView(CreateView):
    model = Car
    form_class = CarForm
    template_name = 'project_first_app/car_form.html'
    success_url = reverse_lazy('car_list')

class CarUpdateView(UpdateView):
    model = Car
    form_class = CarForm
    template_name = 'project_first_app/car_form.html'
    success_url = reverse_lazy('car_list')

class CarDeleteView(DeleteView):
    model = Car
    template_name = 'project_first_app/car_confirm_delete.html'
    success_url = reverse_lazy('car_list')

# Driver License Views - update template_name
class DriverLicenseListView(ListView):
    model = DriverLicense
    template_name = 'project_first_app/driverlicense_list.html'
    context_object_name = 'licenses'

class DriverLicenseDetailView(DetailView):
    model = DriverLicense
    template_name = 'project_first_app/driverlicense_detail.html'
    context_object_name = 'license'

class DriverLicenseCreateView(CreateView):
    model = DriverLicense
    form_class = DriverLicenseForm
    template_name = 'project_first_app/driverlicense_form.html'
    success_url = reverse_lazy('driverlicense_list')

class DriverLicenseUpdateView(UpdateView):
    model = DriverLicense
    form_class = DriverLicenseForm
    template_name = 'project_first_app/driverlicense_form.html'
    success_url = reverse_lazy('driverlicense_list')

class DriverLicenseDeleteView(DeleteView):
    model = DriverLicense
    template_name = 'project_first_app/driverlicense_confirm_delete.html'
    success_url = reverse_lazy('driverlicense_list')