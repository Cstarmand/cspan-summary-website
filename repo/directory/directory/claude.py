import requests
import json

ENDPOINT = 'https://api.anthropic.com/v1/claude-3.5-sonnet'
KEY = 'api-key'
DATA = 'our-pulled-data'

headers = {"Content-Type":"application/json", "Authentication": f"Bearer {KEY}"}
data = {"prompt": f"Summarize the following meeting, using key terminology: {DATA}", "max_tokens_to_sample": 1024}

response = requests.post(ENDPOINT, headers=headers, data = json.dumps(data))

if response.status_code == 200:
    result = response.json()
else: 
    result = f"Error: {response.status_code}"