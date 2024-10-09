import requests
import json
import anthropic
#from .models import CSPANdata
#import views

ENDPOINT = 'https://api.anthropic.com/v1/claude-3.5-sonnet'
# fyi current claude account is on free, 429 error is out of tokens
KEY = f"sk-ant-api03-yjWtPheKJUMc8nt_NxmFayd17CVhjwaqRTyNjHnq9I0Nn1pwoByOfLrkswX7GiHiRwuEyRi9MaX9hTEja7dESQ-GnJ-RAAA"
DATA = 'our-pulled-data'

client = anthropic.Anthropic(api_key=KEY)

message = client.messages.create(model="claude-3-5-sonnet-20240620", max_tokens=1024, temperature=0, system="You are a summary tool, whose job is to summarize a government meeting, keeping key terminology and topics, and writing a shortened and readable summary which is understandable to the average citizen.", messages = [{"role":"user", "content":[{"type":"text", "text":f"{DATA}"}]}])
message.content

# headers = {"Content-Type":"application/json", "Authentication": f"Bearer {KEY}"}
# data = {"prompt": f"Summarize the following meeting, using key terminology: {DATA}", "max_tokens_to_sample": 1024}

# response = requests.post(ENDPOINT, headers=headers, data = json.dumps(data))

# if response.status_code == 200:
#     result = response.json()
#     print(result)
# else: 
#     result = f"Error: {response.status_code}"
#     print(result)