import json
from payloadSample import *
import requests
from utilities.configurations import *
from utilities.resources import *

headers = {"Content-Type": "application/json"}

addBookUrl = getConfig()["API"]["endpoint"] + ApiResources.addBook
deleteBookUrl = getConfig()["API"]["endpoint"] + ApiResources.deleteBook

response = requests.post(addBookUrl, json=addBook('225dfv'), headers=headers, )

json_response = response.json()
print(json_response)

book_id = json_response['ID']

print(json_response)
print(f"Book id is {book_id}")

delete_response = requests.post(deleteBookUrl, json=delete_json(book_id),
                                headers=headers, )

print("Delete status is {}".format(delete_response.status_code))
assert delete_response.status_code == 200
res_json = delete_response.json()

print(res_json["msg"])
assert res_json["msg"] == "book is successfully deleted"

# Authentication
se = requests.session()  # Creating Session
se.auth = auth = ('ramizw', getPassword())

url = getConfig()["API"]["gitHubEndpoint"] + ApiResources.githubUser
github_response = requests.get(url, auth=('ramizw', getPassword()))  # for SSL certification: verify=False
print(github_response.status_code)

url2 = getConfig()["API"]["gitHubEndpoint"] + ApiResources.githubRepos
resp = se.get(url2)
print(resp.status_code)
