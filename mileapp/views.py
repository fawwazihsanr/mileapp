from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status

from rest_framework.decorators import api_view
from rest_framework.response import Response

from mileapp.models import Mileapp
from .serializers import MileAppSerializer


# Create your views here.


@api_view(['GET', 'POST'])
def get_package(request):
    if request.method == 'GET':
        get_list = Mileapp.objects.all().values()
        data_return = []
        for data in get_list:
            data_return.append(data)
        return Response(data=data_return, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        new_data = request.data['new_data']
        serializer = MileAppSerializer(data=new_data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response(data={"message": "Created!"}, status=status.HTTP_201_CREATED)


@api_view(['GET', 'DELETE', 'PUT'])
def get_package_details(request, pk):
    if request.method == 'GET':
        try:
            data_return = []
            get_detail = Mileapp.objects.filter(pk=pk).values()
            for data in get_detail:
                data_return.append(data)
            return Response(data=data_return, status=status.HTTP_200_OK)
        except Mileapp.DoesNotExist:
            return Response(data={"message": "data not found"}, status=status.HTTP_404_NOT_FOUND)
    elif request.method == 'DELETE':
        try:
            get_data = Mileapp.objects.get(pk=pk)
            get_data.delete()
            return Response(data={"message": "deleted"}, status=status.HTTP_204_NO_CONTENT)
        except Mileapp.DoesNotExist:
            return Response(data={"message": "data not found"}, status=status.HTTP_404_NOT_FOUND)
    elif request.method == 'PUT':
        try:
            package = Mileapp.objects.get(pk=pk)
            update_data = request.data['update_data']
            serializer = MileAppSerializer(instance=package, data=update_data, partial=True)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(data={"message": "Created!"}, status=status.HTTP_201_CREATED)
        except Mileapp.DoesNotExist:
            return Response(data={"message": "data not found"}, status=status.HTTP_404_NOT_FOUND)









