# from django.shortcuts import render

# # Create your views here.
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import CarSerializer
from .models import Car

@api_view(['GET', 'POST'])
def cars_list(request):

    if request.method == "GET":
        cars = Car.objects.all()
        serializer = CarSerializer(cars, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = CarSerializer(data=request.data)
        #the below code is like a short cut to the if statement
        serializer.is_valid(raise_exception=True)
        # if serializer.is_valid() == True:
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
        # else:
        #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT'])
def car_detail(request, pk):

    car = get_object_or_404(Car, pk=pk)
    if request.method == 'GET':
        serializer = CarSerializer(car);
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = CarSerializer(car, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    # try: no longer need try/except for get_list
        # car = Car.objects.get(pk=pk) no longer need this, can use django import      

    # except Car.DoesNotExist:
        # return Response(status=status.HTTP_404_NOT_FOUND)

    # print(pk)
    # return Response(pk)