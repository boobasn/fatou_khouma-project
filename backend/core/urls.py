from django.urls import path
from .views import DeviceListCreate, DeviceDetail


urlpatterns = [
    path('devices/', DeviceListCreate.as_view()),
    path('devices/<int:pk>/', DeviceDetail.as_view()),
]
