from django.shortcuts import render

# Create your views here.

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

from .models import Payments, Payments_expired
from .serializers import PaymentsSerializer, Payments_expiredSerializer

from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser

from rest_framework import viewsets
from .paginations import Paginacion



class Get_Payments(viewsets.ReadOnlyModelViewSet):
    queryset = Payments.objects.all()
    serializer_class = PaymentsSerializer
    pagination_class = Paginacion

    def get_permissions(self):
        if self.request.method == 'GET':
            return [AllowAny()]
        elif self.request.method == 'POST':
            return [AllowAny()]
        return [AllowAny()]


    def post(self, request):        
        serializer = PaymentsSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            payment_date = serializer.data.get('payment_date')
            expiration_date = serializer.data.get('expiration_date')
            amount = serializer.data.get('amount')
            if expiration_date<payment_date:
                request.data['amount_fee']= 0.2*float(amount)
                request.data['payment_id']= serializer.data.get('id')
                print(request.data)
                serializer2 = Payments_expiredSerializer(data=request.data)
                if serializer2.is_valid():
                    serializer2.save()
                    return Response({
                        "ok":True,
                        "message":"Record added",
                        "data 1":serializer.data,
                        "message":"Record added also in Expired Payments",
                        "data 2":serializer2.data
                    }, status=status.HTTP_201_CREATED)

            return Response({
                "ok":True,
                "message":"Record created",
                "data":serializer.data
            }, status=status.HTTP_201_CREATED)

        return Response({
            "ok":False,
            "message": serializer.errors
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


