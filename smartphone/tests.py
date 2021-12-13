from typing import List
from django.test import TestCase
import json

# Create your tests here.
ch ="A:\python\web shop\phone bot\e-shop\jumia.txt"
f = open("A:\python\web shop\phone bot\e-shop\jumia.txt","r")
with open(ch) as f:
    h = list()
    t = f.read()
    t = t.split('\n')
    t.remove("")
    b = [ i.split("#") for i in t]
    for n in b:
        d = dict()
        for i in n:
            m = i.split('+')
            d[m[0]]=m[1]
        h.append(d)
    print(h)
    
    
    
    
    # print(params)
    # print([json.loads(i) for i in t])


# newConditions = {"con1":40, "con2":20, "con3":99, "con4":40, "password":"1234"} 
# params = json.dumps(newConditions).encode('utf8')
# print(json.loads(params))