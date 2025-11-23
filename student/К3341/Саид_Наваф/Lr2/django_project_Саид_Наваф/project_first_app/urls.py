from django.urls import path
from . import views

urlpatterns = [
    # Home page
    path('', views.home, name='home'),
    
    # Owner URLs (Functional views)
    path('owners/', views.owner_list, name='owner_list'),
    path('owners/<int:owner_id>/', views.owner_detail, name='owner_detail'),
    path('owners/create/', views.create_owner, name='create_owner'),
    
    # Car URLs (Class-based views)
    path('cars/', views.CarListView.as_view(), name='car_list'),
    path('cars/<int:pk>/', views.CarDetailView.as_view(), name='car_detail'),
    path('cars/create/', views.CarCreateView.as_view(), name='car_create'),
    path('cars/<int:pk>/update/', views.CarUpdateView.as_view(), name='car_update'),
    path('cars/<int:pk>/delete/', views.CarDeleteView.as_view(), name='car_delete'),
    
    # Driver License URLs (Class-based views)
    path('licenses/', views.DriverLicenseListView.as_view(), name='driverlicense_list'),
    path('licenses/<int:pk>/', views.DriverLicenseDetailView.as_view(), name='driverlicense_detail'),
    path('licenses/create/', views.DriverLicenseCreateView.as_view(), name='driverlicense_create'),
    path('licenses/<int:pk>/update/', views.DriverLicenseUpdateView.as_view(), name='driverlicense_update'),
    path('licenses/<int:pk>/delete/', views.DriverLicenseDeleteView.as_view(), name='driverlicense_delete'),
]