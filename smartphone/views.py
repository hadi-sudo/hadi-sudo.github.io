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
        data1 = SmartPhoneSerializer().get_tunisianet()
        phone = data1 +data
        def price(prix,phone):
            if ("\u202f" in prix):
                prix =prix.replace('\u202f','')
            if (prix.find(".")!=-1):
                prix.replace(',','')
                t = int(prix.find("."))
                return int(prix[0:t].replace(',',''))
            t = prix.find(",")
            return int(prix[0:t].replace(' ',''))
        p = sorted(
            phone,
            key = lambda phone:price(phone['price'],phone["name"]))

        return Response(p)

    
@api_view(['GET'])
def smartphone_mark(request):
    if request.method=='GET':
        smartphone = SmartPhone.objects.all()
        data = SmartPhoneSerializer().get_mark()
        return Response(data)
