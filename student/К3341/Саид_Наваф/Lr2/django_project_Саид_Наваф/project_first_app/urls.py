from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),

    path('owner/<int:owner_id>/', views.owner_detail, name='owner_detail'),
]