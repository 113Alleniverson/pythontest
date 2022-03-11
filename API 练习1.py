import requests
import json
url='https://github.com/public-apis/public-apis'
r=requests.get(url)
print(r)
print('status code:',r.status_code)
response_dict=r.json()
t=response_dict.keys()
print(t)