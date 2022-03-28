import requests
import json

response = requests.get('http://216.10.245.166/Library/GetBook.php',
             params={'AuthorName':'Rahul Shetty'},)
json_responce = response.json()

# Retrieve book details with isbn RGHCC
for book in json_responce:
    if book['isbn'] == 'RGHCC':
        print(book)
        break

expectedBook = {
        "book_name": "Learn with Java",
        "isbn": "RGHCC",
        "aisle": "222"
    }

assert book == expectedBook