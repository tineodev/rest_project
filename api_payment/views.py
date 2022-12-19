from django.shortcuts import render

# Create your views here.

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

from .models import Payments
from .serializers import PaymentsSerializer

from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser

class Get_Payments(APIView):
    def get_permissions(self):
        if self.request.method == 'GET':
            return [AllowAny()]
        elif self.request.method == 'POST':
            return [IsAuthenticated()]
        return [AllowAny()]


    def get(self, request):
        query = Payments.objects.all()
        serializer = PaymentsSerializer(query, many=True)
        return Response({
            "ok":True,
            "data": serializer.data
        })


    def post(self, request):
        serializer = PaymentsSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({
                    "ok":True,
                "message":"pm_message"
            }, status=status.HTTP_201_CREATED)

        return Response({
            "ok":False,
            "message": serializer.errors
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

