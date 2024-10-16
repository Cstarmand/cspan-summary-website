#importing required modules
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time
import json

#this gets the transcript for individual sessions
def get_transcript(url):
    time.sleep(2)
    #Initialize selenium using chrome and get the content into the driver
    driver = webdriver.Chrome()
    driver.get(url)

    #makes it into a beautiful soup and then extracts from the <pre> tag the transcript
    soup = BeautifulSoup(driver.page_source, features="lxml")
    
    raw_transcript = soup.find_all('pre')[0]

    return raw_transcript.text

#gets a list of congressional hearings from a given page
def get_session_list_house(url="https://www.congress.gov/house-hearing-transcripts/118th-congress"):
    #Initialize selenium using chrome and get the content into the driver
    driver = webdriver.Chrome()
    driver.get(url)
    
    #makes it into a beautiful soup and then extracts from the <pre> tag the transcript
    soup = BeautifulSoup(driver.page_source, features="lxml")
    
    tableRows = [tag for tag in soup.find_all('tr')]
    
    return tableRows

def get_session_list_senate(url="https://www.congress.gov/senate-hearing-transcripts/118th-congress"):
    #Initialize selenium using chrome and get the content into the driver
    driver = webdriver.Chrome()
    driver.get(url)
    
    #makes it into a beautiful soup and then extracts from the <pre> tag the transcript
    soup = BeautifulSoup(driver.page_source, features="lxml")
    
    tableRows = [tag for tag in soup.find_all('tr')]
    
    return tableRows

def get_session_list_joint(url="https://www.congress.gov/joint-hearing-transcripts/118th-congress"):
    #Initialize selenium using chrome and get the content into the driver
    driver = webdriver.Chrome()
    driver.get(url)
    
    #makes it into a beautiful soup and then extracts from the <pre> tag the transcript
    soup = BeautifulSoup(driver.page_source, features="lxml")
    
    tableRows = [tag for tag in soup.find_all('tr')]
    
    return tableRows

#turns the list of sessions into a list of dictionaries
def dictify_session_list(tableRows: BeautifulSoup):
    events = []

    for i in tableRows[1::]:
        event = {}
        link = 'https://www.congress.gov' + i.find_all('a')[0]['href']
        if link[-5::] != '/text':
            link += '/text'
        event['link'] = link
        tags = i.find_all('td')
        event['date'] = tags[1].text
        event['title'] = tags[2].text
        event['id'] = int(tags[0]['data-text'])
        committee = tags[3].find_all('a')
        if len(committee) > 0:
            event['committee'] = committee[0].text
        else:
            event['committee'] = 'Non Specific'
        events.append(event)
    return events

#returns of a list of event dictionaries with their transcript added
def add_transcripts(events: list):
    transcripts = []
    for i in range(len(events)):
        #if not events[i]['link'] == '':
         #   events[i]['transcript'] = get_transcript(events[i]['link'])
        try:
            events[i]['transcript'] = get_transcript(events[i]['link'])
        except:
            events[i]['transcript'] = ''
            print(f'error at index {i} in events')
    return events


#little example of what it can do (only runs as the main file)
if __name__ == "__main__":
    house_sessions = get_session_list_house()
    events = dictify_session_list(house_sessions)
    
    sub_events = events[0:3]

    transcript_and_events = add_transcripts(sub_events)
    
    for i in range(len(transcript_and_events)):
        print(transcript_and_events[i])
        print(json.dumps(transcript_and_events[i]['transcript']))
