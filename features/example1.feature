Feature: service api

  Scenario: validate api get request
    Given I am logged in
    When get request to api/service is made 
    Then should return status code 200 OK

  """
  Scenario: test forbidden method put
    Given I am logged in
    When put request to api/service is made 
    Then should return status code 405 METHOD NOT ALLOWED
  """

  Scenario: test forbidden method delete
    Given I am logged in
    When delete request to api/service is made 
    Then should return status code 405 METHOD NOT ALLOWED

  Scenario Outline: Method not Allowed
      When <method> request to api/service is made 
      Then should return status code 405 METHOD NOT ALLOWED

		Examples: Methods
            | method |
            | delete |
           # | put	 |


  Scenario: test bad request - wrong id type
    Given I am logged in
    Given json body
    """
      {
        "id": "1",
        "property1": "2015-06-01 00:00:00",
        "property2": "2015-06-01"
      }
    """
    When post request to api/service is made 
    Then should return status code 400 BAD REQUEST
    Then the response should have body
    """
    {
        "error_code": "IOE001",
        "message": "Os dados inseridos são inválidos para essa operação.",
        "response": ""
    }
    """

  Scenario: test bad request - missing attibute "id"
    Given I am logged in
    Given json body
    """
      {
        "property1": "2015-06-01 00:00:00",
        "property2": "2015-06-01"
      }
    """
    When post request to api/service is made 
    Then should return status code 400 BAD REQUEST
    Then the response should have body
    """
    {
        "error_code": "IOE001",
        "message": "Os dados inseridos são inválidos para essa operação.",
        "response": ""
    }
    """

  Scenario: validate api post request
    Given I am logged in
    Given json body
    """
      {
        "id": 1,
        "property1": "2015-06-01 00:00:00",
        "property2": "2015-06-01"
      }
    """
    Given The mock is set to answer POST request to http://0.0.0.0:3000/api/remote with status 404 and body
    """
    {
      "id": 400
    }
    """
    When post request to api/service is made 
    Then should return status code 404 NOT FOUND
