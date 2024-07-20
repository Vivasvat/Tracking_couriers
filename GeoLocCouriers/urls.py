from GeoLocCouriers import views
from django.urls import path

app_name = 'GeoLocCouriers'

urlpatterns = [
    path('', views.GeoLocCouriers, name="GeoLocCouriers"),
]