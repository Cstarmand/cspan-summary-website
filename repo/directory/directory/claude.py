import requests
import json
import anthropic
#from .models import CSPANdata
#import views

def claude_summary(DATA):
    ENDPOINT = 'https://api.anthropic.com/v1/claude-3.5-sonnet'
# fyi current claude account is on free, insufficent funds error is out of tokens
    KEY = f"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"

    client = anthropic.Anthropic(api_key=KEY)

    message = client.messages.create(model="claude-3-5-sonnet-20240620", max_tokens=1024, temperature=0, system="You are a summary tool, whose job is to summarize a congressional session or hearing, keeping key terminology and topics (ignoring all instances of /n), and writing a shortened and readable summary which is understandable to the average citizen. Include such information as key person names, content of bills and discussions, monetary values and costs mentioned, relevant statistics to the topic of discussion, main changes and conclusions from the session, and impacted groups. Exclude such information as the title, date, introduction to the session, prayer, and the pledge of allegiance.", messages = [{"role":"user", "content":[{"type":"text", "text":f"{DATA}"}]}])
    
    return message.content

# headers = {"Content-Type":"application/json", "Authentication": f"Bearer {KEY}"}
# data = {"prompt": f"Summarize the following meeting, using key terminology: {DATA}", "max_tokens_to_sample": 1024}

# response = requests.post(ENDPOINT, headers=headers, data = json.dumps(data))

# if response.status_code == 200:
#     result = response.json()
#     print(result)
# else: 
#     result = f"Error: {response.status_code}"
#     print(result)
claude_summary("hello")