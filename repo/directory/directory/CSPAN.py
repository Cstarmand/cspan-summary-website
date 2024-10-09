# api-key = "0j2wWr10819hVgK4DT8LSata-j82U84y9vafA4YX"
# pull from /mentions for date=yyyy-mm-dd&
# https://api.c-spanarchives.org/2.0/mentions?query=speaker&limit=&personid=&date=(         )&maxdate=&mindate=&page=&videotype=
# Sort by programPublicId

import requests
from requests.auth import HTTPBasicAuth
import json
from datetime import datetime
#from .models import CSPANdata

val = datetime.now().date()
api_key = "0j2wWr10819hVgK4DT8LSata-j82U84y9vafA4YX"
api_url = f"https://api.c-spanarchives.org/2.0/mentions?query=speaker&limit=&personid=&date={val}&maxdate=&mindate=&page=&videotype=/get"
auth_ = HTTPBasicAuth('apikey', api_key)
response = requests.get(api_url, headers={"Authentication": f"Basic {api_key}"})

if response.status_code == 200:
    data = response.json()
    print(data)
else:
    data = response.status_code
    print(data)

# messed around with program, kept getting 403 error (forbidden) no matter how I changed headers and auth
