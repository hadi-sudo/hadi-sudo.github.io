from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('smartphone', views.smartphone_data,name='smartphone'),
    path('smartphone/mark', views.smartphone_mark,name='smartphone_mark'),

]
