from django.http import Http404
from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import *
from .serializers import *

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class FamilydetailsList(APIView):
    def get(self, request, format=None):
        Family = Familydetails.objects.all()
        serializer = FamilydetailsSerializer(Family, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = FamilydetailsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Familydetailsview(APIView):
    def get_object(self, pk):
        try:
            return Familydetails.objects.get(pk=pk)
        except Familydetails.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        Familydetails = self.get_object(pk)
        serializer = FamilydetailsSerializer(Familydetails)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        Familydetails = self.get_object(pk)
        serializer = FamilydetailsSerializer(Familydetails, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        Familydetails = self.get_object(pk)
        Familydetails.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)