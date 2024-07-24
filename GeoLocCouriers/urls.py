from GeoLocCouriers import views
from django.urls import path

app_name = 'GeoLocCouriers'

urlpatterns = [
    path('save_location/', views.save_location, name='save_location'),
    path('', views.CreateTestOrder, name = 'CreateTestOrder'),
    path('GetDataCouriers/', views.GetDataCouriers, name = 'GetDataCouriers'),
    # path('', views.location_page, name='location_page'),
    path('geoloc/', views.geolocation, name='geolocation'),
]
