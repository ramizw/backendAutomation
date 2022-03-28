from behave import *
import requests

from payload import *
from utilities.configurations import *
from utilities.resources import *


@given('I have github auth credentials')
def step_impl(context):
    context.se = requests.session()  # Creating Session
    context.se.auth = auth = ('ramizw', getPassword())

    context.url2 = getConfig()["API"]["gitHubEndpoint"] + ApiResources.githubRepos


@when('I hit getRepo API of github')
def step_impl(context):
    context.resp = context.se.get(context.url2)


@then('Status code of response should be {statusCode:d}')
def step_impl(context, statusCode):
    print(context.resp.status_code)
    assert context.resp.status_code == statusCode
