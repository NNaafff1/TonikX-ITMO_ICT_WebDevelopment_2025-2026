from django.urls import path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView
from . import views

app_name = "carApp"

urlpatterns = [
    # Owners
    path("owners/", views.OwnerListCreateAPIView.as_view(), name="owners-list-create"),
    path("owners/<int:pk>/", views.OwnerRetrieveUpdateDestroyAPIView.as_view(), name="owners-detail"),
    # Cars
    path("cars/", views.CarListCreateAPIView.as_view(), name="cars-list-create"),
    path("cars/<int:pk>/", views.CarRetrieveUpdateDestroyAPIView.as_view(), name="cars-detail"),
    # Licenses (optional)
    path("licenses/", views.DriverLicenseListCreateAPIView.as_view(), name="licenses-list-create"),
    path("licenses/<int:pk>/", views.DriverLicenseRetrieveUpdateDestroyAPIView.as_view(), name="licenses-detail"),
    # Ownership create helper
    path("ownerships/create/", views.OwnershipCreateAPIView.as_view(), name="ownership-create"),
    


    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path("api/docs/swagger/", SpectacularSwaggerView.as_view(url_name="schema"), name="swagger-ui"),
    path("api/docs/redoc/", SpectacularRedocView.as_view(url_name="schema"), name="redoc"),
]