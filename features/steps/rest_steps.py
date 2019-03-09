from app import app
from behave import *
from hamcrest import *
from mock import patch
from jsonschema import validate
from nose.tools import assert_equal
from app.common import check_json
from datetime import datetime
import json
import httpretty
import requests


@given('I am logged in')
def step_impl(context):
    logged_in = True
    assert logged_in


@given('json body')
def json_body(context):
    body = context.text
    context.json_body = json.loads(body)


@given('server is down')
def step_impl(context):
    context.patch = patch.object(requests, 'request')
    context.mock = context.patch.start()
    context.mock.side_effect = requests.exceptions.RequestException


@given('headers')
def json_body(context):
    context.headers = json.loads(context.text)


@then('should return status code {status_code} {status_name}')
def response_status_code(context, status_code, status_name):
    assert_that(context.response.status_code, equal_to(int(status_code)))


@given('The mock is set to answer {method} request to {url} with status {status} and body')
def mock_configuration(context, method, url, status):
    mock_configuration = {'status': int(status), 'url': url, 'body': context.text, 'method': method}
    if hasattr(context, 'mock_configurations'):
        context.mock_configurations.append(mock_configuration)
    else:
        context.mock_configurations = [mock_configuration]
    pass


@given('The mock is configured to answer {method} request to {service} service of {url} with status {status} and body')
def mock_configuration(context, method, service, url, status):
    mock_configuration = {'status': int(status), 'url': (app.config[url] + service), 'body': context.text,
                          'method': method}
    if hasattr(context, 'mock_configurations'):
        context.mock_configurations.append(mock_configuration)
    else:
        context.mock_configurations = [mock_configuration]
    pass


@when('{method} request to {url} is made')
def json_request(context, method, url):
    data = None
    headers = {}
    content_type = 'application/json'

    if 'json_body' in context:
        data = json.dumps(context.json_body)

    if hasattr(context, 'mock_configurations'):
        for mock_configuration in context.mock_configurations:
            httpretty.register_uri(method=mock_configuration['method'].upper(),
                                   uri=mock_configuration['url'],
                                   status=mock_configuration['status'],
                                   body=mock_configuration['body'],
                                   match_querystring=True)

    client = app.test_client()

    response = getattr(client, method)(url, data=data, content_type=content_type, headers=headers)
    context.response = response
    try:
        context.response.json = json.loads(context.response.data)
    except Exception:
        pass


@then('response should be content-type {content_type} and has body')
def step_impl(context, content_type):
    assert_that(context.response.content_type, equal_to(content_type))
    assert_that(context.response.data, equal_to(context.text))


@then('response should be content-type {content_type} and has body {body}')
def step_impl(context, content_type, body):
    assert_that(context.response.content_type, equal_to(content_type))
    assert_that(context.response.data, equal_to(body))


@then('the response should have body')
def step_impl(context):
    body = context.text
    check_json(json.loads(body), json.loads(context.response.data))


@then('the response body matches the schema {schema_name}')
def match_schema(context, schema_name):
    j = globals()[schema_name]
    schema = json.loads(j)
    json_response = json.loads(context.response.data)
    validate(json_response, schema)


@then('the response contains {tag}')
def step_impl(context, tag):
    json_response = json.loads(context.response.data)
    assert tag in json_response


@then('should have response body')
def response_body(context):
    json_response = context.response.json
    json_expected = json.loads(context.text)
    check_json(json_expected, json_response)



@then('the tag {tag} of the response has length {n}')
def step_impl(context, tag, n):
    assert tag in context.response.json
    assert_equal(len(context.response.json[tag]), int(n))


@then('the tag {tag} of type {type} of the response is equal to {n}')
def step_impl(context, tag, type, n):
    assert tag in context.response.json
    if type == "integer":
        assert_equal(context.response.json[tag], int(n))
    else:
        assert_equal(context.response.json[tag], n)


@then('the response json should contain error of type {exc} and message {msg}')
def check_exception_error(context, exc, msg):
    errors_array = json.loads(context.response.data)['errors']

    found = False
    for error in errors_array:
        if error['name'] == exc and error['message'] == msg:
            found = True
            break

    assert found


@then('the response json contains an error about {msg}')
def check_exception_error(context, msg):
    error = json.loads(context.response.data)['error']
    assert(error.find(msg) >= 0)


@then('the response json contains an error message about {msg}')
def check_exception_error(context, msg):
    error = json.loads(context.response.data)['message']
    assert(error.find(msg) >= 0)


@then('should have response body with key {key}')
def step_impl(context, key):
    json_response = context.response.json
    assert key in json_response


@then('should have valid datetime for the key {key}')
def step_impl(context, key):
    json_response = context.response.json
    valid_datetime = True

    try:
        datetime.strptime(json_response[key], '%Y-%m-%d %H:%M:%S')
    except ValueError:
        valid_datetime = False
        pass
    assert valid_datetime
