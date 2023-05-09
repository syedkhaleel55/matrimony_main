from django.http import Http404
from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import *
from .serializers import *

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class EducationDetailList(APIView):
    def get(self, request, format=None):
        Education = EducationDetail.objects.all()
        serializer = EducationDetailSerializer(Education, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = EducationDetailSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class EducationDetailview(APIView):
    def get_object(self, pk):
        try:
            return EducationDetail.objects.get(pk=pk)
        except EducationDetail.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        EducationDetail = self.get_object(pk)
        serializer = EducationDetailSerializer(EducationDetail)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        EducationDetail = self.get_object(pk)
        serializer = EducationDetailSerializer(EducationDetail, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        EducationDetail = self.get_object(pk)
        EducationDetail.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)