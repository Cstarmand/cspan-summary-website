from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import render
import json
from .data import *

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
    data = {}
    #Pulling data from respective json files
    with open('house_data_ex_transcripts.json', 'r') as file:
        house_all_data = json.load(file)
    with open('senate_data_ex_transcripts.json', 'r') as file:
        senate_all_data = json.load(file)
    with open('joint_data_ex_transcripts.json', 'r') as file:
        joint_all_data = json.load(file)
    
    data['house'] = house_all_data
    data['senate'] = senate_all_data
    data['joint'] = joint_all_data

    committees = []
    for x in range(len(data['house'])):
        if data['house'][x]['committee'] not in committees:
            committees.append(data['house'][x]['committee'])
    for x in range(len(data['senate'])):
        if data['senate'][x]['committee'] not in committees:
            committees.append(data['senate'][x]['committee'])
    for x in range(len(data['joint'])):
        if data['joint'][x]['committee'] not in committees:
            committees.append(data['joint'][x]['committee'])
    
    return render(request, 'home/home.html', {'data': data,'committees':committees})
    
def resultPage(request, format=None):
    if request.method == "POST":
        data = {}
        #Pulling data from respective json files
        with open('house_data_ex_transcripts.json', 'r') as file:
            house_all_data = json.load(file)
        with open('senate_data_ex_transcripts.json', 'r') as file:
            senate_all_data = json.load(file)
        with open('joint_data_ex_transcripts.json', 'r') as file:
            joint_all_data = json.load(file)
        
        data['house'] = house_all_data
        data['senate'] = senate_all_data
        data['joint'] = joint_all_data

        committees = []
        for x in range(len(data['house'])):
            if data['house'][x]['committee'] not in committees:
                committees.append(data['house'][x]['committee'])
        for x in range(len(data['senate'])):
            if data['senate'][x]['committee'] not in committees:
                committees.append(data['senate'][x]['committee'])
        for x in range(len(data['joint'])):
            if data['joint'][x]['committee'] not in committees:
                committees.append(data['joint'][x]['committee'])

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
        return render(request, 'result/result.html', {'data': data, 'searched':searched, 'return':ret,'committees':committees})
    else:
        return render(request, 'result/result.html', {'data':'', 'searched':searched, 'committees':committees,'return':[{'id':'','committee':'','title':'','date':''}]})

def searchPage(request, format=None):
    if request.method == "POST":
        data = {}
        #Pulling data from respective json files
        with open('house_data_ex_transcripts.json', 'r') as file:
            house_all_data = json.load(file)
        with open('senate_data_ex_transcripts.json', 'r') as file:
            senate_all_data = json.load(file)
        with open('joint_data_ex_transcripts.json', 'r') as file:
            joint_all_data = json.load(file)
        
        data['house'] = house_all_data
        data['senate'] = senate_all_data
        data['joint'] = joint_all_data

        committees = []
        for x in range(len(data['house'])):
            if data['house'][x]['committee'] not in committees:
                committees.append(data['house'][x]['committee'])
        for x in range(len(data['senate'])):
            if data['senate'][x]['committee'] not in committees:
                committees.append(data['senate'][x]['committee'])
        for x in range(len(data['joint'])):
            if data['joint'][x]['committee'] not in committees:
                committees.append(data['joint'][x]['committee'])

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
        return render(request, 'search/search.html', {'data': data, 'searched':searched, 'return':ret,'committees':committees})
    else:
        return render(request, 'search/search.html', {'data':'', 'searched':searched, 'committees':committees, 'return':{'id':'','committee':'','title':'','date':''}})

def summaryPage(request, id, format=None):
    # id is a string value that matches the id provided from congress.gov
    data = {}
    #Pulling data from respective json files
    with open('house_data_ex_transcripts.json', 'r') as file:
        house_all_data = json.load(file)
    with open('senate_data_ex_transcripts.json', 'r') as file:
        senate_all_data = json.load(file)
    with open('joint_data_ex_transcripts.json', 'r') as file:
        joint_all_data = json.load(file)
    
    data['house'] = house_all_data
    data['senate'] = senate_all_data
    data['joint'] = joint_all_data

    committees = []
    for x in range(len(data['house'])):
        if data['house'][x]['committee'] not in committees:
            committees.append(data['house'][x]['committee'])
    for x in range(len(data['senate'])):
        if data['senate'][x]['committee'] not in committees:
            committees.append(data['senate'][x]['committee'])
    for x in range(len(data['joint'])):
        if data['joint'][x]['committee'] not in committees:
            committees.append(data['joint'][x]['committee'])

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
    return render(request, 'summary/summary.html', {'data': data, 'id': id, 'committees':committees})
    
def aboutPage(request, format=None):
    return render(request, 'about/about.html')

# No posting functionality needed as homepage and get requests should function
# @api_view(['POST'])

# def postSummary(request, format=None):
#     #filler so we don't have an error
#     print("also test")