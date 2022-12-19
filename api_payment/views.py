from django.shortcuts import render

# Create your views here.

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

from .models import Payments, Payments_expired
from .serializers import PaymentsSerializer, Payments_expiredSerializer

from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser

class Get_Payments(APIView):
    def get_permissions(self):
        if self.request.method == 'GET':
            return [AllowAny()]
        elif self.request.method == 'POST':
            return [AllowAny()]
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
                    return Response({'ok':True})

            return Response({
                "ok":True,
                "message":"Record created",
                "data":serializer.data
            }, status=status.HTTP_201_CREATED)

        return Response({
            "ok":False,
            "message": serializer.errors
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



class Rest_payments(APIView):
    def get_permissions(self):
        if self.request.method == 'PUT':
            return [AllowAny()]
        elif self.request.method == 'DELETE':
            return [AllowAny()]
        return [AllowAny()]


    def put(self, request,id):
        query = get_object_or_404(Payments, id=id)
        serializer = PaymentsSerializer(query, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({
                "ok":True,
                "message":"Record updated",
            })

        return Response({
            "ok": False,
            "message": serializer.errors
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


    def get(self, request, id):
        query = get_object_or_404(Payments, id=id)
        serializer = PaymentsSerializer(query)
        return Response({
			"ok": True,
            "data":serializer.data
        })


    def delete(self, request, id):
        query = get_object_or_404(Payments, id=id)
        query.delete()
        return Response({
            "ok":True,
                "message":"Record deleted",
		}, status=status.HTTP_202_ACCEPTED)
