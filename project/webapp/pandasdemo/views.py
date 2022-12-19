from django.shortcuts import render
import mimetypes
import os
from django.http.response import HttpResponse
from django.views import View
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import*
import pandas as pd
import json

# Create your views here.


class main():
    def home(request):
        item = Orders.objects.all().values()
        df = pd.DataFrame(item)
        # data1 = pd.read_csv('output.csv')
        # df1 = pd.DataFrame(data1)
        mydict = {
            "df": df.to_html()
        }
        return render(request, 'index.html', context=mydict)

    def csv_del(request):
        item = Orders.objects.all().values()
        df = pd.DataFrame(item)
        df1 = df.drop_duplicates(
            subset=['id_order', 'client_name', 'client_surname', 'order_date', 'price'])
        df1.to_csv("output.csv")
        f = open('output.csv', 'rb')
        response = HttpResponse(
            f, content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        response['Content-Disposition'] = 'attachment; filename="Orders.csv"'
        return(response)

    def csv_bef(request):
        item = Orders.objects.all().values()
        df = pd.DataFrame(item)
        df.to_csv("output0.csv")
        f = open('output0.csv', 'rb')
        response = HttpResponse(
            f, content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        response['Content-Disposition'] = 'attachment; filename="Orders.csv"'
        return(response)


class pandasdemo_view(APIView):
    def get(self, request):
        k = {}
        data = pd.read_csv('output.csv')
        # data1 = pd.read_csv('output.csv')
        df = pd.DataFrame(data)
        # df1 = pd.DataFrame(data1)
        a = df.to_dict()
        # a['del'] = df1.to_dict()
        k['zadacha'] = a
        return Response(k)
