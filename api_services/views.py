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
    def get_permissions(self):
        if self.request.method == 'GET':
            return [AllowAny()]
        elif self.request.method == 'POST':
            return [AllowAny()]
        return [AllowAny()]


    def get(self, request):
        query = Services.objects.all()
        serializer = ServicesSerializer(query, many=True)
        return Response({
            "ok":True,
        "data": serializer.data
        })

    def post(self, request):
        serializer = ServicesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "ok":True,
                "message":"Record added",
                "data":serializer.data
            }, status=status.HTTP_201_CREATED)
            
        return Response({
            "ok":False,
            "message": serializer.errors
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



class Rest_services(APIView):
    def get_permissions(self):
        if self.request.method == 'PUT':
            return [AllowAny()]
        elif self.request.method == 'DELETE':
            return [IsAdminUser()]
        return [AllowAny()]


    def put(self, request,id):
        query = get_object_or_404(Services, id=id)
        serializer = ServicesSerializer(query, data=request.data)

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
        query = get_object_or_404(Services, id=id)
        serializer = ServicesSerializer(query)
        return Response({
			"ok": True,
            "data":serializer.data
        })

    def delete(self, request, id):
        query = get_object_or_404(Services, id=id)
        query.delete()
        return Response({
            "ok":True,
                "message":"Record deleted",
		}, status=status.HTTP_202_ACCEPTED)


