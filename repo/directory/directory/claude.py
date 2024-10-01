import requests
import json
from .models import CSPANdata
import views

ENDPOINT = 'https://api.anthropic.com/v1/claude-3.5-sonnet'
# fyi current claude account is on free, 429 error is out of tokens
KEY = 'sk-ant-api03-yjWtPheKJUMc8nt_NxmFayd17CVhjwaqRTyNjHnq9I0Nn1pwoByOfLrkswX7GiHiRwuEyRi9MaX9hTEja7dESQ-GnJ-RAAA'
DATA = 'our-pulled-data'

headers = {"Content-Type":"application/json", "Authentication": f"Bearer {KEY}"}
data = {"prompt": f"Summarize the following meeting, using key terminology: {DATA}", "max_tokens_to_sample": 1024}

response = requests.post(ENDPOINT, headers=headers, data = json.dumps(data))

if response.status_code == 200:
    result = response.json()
else: 
    result = f"Error: {response.status_code}"