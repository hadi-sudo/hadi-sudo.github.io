import ast
from django.http.response import JsonResponse
from rest_framework import serializers 
from .models import *
import json
import re
import ast

class SmartPhoneSerializer():
    def __init__(self) -> None:
        pass

    def get_tunisianet(self):
        sites = ['jumia','tunisianet']
        Phones = list()
        for site in sites:
            File = open(f'.\e-shop\{site}.txt','r')
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
            if (prix.find(".")!=-1):
                prix.replace(',','')
                t = prix.find(".")
                return int(prix[0:t].replace(',',''))
            t = prix.find(",")
            return int(prix[0:t].replace(' ',''))
        p = sorted(Phones,key = lambda phone:price(phone['price']))
        return p


    def get_phone(self):
        #,'jumia','mytek','tunisianet'
        Sites= ['spacenet','tryandbuy','wiki','tunisiatech']
        Phones = list()
        for site in Sites:
            File = open('.\e-shop\{}.txt'.format(site),'r',encoding="utf8")
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
        marks = list()
        with open('A:\python\web shop\phone bot\e-shop\marks.txt','r') as file:
            data = file.readlines()
            data = [ d.replace('\n','') for d in data ]
            file.close()
        return data

