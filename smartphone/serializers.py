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

    def get_phone_special(self):
        base_dir =settings.MEDIA_ROOT    
        sites = ['jumia','tunisianet',"zoom"]
        Phones = list()
        for site in sites:
            my_file = os.path.join(base_dir, str(site))
            File = open(f'{base_dir}/smartphones/{site}.txt','r')
            des = open(f'{base_dir}/smartphones/des_{site}.txt','r',encoding="utf8")
            descp  = des.readlines()
            data = File.read()
            data = data.split('\n')
            data.remove('')
            data = [ i.split("#") for i in data]
            for n in data:
                test = dict()
                for i in n:
                    m = i.split('+')
                    test[m[0]]=m[1]
                test["description"]=descp[data.index(n)]
                Phones.append(test)
            File.close()
            des.close()
        def price(prix):
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
        Sites= ['spacenet','wiki','mytek','tunisiatech','affariyet','tryandbuy']
        Phones = list()
        for site in Sites:
            File = open(f'{base_dir}/smartphones/{site}.txt','r',encoding="utf8")
            des = open(f'{base_dir}/smartphones/des_{site}.txt','r',encoding="utf8")
            descp  = des.readlines()
            data = File.readlines()
            data = [ d.replace('\n','') for d in data ]
            data = [ d.replace(' ','') for d in data ]
            data = [ d.replace("'", '"') for d in data ]
            data = [ json.loads(i) for i in data]
            for i in data:
                 i["description"]=descp[data.index(i)] 
            Phones+=data
            des.close()
        File.close()
        return Phones

    def get_mark(self,ty_):
        base_dir =settings.MEDIA_ROOT
        marks = list()
        with open(f'{base_dir}/{ty_}/marks.txt','r') as file:
            data = file.readlines()
            data = [ d.replace('\n','') for d in data ]
            file.close()
        return data

    def get_laptop(self):
        base_dir =settings.MEDIA_ROOT
        #,'jumia','mytek','tunisianet','tryandbuy','tunisiatech','affariyet'
        Sites= ['spacenet','wiki','mytek','tryandbuy']
        laptops = list()
        for site in Sites:
            File = open(f'{base_dir}/laptop/{site}.txt','r',encoding="utf8")
            des = open(f'{base_dir}/laptop/des_{site}.txt','r',encoding="utf8")
            descp  = des.readlines()
            data = File.readlines()
            data = [ d.replace('\n','') for d in data ]
            data = [ d.replace(' ','') for d in data ]
            data = [ d.replace("'", '"') for d in data ]
            data = [ json.loads(i) for i in data]
            for i in data:
                 i["description"]=descp[data.index(i)] 
            laptops+=data
            des.close()
        File.close()
        return laptops

    def get_laptop_special(self):
        base_dir =settings.MEDIA_ROOT    
        sites = ['jumia','tunisianet',"zoom",'tunisiatech','affariyet']
        laptops = list()
        for site in sites:
            my_file = os.path.join(base_dir, str(site))
            File = open(f'{base_dir}/laptop/{site}.txt','r')
            des = open(f'{base_dir}/laptop/des_{site}.txt','r',encoding="utf8")
            descp  = des.readlines()
            data = File.read()
            data = data.split('\n')
            if "" in data:
                data.remove('')
            if " " in data:
                data.remove(' ')
            data = [ i.split("#") for i in data]
            for n in data:
                test = dict()
                for i in n:
                    try:
                        m = i.split('+')
                        test[m[0]]=m[1]
                    except Exception:
                        continue
                test["description"]=descp[data.index(n)]
                if test["price"]!="":
                    laptops.append(test) 
            File.close()
            des.close()
        return laptops
