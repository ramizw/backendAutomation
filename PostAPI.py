import requests
import json
from payload import *
import configparser
from utilities.configurations import *
from utilities.resources import *

url = getConfig()["API"]["endpoint"] + ApiResources.addBook

headers = {"Content-Type": "application/json"}
query = 'select * from Books'
addBook_Response = requests.post(url,
                                 json=buildPayLoadFromDB(query),
                                 headers=headers,
                                 )
print(addBook_Response.json())
response_json = addBook_Response.json()
bookID = response_json['ID']
print(bookID)


#############
#############
# Delete the book
def delete_bookJson(bookID):
    return {
        'ID': bookID
    }


print('deleting the book#######################')
response_delete = requests.post("http://216.10.245.166/Library/DeleteBook.php", json=delete_bookJson(bookID),
                                headers=headers, )
# assert response_delete.status_code == 200
print(bookID)
print(response_delete.status_code)
res_json = response_delete.json()
print(res_json["msg"])


# Upload File
urlF = 'https://httpbin.org/post'
filesX = {'file': open('report.xlsx', 'rb')}

r1 = requests.post(urlF, files=filesX)
print(r1.text)
