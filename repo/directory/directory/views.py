from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages
import json
import os
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
    #Pulling data from respective json files
    with open(os.path.join(os.path.dirname(__file__), "house_data_summaries.json"), 'r') as info:
        house_all_data = json.load(info)
    with open(os.path.join(os.path.dirname(__file__), "senate_data_summaries.json"), 'r') as info:
        senate_all_data = json.load(info)

    for x in range(len(house_all_data)):
        house_all_data[x] = ast.literal_eval(house_all_data[x])
    for x in range(len(senate_all_data)):
        senate_all_data[x] = ast.literal_eval(senate_all_data[x])

    data = {'house':house_all_data,'senate':senate_all_data}

    #data['house'] = house_all_data
    #data['senate'] = senate_all_data

    committees = []
    for x in range(len(data['house'])):
        if house_all_data[x]['committee'] not in committees:
            committees.append(house_all_data[x]['committee'])
    for x in range(len(data['senate'])):
        if senate_all_data[x]['committee'] not in committees:
            committees.append(senate_all_data[x]['committee'])
    
    return render(request, 'home/home.html', {"data":data,"committees":committees})
    
def resultPage(request, format=None):
    if request.method == "POST":
        data = {}
        #Pulling data from respective json files
        with open(os.path.join(os.path.dirname(__file__), "house_data_summaries.json"), 'r') as info:
            house_all_data = json.load(info)
        with open(os.path.join(os.path.dirname(__file__), "senate_data_summaries.json"), 'r') as info:
            senate_all_data = json.load(info)

        for x in range(len(house_all_data)):
            house_all_data[x] = ast.literal_eval(house_all_data[x])
        for x in range(len(senate_all_data)):
            senate_all_data[x] = ast.literal_eval(senate_all_data[x])

        data = {'house':house_all_data,'senate':senate_all_data}

        #data['house'] = house_all_data
        #data['senate'] = senate_all_data

        committees = []
        for x in range(len(data['house'])):
            if house_all_data[x]['committee'] not in committees:
                committees.append(house_all_data[x]['committee'])
        for x in range(len(data['senate'])):
            if senate_all_data[x]['committee'] not in committees:
                committees.append(senate_all_data[x]['committee'])

        ret = []
        searched = request.POST.get('q2', '')
        for x in range(len(data['house'])):
            if searched in data['house'][x]['committee']:
                ret.append(data['house'][x])
        for x in range(len(data['senate'])):
            if searched in data['senate'][x]['committee']:
                ret.append(data['senate'][x])
        return render(request, 'result/result.html', {'data': data, 'searched':searched, 'return':ret,'committees':committees})

def searchPage(request, format=None):
    if request.method == "POST":
        data = {}
        #Pulling data from respective json files
        with open(os.path.join(os.path.dirname(__file__), "house_data_summaries.json"), 'r') as info:
            house_all_data = json.load(info)
        with open(os.path.join(os.path.dirname(__file__), "senate_data_summaries.json"), 'r') as info:
            senate_all_data = json.load(info)

        for x in range(len(house_all_data)):
            house_all_data[x] = ast.literal_eval(house_all_data[x])
        for x in range(len(senate_all_data)):
            senate_all_data[x] = ast.literal_eval(senate_all_data[x])

        data = {'house':house_all_data,'senate':senate_all_data}

        #data['house'] = house_all_data
        #data['senate'] = senate_all_data

        committees = []
        for x in range(len(data['house'])):
            if house_all_data[x]['committee'] not in committees:
                committees.append(house_all_data[x]['committee'])
        for x in range(len(data['senate'])):
            if senate_all_data[x]['committee'] not in committees:
                committees.append(senate_all_data[x]['committee'])

        ret = []
        searched = request.POST.get('q1', '')
        for x in range(len(data['house'])):
            if searched.lower() in data['house'][x]['title'].lower():
                ret.append(data['house'][x])
        for x in range(len(data['senate'])):
            if searched.lower() in data['senate'][x]['title'].lower():
                ret.append(data['senate'][x])
        return render(request, 'search/search.html', {'data': data, 'searched':searched, 'return':ret,'committees':committees})


def summaryPage(request, id, format=None):
    # id is a string value that matches the id provided from congress.gov
    data = {}
    #Pulling data from respective json files
    with open(os.path.join(os.path.dirname(__file__), "house_data_summaries.json"), 'r') as info:
        house_all_data = json.load(info)
    with open(os.path.join(os.path.dirname(__file__), "senate_data_summaries.json"), 'r') as info:
        senate_all_data = json.load(info)

    for x in range(len(house_all_data)):
        house_all_data[x] = ast.literal_eval(house_all_data[x])
    for x in range(len(senate_all_data)):
        senate_all_data[x] = ast.literal_eval(senate_all_data[x])

    data = {'house':house_all_data,'senate':senate_all_data}

    #data['house'] = house_all_data
    #data['senate'] = senate_all_data

    committees = []
    for x in range(len(data['house'])):
        if house_all_data[x]['committee'] not in committees:
            committees.append(house_all_data[x]['committee'])
    for x in range(len(data['senate'])):
        if senate_all_data[x]['committee'] not in committees:
            committees.append(senate_all_data[x]['committee'])

    check = True
    if check == True: 
        for x in range(len(house_all_data)):
            if house_all_data[x]['title'] == id:
                data = house_all_data[x]
                check = False
    if check == True: 
        for x in range(len(senate_all_data)):
            if senate_all_data[x]['title'] == id:
                data = senate_all_data[x]
                check = False
    if check == True:
        data = {'title':'invalid id','id':id,'transcript':'','date':'','committee':''}
    return render(request, 'summary/summary.html', {'data': data, 'committees':committees})
    
def aboutPage(request, format=None):
    # id is a string value that matches the id provided from congress.gov
    data = {}
    #Pulling data from respective json files
    with open(os.path.join(os.path.dirname(__file__), "house_data_summaries.json"), 'r') as info:
        house_all_data = json.load(info)
    with open(os.path.join(os.path.dirname(__file__), "senate_data_summaries.json"), 'r') as info:
        senate_all_data = json.load(info)

    for x in range(len(house_all_data)):
        house_all_data[x] = ast.literal_eval(house_all_data[x])
    for x in range(len(senate_all_data)):
        senate_all_data[x] = ast.literal_eval(senate_all_data[x])

    data = {'house':house_all_data,'senate':senate_all_data}

    #data['house'] = house_all_data
    #data['senate'] = senate_all_data

    committees = []
    for x in range(len(data['house'])):
        if house_all_data[x]['committee'] not in committees:
            committees.append(house_all_data[x]['committee'])
    for x in range(len(data['senate'])):
        if senate_all_data[x]['committee'] not in committees:
            committees.append(senate_all_data[x]['committee'])
    
    return render(request, 'about/about.html', {'committees':committees})

def signup(request, format=None):

    if request.method == 'POST':
        username = request.POST.get('username')
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm = request.POST.get('confirm')

        myuser = User.objects.create(username, email, password)
        myuser.first_name = firstname
        myuser.last_name = lastname

        myuser.save()
        messages.success(request, "Your Account has successfully been created.")
        return redirect('signin')

        return

    return render(request, 'signup/signup.html')

def signin(request, format=None):
    
    return render(request, 'signin/signin.html')

def signout(request, format=None):
    
    pass

# No posting functionality needed as homepage and get requests should function
# @api_view(['POST'])

# def postSummary(request, format=None):
#     #filler so we don't have an error
#     print("also test")