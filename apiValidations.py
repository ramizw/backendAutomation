import requests
import json

response = requests.get('http://216.10.245.166/Library/GetBook.php',
             params={'AuthorName':'Rahul Shetty1'},)
print(response.text)
print(type(response.text))
dict_response = json.loads(response.text)
print(dict_response[0]['isbn'])
################################################################
json_resp = response.json()
print(type(json_resp))
print(dict_response[0]['isbn'])
print(response.status_code)
assert response.status_code == 200
print(response.headers)
print(response.headers['Content-Type'] == 'application/json;charset=UTF-8')
print(response.cookies)
assert response.headers['Content-Type'] == 'application/json;charset=UTF-8'
##############################################################
