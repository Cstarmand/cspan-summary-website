from django.http import JsonResponse
from .models import CSPANdata
from .serializer import CSPANSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import render

@api_view(['GET'])

def getData(request, format=None):
    if request.method == 'GET':
        #filler so we don't have an error
        data = CSPANdata.objects.all()
        #get data from website scraper
        #send to Claude
        #postSummary()
        return render(request, 'result/result.html', {'data': data})

@api_view(['POST'])

def postSummary(request, format=None):
    #filler so we don't have an error
    print("also test")