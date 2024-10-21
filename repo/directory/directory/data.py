from datetime import datetime
import json
from .transcript_retrieval_functions import *
from .claude import *

transcript_summaries = {'house':[], 'senate':[], 'joint':[]}

def house_data(house_all_data, combined_data):
    #Place transcripts and id into specific lists

    house_transcripts = []
    house_id = []

    house_sessions = get_session_list_house()

    events = dictify_session_list(house_sessions)

    new_events = []

    for session in events:
        if session['id'] not in combined_data:
            new_events.append(session)

    transcript_and_events = add_transcripts(new_events)

    for x in range(len(transcript_and_events)):
        house_transcripts[x] = transcript_and_events[x]['transcript']
        house_id[x] = transcript_and_events[x]['id']

    return house_transcripts, house_id, transcript_and_events


def senate_data(senate_all_data, combined_data):
    #Place transcripts and id into specific lists
    
    senate_transcripts = []
    senate_id = []

    senate_sessions = get_session_list_senate()

    events = dictify_session_list(senate_sessions)

    new_events = []

    for session in events:
        if session['id'] not in combined_data:
            new_events.append(session)

    transcript_and_events = add_transcripts(new_events)

    for x in range(len(transcript_and_events)):
        senate_transcripts[x] = transcript_and_events[x]['transcript']
        senate_id[x] = transcript_and_events[x]['id']

    return senate_transcripts, senate_id, transcript_and_events


def joint_data(joint_all_data, combined_data):
    #Place transcripts and id into specific lists
    
    joint_transcripts = []
    joint_id = []

    joint_sessions = get_session_list_joint()

    events = dictify_jointsession_list(joint_sessions)

    new_events = []

    for session in events:
        if session['id'] not in combined_data:
            new_events.append(session)

    transcript_and_events = add_transcripts(new_events)

    for x in range(len(transcript_and_events)):
        joint_transcripts[x] = transcript_and_events[x]['transcript']
        joint_id[x] = transcript_and_events[x]['id']

    return joint_transcripts, joint_id, transcript_and_events


# limit updates to daily occurences
def pull_summary():
    #All known ids
    combined_data = []

    #Pull already gathered information from json file
    with open('house_data_ex_transcripts.json', 'r') as file:
        house_all_data = json.load(file)
    with open('senate_data_ex_transcripts.json', 'r') as file:
        senate_all_data = json.load(file)
    with open('joint_data_ex_transcripts.json', 'r') as file:
        joint_all_data = json.load(file)

    #Place already gathered ids into list so repeat generations are not completed
    for x in range(len(house_all_data)):
        combined_data.append(house_all_data[x]['id'])
    for x in range(len(senate_all_data)):
        combined_data.append(senate_all_data[x]['id'])
    for x in range(len(joint_all_data)):
        combined_data.append(joint_all_data[x]['id'])
    
    # Consolidates data
    house_transcripts, house_id, house_all = house_data(house_all_data, combined_data)
    senate_transcripts, senate_id, senate_all = senate_data(senate_all_data, combined_data)
    joint_transcripts, joint_id, joint_all = joint_data(joint_all_data, combined_data)

    # Summarize new transcripts
    for x in range(len(house_id)):
        if house_id[x] not in combined_data:
            summary = claude_summary(house_transcripts[x])
            #transcript_summaries['house'].append(summary)
            house_all[x]['summary'] = summary

    for x in range(len(senate_id)):
        if senate_id[x] not in combined_data:
            summary = claude_summary(senate_transcripts[x])
            #transcript_summaries['senate'].append(summary)
            senate_all[x]['summary'] = summary

    for x in range(len(joint_id)):
        if joint_id[x] not in combined_data:
            summary = claude_summary(joint_transcripts[x])
            #transcript_summaries['joint'].append(summary)
            joint_all[x]['summary'] = summary

    # Remove transcripts from stored information
    house_final = []
    senate_final = []
    joint_final = []
    
    for x in range(len(house_all)):
        house_final[x]['id'] = house_all[x]['id']
        house_final[x]['title'] = house_all[x]['title']
        house_final[x]['date'] = house_all[x]['date']
        house_final[x]['summary'] = house_all[x]['summary']
        house_final[x]['link'] = house_all[x]['link']
        house_final[x]['committee'] = house_all[x]['committee']
    
    for x in range(len(senate_all)):
        senate_final[x]['id'] = senate_all[x]['id']
        senate_final[x]['title'] = senate_all[x]['title']
        senate_final[x]['date'] = senate_all[x]['date']
        senate_final[x]['summary'] = senate_all[x]['summary']
        senate_final[x]['link'] = senate_all[x]['link']
        senate_final[x]['committee'] = senate_all[x]['committee']
    
    for x in range(len(joint_all)):
        joint_final[x]['id'] = joint_all[x]['id']
        joint_final[x]['title'] = joint_all[x]['title']
        joint_final[x]['date'] = joint_all[x]['date']
        joint_final[x]['summary'] = joint_all[x]['summary']
        joint_final[x]['link'] = joint_all[x]['link']
        joint_final[x]['committee'] = joint_all[x]['committee']

    #append new information to json file list
    for item in house_final:
        house_all_data.append(item)

    for item in senate_final:
        senate_all_data.append(item)

    for item in joint_final:
        joint_all_data.append(item)

    #Save data to json files
    with open('house_data_ex_transcripts.json', 'w') as file:
        json.dump(house_all_data, file)
    with open('senate_data_ex_transcripts.json', 'w') as file:
        json.dump(senate_all_data, file)
    with open('joint_data_ex_transcripts.json', 'w') as file:
        json.dump(joint_all_data, file)

    return "Update Complete"