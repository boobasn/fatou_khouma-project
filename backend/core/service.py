import core.models as models
from core.serializers import DeviceSerializer, SensorSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404

class DeviceListCreateView(APIView):
    def get(self, request):
        devices = models.Device.objects.all()
        serializer = DeviceSerializer(devices, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = DeviceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class SensorReadingList(APIView):
    def get(self, request):
        readings = models.SensorReading.objects.all()
        serializer = SensorSerializer(readings, many=True)
        return Response(serializer.data)

