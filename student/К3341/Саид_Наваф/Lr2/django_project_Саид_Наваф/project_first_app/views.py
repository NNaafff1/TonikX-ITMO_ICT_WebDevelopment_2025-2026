from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Owner

def home(request):
    """Home page with links to all owners"""
    owners = Owner.objects.all()
    return render(request, 'home.html', {'owners': owners})

def owner_detail(request, owner_id):
    owner_obj = get_object_or_404(Owner, pk=owner_id)
    return render(request, 'owner.html', {'owner': owner_obj})