import requests
import json
"""
def view_app():
    URL= 'http://127.0.0.1:8000/api/view/'
    r= requests.get(url=URL)
    data=r.json()
    print(data)"""
URL='http://127.0.0.1:8000/myshop/edit/'
data={'name':'test1','age':101,'email':'owaisali'
                                       '@gmail.com'}
json_data=json.dumps(data)
r=requests.post(url=URL, data = json_data)
data=r.json()
print(data)



    
    