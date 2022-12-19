from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated

from .models import Services
from .serializers import ServicesSerializer

# Create your views here.


class Get_Services(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        query = Services.objects.all()
        serializer = ServicesSerializer(query, many=True)
        return Response({
            "ok":True,
        "data": serializer.data
        })

