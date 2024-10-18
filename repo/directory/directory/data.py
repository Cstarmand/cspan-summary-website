from datetime import datetime
from transcript_retrieval_functions import *
from claude import *

current_date = datetime.now().date()
stored_date = ''
combined_data = []
transcript_summaries = {'house':[], 'senate':[], 'joint':[]}
all_data = {}

def house_data():
    #Place transcripts and id into specific lists

    house_transcripts = []
    house_id = []

    house_sessions = get_session_list_house()

    events = dictify_session_list(house_sessions)

    transcript_and_events = add_transcripts(events)

    for x in range(len(transcript_and_events)):
        house_transcripts[x] = transcript_and_events[x]['transcript']
        house_id[x] = transcript_and_events[x]['id']

    return house_transcripts, house_id, transcript_and_events


def senate_data():
    #Place transcripts and id into specific lists
    
    senate_transcripts = []
    senate_id = []

    senate_sessions = get_session_list_senate()

    events = dictify_session_list(senate_sessions)

    transcript_and_events = add_transcripts(events)

    for x in range(len(transcript_and_events)):
        senate_transcripts[x] = transcript_and_events[x]['transcript']
        senate_id[x] = transcript_and_events[x]['id']

    return senate_transcripts, senate_id, transcript_and_events


def joint_data():
    #Place transcripts and id into specific lists
    
    joint_transcripts = []
    joint_id = []

    joint_sessions = get_session_list_joint()

    events = dictify_jointsession_list(joint_sessions)

    transcript_and_events = add_transcripts(events)

    for x in range(len(transcript_and_events)):
        joint_transcripts[x] = transcript_and_events[x]['transcript']
        joint_id[x] = transcript_and_events[x]['id']

    return joint_transcripts, joint_id, transcript_and_events


# limit updates to daily occurences
def pull_summary():
    # Consolidates data
    house_transcripts, house_id, house_all = house_data()
    senate_transcripts, senate_id, senate_all = senate_data()
    joint_transcripts, joint_id, joint_all = joint_data()

    #Funnel all data into one dictionary
    all_data['house'] = house_all
    all_data['senate'] = senate_all
    all_data['joint'] = joint_all

    # Summarize new transcripts
    for x in range(len(house_id)):
        if house_id[x] not in combined_data:
            combined_data.append(house_id[x])
            summary = claude_summary(house_transcripts[x])
            #transcript_summaries['house'].append(summary)
            all_data['house'][x]['summary'] = summary

    for x in range(len(senate_id)):
        if senate_id[x] not in combined_data:
            combined_data.append(senate_id[x])
            summary = claude_summary(senate_transcripts[x])
            #transcript_summaries['senate'].append(summary)
            all_data['senate'][x]['summary'] = summary

    for x in range(len(joint_id)):
        if joint_id[x] not in combined_data:
            combined_data.append(joint_id[x])
            summary = claude_summary(joint_transcripts[x])
            #transcript_summaries['joint'].append(summary)
            all_data['joint'][x]['summary'] = summary

    # all_data['house'] = house_all
    # all_data['house']['summary'] = transcript_summaries['house']

    # all_data['senate'] = senate_all
    # all_data['senate']['summary'] = transcript_summaries['senate']

    # all_data['joint'] = joint_all
    # all_data['joint']['summary'] = transcript_summaries['joint']
    return all_data
    

