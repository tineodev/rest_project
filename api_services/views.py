from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated

from .models import Services
from .serializers import ServicesSerializer


# Create your views here.

from rest_framework import viewsets

class Rest_Services(viewsets.ModelViewSet):
    queryset = Services.objects.all()
    serializer_class = ServicesSerializer
    throttle_scope = 'all'


    def get_permissions(self):
        if self.request.method == 'GET':
            return [AllowAny()]
        return [IsAdminUser()]
