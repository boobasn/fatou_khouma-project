from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets
from .models import Device
from .serializers import DeviceSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import AllowAny
def status(request):
    return JsonResponse({'status':'ok'})




class DeviceViewSet(viewsets.ModelViewSet):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer
    permission_classes = [AllowAny] 
