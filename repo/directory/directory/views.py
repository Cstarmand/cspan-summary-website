from django.http import JsonResponse
from .models import CSPANdata
from .serializer import CSPANSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])

def getData(request, format=None):
    if request.method == 'GET':
        #filler so we don't have an error
        print('test')

@api_view(['PUT'])

def postSummary(request, format=None):
    #filler so we don't have an error
    print("also test")