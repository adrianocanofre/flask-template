Feature: Working service feature

  Scenario Outline: Method not Allowed
    When <method> request to api/working is made
    Then should return status code 405 METHOD NOT ALLOWED

      Examples: Methods
          | method |
          | delete |
          | put	   |
          | post   |


  Scenario: api not working - dependencies are down
    When get request to api/working is made
    Then should return status code 200 OK
    Then should have response body
    """
    [
    {
      "service": "dependency-api",
      "status": "error",
      "error_description": "dependency-api offline.",
      "error_code": "CODE01"
    },
    {
      "service": "another_dependency-api",
      "status": "error",
      "error_description": "another_dependency-api offline.",
      "error_code": "CODE02"
    }
    ]
    """


  Scenario: api working
    Given The mock is configured to answer GET request to /api/healthcheck service of DEPENDENCY_API_A_URL with status 200 and body
    """
    {
      "status": "I'm alive"
    }
    """
    Given The mock is configured to answer GET request to /api/healthcheck service of DEPENDENCY_API_B_URL with status 200 and body
    """
    {
      "status": "I'm alive"
    }
    """
    When get request to api/working is made
    Then should return status code 200 OK
    Then should have response body
    """
    [
    {
      "service": "dependency-api",
      "status": "working",
      "error_description": "",
      "error_code": ""
    },
    {
      "service": "another_dependency-api",
      "status": "working",
      "error_description": "",
      "error_code": ""
    }
    ]
    """