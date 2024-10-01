# api-key = "0j2wWr10819hVgK4DT8LSata-j82U84y9vafA4YX"
# pull from /mentions for date=yyyy-mm-dd&
# https://api.c-spanarchives.org/2.0/mentions?query=speaker&limit=&personid=&date=(         )&maxdate=&mindate=&page=&videotype=
# Sort by programPublicId

import requests
import json
from datetime import datetime
#from .models import CSPANdata

val = datetime.now().date()
api_url = f"https://api.c-spanarchives.org/2.0/mentions?query=speaker&limit=&personid=&date={val}&maxdate=&mindate=&page=&videotype="
response = requests.get(api_url)

if response.status_code == 200:
    data = response.json()
else:
    data = response.status_code