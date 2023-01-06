
from django.shortcuts import render
from rest_framework import status
from django.shortcuts import render
from rest_framework import generics
import  pandas as pd
from rest_framework.response import Response
from .models import File
from .serializer import FileUploadSerializer,DataSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from tkinter.tix import Tree

class UploadFileView(generics.CreateAPIView):
    serializer_class = FileUploadSerializer
    
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        file = serializer.validated_data['file']
        reader = pd.read_csv(file)
        for _, row in reader.iterrows():
            new_file = File(
                    transaction_date = row['date'],
                    channel = row['channel'],
                    country = row['country'],
                    os = row['os'],
                    impressions = row['impressions'],
                    clicks = row['clicks'],
                    installs = row['installs'],
                    spend = row['spend'],
                    revenue = row['revenue'],
                       )
            new_file.save()
        return Response({"status": "success"}, status = status.HTTP_201_CREATED)
        #http://127.0.0.1:8000/data/upload/

class DataAPIView(APIView):
    
    def get(self,request,format=None):

        sortBy = self.request.query_params.get('sortBy',None)
        orderBy = self.request.query_params.get('orderBy',None)
        sortByField = self.request.query_params.get('sortByField',None)
        operation = self.request.query_params.get('operation',None)
        country = self.request.query_params.get('country',None)
        channel = self.request.query_params.get('channel',None)
        os = self.request.query_params.get('os',None)
        fromDate = self.request.query_params.get('fromDate',None)
        toDate = self.request.query_params.get('toDate',None)
        date = self.request.query_params.get('date',None)
    
        if operation =='all':
            response  = File.objects.all()
            serializer =DataSerializer(response ,many=Tree)
            return Response(serializer.data)
            #http://127.0.0.1:8000/?operation=all   to get all the entries in the database. 




            
 

        