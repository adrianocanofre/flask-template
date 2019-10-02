import app
from behave import *
from hamcrest import *
from mock import patch, MagicMock
from jsonschema import validate
from nose.tools import assert_equal
from app.common import check_json
from datetime import datetime
import json
import httpretty
import requests
from time import sleep


@given('json body')
def json_body(context):
    body = context.text
    context.json_body = json.loads(body)


@when('{method} request to {url} is made')
def json_request(context, method, url):
    data = None
    headers = {}
    content_type = 'application/json'

    if 'json_body' in context:
        data = json.dumps(context.json_body)
    if not httpretty.is_enabled():
        httpretty.enable()
    if hasattr(context, 'mock_configurations'):
        for mock_configuration in context.mock_configurations:
            httpretty.register_uri(method=mock_configuration['method'].upper(),
                                   uri=mock_configuration['url'],
                                   status=mock_configuration['status'],
                                   body=mock_configuration['body'],
                                   match_querystring=True)

    client = app.app.test_client()

    response = getattr(client, method)(url, data=data, content_type=content_type, headers=headers)
    context.response = response
    try:
        context.response.json = json.loads(context.response.data)
    except Exception:
        pass


@then('should return status code {status_code} {status_name}')
def response_status_code(context, status_code, status_name):
    assert_that(context.response.status_code, equal_to(int(status_code)))


@then('should have response body')
def response_body(context):
    json_response = context.response.json
    json_expected = json.loads(context.text)
    print("json", context.response.json)
    print("exp", json_expected)
    check_json(json_expected, json_response)


@Then('the return job json matches')
def return_json(context):
    result = context.response.json
    check_json(json.loads(context.text), result)


@Then('the update return json matches')
def step_impl(context):
    returned_json = context.response.json
    expected_json = json.loads(context.text)
    if 'id' in returned_json:
        returned_json.pop('id', None)
        expected_json.pop('id', None)
    else:
        raise IndexError('should have id key')
    check_json(expected_json, returned_json)
