import ast
from django.http.response import JsonResponse
from rest_framework import serializers 
from .models import *
import json
import re
import ast
from django.conf import settings
import os


class SmartPhoneSerializer():
    def __init__(self) -> None:
        pass

    def get_tunisianet(self):
        base_dir =settings.MEDIA_ROOT    
        
        sites = ['jumia','tunisianet',"zoom"]
        Phones = list()
        for site in sites:
            my_file = os.path.join(base_dir, str(site))
            File = open(f'{base_dir}/{site}.txt','r')
            data = File.read()
            data = data.split('\n')
            data.remove('')
            data = [ i.split("#") for i in data]
            for n in data:
                test = dict()
                for i in n:
                    m = i.split('+')
                    test[m[0]]=m[1]
                Phones.append(test)
            File.close()

        def price(prix):
            print(prix)
            if (prix.find(".")!=-1):
                prix.replace(',','')
                t = prix.find(".")
                return int(float(prix[0:t].replace(',','')))
            t = prix.find(",")
            return int(float(prix[0:t].replace(' ','')))
        p = sorted(Phones,key = lambda phone:price(phone['price']))
        return p


    def get_phone(self):
        base_dir =settings.MEDIA_ROOT
        #,'jumia','mytek','tunisianet','tryandbuy'
        Sites= ['spacenet','wiki','mytek','tunisiatech',"affariyet"]
        Phones = list()
        for site in Sites:
            File = open(f'{base_dir}/{site}.txt','r',encoding="utf8")
            data = File.readlines()
            data = [ d.replace('\n','') for d in data ]
            data = [ f"{d.replace(' ','')}" for d in data ]
            data = [ d.replace("'", '"') for d in data ]
            data = [ json.loads(i) for i in data]
            Phones+=data
        File.close()
        # sorted(Phones,key = lambda phone:phone['price'])
        return Phones

    def get_mark(self):
        base_dir =settings.MEDIA_ROOT
        marks = list()
        with open(f'{base_dir}/marks.txt','r') as file:
            data = file.readlines()
            data = [ d.replace('\n','') for d in data ]
            file.close()
        return data


