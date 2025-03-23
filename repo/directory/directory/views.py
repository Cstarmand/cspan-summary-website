from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from directory import settings
from django.core.mail import send_mail
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from . tokens import generate_token
from django.core.mail import EmailMessage, send_mail
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

        if User.objects.filter(username=username):
            messages.error(request, "Username already in use")
            return redirect('signup/')

        if User.objects.filter(email=email):
            messages.error(request, "Email already in use")
            return redirect('signup/')

        if password != confirm:
            messages.error(request, "Passwords do not match")
            return redirect('signup/')
        
        if not username.isalnum():
            messages.error(request, "Username contains special characters")
            return redirect('signup/')

        myuser = User.objects.create_user(username, email, password)
        myuser.first_name = firstname
        myuser.last_name = lastname
        
        myuser.is_active = False
        myuser.save()
        messages.success(request, "Your Account has successfully been created. We have sent you a confirmation email, please confirm your account to activate it.")

        # Info Email
        subject = "Welcome to DocIt Accounts"
        message = "Hello " + myuser.first_name + "! \n\n" + "Welcome to DocIt!\nThank you for joining the community of informed citizens!\nYou can now add favorite pages to your profile and stay further up to date with government proceedings!\nYou will also recieve a confirmation email. Please confirm your email address to activate your account.\n\nThank You,\nFrom DocIt Team"
        from_email = settings.EMAIL_HOST_USER
        to_list = [myuser.email]
        send_mail(subject, message, from_email, to_list, fail_silently=True)

        # Email Address Confirmation
        current_site = get_current_site(request)
        email_subject = "Confirm Your Email - DocIt"
        email_message = render_to_string('email_confirmation.html', {
            'name':myuser.first_name,
            'domain':current_site.domain,
            'uid':urlsafe_base64_encode(force_bytes(myuser.pk)),
            'token':generate_token.make_token(myuser)
        })
        email = EmailMessage(
            email_subject,
            email_message,
            settings.EMAIL_HOST_USER,
            [myuser.email]
        )
        email.fail_silently = True
        email.send()

        return redirect('home/')

    return render(request, 'signup/signup.html')

def signin(request, format=None):
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            firstname = user.first_name
            return render(request, "home/home.html",  {'firstname':firstname})

        else:
            messages.error(request, "Bad Credentials")
            return redirect('home/')
    
    return render(request, 'signin/signin.html')

def signout(request, format=None):
    logout(request)
    messages.success(request, "You have successfully logged out!")
    return redirect('home/')

def activate(request, uidb64, token, format=None):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        myuser = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        myuser = None
    
    if myuser is not None and generate_token.check_token(myuser, token):
        myuser.is_active = True
        myuser.save()
        login(request, myuser)
        return redirect('home/')
    else:
        return render(request, 'activation_failed.html')

# No posting functionality needed as homepage and get requests should function
# @api_view(['POST'])

# def postSummary(request, format=None):
#     #filler so we don't have an error
#     print("also test")