from django.shortcuts import render,get_object_or_404

from .models import *
from django.http import JsonResponse
from django.db.models import Count
from rest_framework.views import APIView
from .serializers import *
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view


# Create your views here.


@api_view(['GET'])
def smartphone_data(request):
    if request.method=='GET':
        phone = list()
        data = SmartPhoneSerializer().get_phone()
        # data1 = SmartPhoneSerializer().get_phone_special()
        phone =data
        def price(prix):
            if ("\u202f" in prix):
                prix =prix.replace('\u202f','')
            if (prix.find(".")!=-1):
                prix.replace(',','')
                t = int(prix.find("."))
                return int(prix[0:t].replace(',',''))
            t = prix.find(",")
            return int(prix[0:t].replace(' ',''))
        try:
            p = sorted(
                phone,
                key = lambda phone:price(phone['price']))
        except Exception as e:
            print(e)
        return Response(p)

    
@api_view(['GET'])
def smartphone_mark(request):
    if request.method=='GET':
        smartphone = SmartPhone.objects.all()
        data = SmartPhoneSerializer()
        data = data.get_mark("smartphones")
        return Response(data)

@api_view(['GET'])
def laptop_mark(request):
    if request.method=='GET':
        laptop = SmartPhone.objects.all()
        data = SmartPhoneSerializer()
        data = data.get_mark("laptop")
        return Response(data)

@api_view(['GET'])
def laptop_data(request):
    if request.method=='GET':
        laptop = list()
        data = SmartPhoneSerializer().get_laptop()
        data1 = SmartPhoneSerializer().get_laptop_special()
        laptop = data1 +data
        def price(prix,phone):
            # print(phone)
            # if ("\â€¯" in prix):
            prix =prix.replace('\u202f','')
            prix = prix.replace('â€¯','')
            if (prix.find(".")!=-1):
                prix.replace(',','')
                t = int(prix.find("."))
                # print(int(float(prix[0:t].replace(',',''))))
                return int(float(prix[0:t].replace(',','')))
            t = prix.find(",")
            # print(int(float(prix[0:t].replace(' ',''))))
            return int(float(prix[0:t].replace(' ','')))
        try:
            laptops = sorted(
                laptop,
                key = lambda laptop:price(laptop['price'],laptop["url"])
                )
        except Exception as e:
            print(f"error {e}")
        return Response(laptops)