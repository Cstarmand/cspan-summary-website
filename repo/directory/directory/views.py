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
    
def resultPage(request, format=None):
    if request.method == "POST":
        data = pull_summary()
        ret = []
        searched = request.POST('searched')
        for x in range(len(data['house'])):
            if searched in data['house'][x]['committee']:
                ret.append(data['house'][x])
        for x in range(len(data['senate'])):
            if searched in data['senate'][x]['committee']:
                ret.append(data['senate'][x])
        for x in range(len(data['joint'])):
            if searched in data['joint'][x]['committee']:
                ret.append(data['joint'][x])
        return render(request, 'result/result.html', {'data': data, 'searched':searched, 'return':ret})
    else:
        return render(request, 'result/result.html', {'data':'', 'searched':searched, 'return':''})

def searchPage(request, format=None):
    if request.method == "POST":
        data = pull_summary()
        ret = []
        searched = request.POST('searched')
        for x in range(len(data['house'])):
            if searched in data['house'][x]['title']:
                ret.append(data['house'][x])
        for x in range(len(data['senate'])):
            if searched in data['senate'][x]['title']:
                ret.append(data['senate'][x])
        for x in range(len(data['joint'])):
            if searched in data['joint'][x]['title']:
                ret.append(data['joint'][x])
        return render(request, 'search/search.html', {'data': data, 'searched':searched, 'return':ret})
    else:
        return render(request, 'search/search.html', {'data':'', 'searched':searched, 'return':''})

def summaryPage(request, id, format=None):
    # id is a string value that matches the id provided from congress.gov
    if request.method == 'GET':
        data = pull_summary()
        check = True
        if check == True: 
            for x in range(len(data['house'])):
                if data['house'][x]['id'] == id:
                    data = data['house'][x]
                    check = False
        if check == True: 
            for x in range(len(data['senate'])):
                if data['senate'][x]['id'] == id:
                    data = data['senate'][x]
                    check = False
        if check == True: 
            for x in range(len(data['joint'])):
                if data['joint'][x]['id'] == id:
                    data = data['joint'][x]
                    check = False
        if check == True:
            data = {'title':'invalid id','id':id,'transcript':'','summary':'','date':'','committee':''}
        return render(request, 'summary/summary.html', {'data': data, 'id': id})
    
def aboutPage(request, format=None):
    if request.method =='GET':
        return render(request, 'about/about.html')

# No posting functionality needed as homepage and get requests should function
# @api_view(['POST'])

# def postSummary(request, format=None):
#     #filler so we don't have an error
#     print("also test")