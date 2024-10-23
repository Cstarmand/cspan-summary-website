from datetime import datetime
import json
import os, ast
from .transcript_retrieval_functions import *
from .claude import *
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import render

def check_new_sessions():
    #first get the json files for senate and house sessions
    f = open('senate_data_backup.json', 'r')
    s = f.read()
    old_senate_sessions = [json.loads(i) for i in json.loads(s)]
    f.close()

    f = open('house_data_updated_backup.json', 'r')
    s = f.read()
    old_house_sessions = [json.loads(i) for i in json.loads(s)]
    f.close()
    
    #now get the current list of house sessions
    raw_house_sessions = get_session_list_house()
    dict_house_sessions = dictify_session_list(raw_house_sessions)
    
    missing_house_sessions = []
    #goes through each session in our list of current sessions
    for i in dict_house_sessions:
        #set a flag to see if it appears in a list of old sessions
        in_list = False
        #do a binary search of the old sessions to find a duplicate
        j = len(old_house_sessions)-1
        x = 0
        end = None
        
        while j >= x:
            #if the id isn't -1 (some of them don't have IDs) then it goes and checks if the id is the same 
            #and if it is it sets things to true and ends the loop
            if (i['id'] != -1 and i['id'] == old_house_sessions[j]['id']) or (i['id'] != -1 and i['id'] == old_house_sessions[x]['id']):
                in_list = True
                break
            elif i['id'] == -1:
                in_list = True
                break
            j -= 1
            x += 1
        if in_list == False:
            missing_house_sessions.append(i)

    #now get the current list of house sessions
    raw_senate_sessions = get_session_list_senate()
    dict_senate_sessions = dictify_session_list(raw_senate_sessions)

    missing_senate_sessions = []
    for i in dict_senate_sessions:
        #set a flag to see if it appears in a list of old sessions
        in_list = False
        #do a binary search of the old sessions to find a duplicate
        j = len(old_senate_sessions)-1
        x = 0
        end = None
        
        while j >= x:
            #if the id isn't -1 (some of them don't have IDs) then it goes and checks if the id is the same 
            #and if it is it sets things to true and ends the loop
            if (i['id'] != -1 and i['id'] == old_senate_sessions[j]['id']) or (i['id'] != -1 and i['id'] == old_senate_sessions[x]['id']):
                in_list = True
                break
            elif i['id'] == -1:
                in_list = True
                break
            j -= 1
            x += 1
        if in_list == False:
            missing_senate_sessions.append(i)

    #upload house and senate json
    old_house_sessions = old_house_sessions + missing_house_sessions
    f = open('house_data_updated_backup.json', 'w')
    f.write(str(json.dumps([json.dumps(i) for i in old_house_sessions])))
    f.close()

    old_senate_sessions = old_senate_sessions + missing_senate_sessions
    f = open('senate_data_backup.json', 'w')
    f.write(str(json.dumps([json.dumps(i) for i in old_senate_sessions])))
    f.close()
