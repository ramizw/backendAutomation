from behave import *
import requests

from payload import *
from utilities.configurations import *
from utilities.resources import *


@given('the Book details with {isbn} and {aisle}')
def step_impl(context, isbn, aisle):
    context.url = getConfig()["API"]["endpoint"] + ApiResources.addBook
    context.headers = {"Content-Type": "application/json"}
    context.payload = addBookPayload(isbn, aisle)


@when('we execute AddBook post API method 2')
def step_impl(context):
    context.resp = requests.post(context.url,
                                 json=context.payload,
                                 headers=context.headers,
                                 )


@then('book is successfully added 2')
def step_impl(context):
    print(context.resp.json())
    response_json = context.resp.json()
    context.bookID = response_json['ID']
    print(context.bookID)
    assert response_json['Msg'] == 'successfully added'

# Command to run: behave features/BookAPI.feature --no-capture
# --no-capture: to capture logs

