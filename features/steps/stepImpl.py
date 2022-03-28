from behave import *
import requests

from payload import *
from utilities.configurations import *
from utilities.resources import *


@given('the Book details which needs to be added to Library')
def step_impl(context):
    context.url = getConfig()["API"]["endpoint"] + ApiResources.addBook

    context.headers = {"Content-Type": "application/json"}
    context.query = 'select * from Books'


@when('we execute AddBook post API method')
def step_impl(context):
    context.resp = requests.post(context.url,
                                 json=buildPayLoadFromDB(context.query),
                                 headers=context.headers,
                                 )


@then('book is successfully added')
def step_impl(context):
    print(context.resp.json())
    response_json = context.resp.json()
    context.bookID = response_json['ID']
    print(context.bookID)
    assert response_json['Msg'] == 'successfully added'

# Command to run: behave features/BookAPI.feature --no-capture
# --no-capture: to capture logs
