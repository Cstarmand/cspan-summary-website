from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import render
from data import *

@api_view(['GET'])

# def getData(request, format=None):
#     if request.method == 'GET':
#         #filler so we don't have an error
#         data = CSPANdata.objects.all()
#         #get data from website scraper
#         #send to Claude
#         #postSummary()
#         return render(request, 'result/result.html', {'data': data})

def homePage(request, format=None):
    if request.method == 'GET':
        data = pull_summary()
        return render(request, 'home/home.html', {'data': data})
    
def summaryPage(request, id, format=None):
    # id is a string value that matches the id provided from congress.gov
    if request.method == 'GET':
        data = pull_summary()
        return render(request, 'summary/summary.html', {'data': data, 'id': id})
    
def aboutPage(request, format=None):
    if request.method =='GET':
        return render(request, 'about/about.html')

# No posting functionality needed as homepage and get requests should function
# @api_view(['POST'])

# def postSummary(request, format=None):
#     #filler so we don't have an error
#     print("also test")