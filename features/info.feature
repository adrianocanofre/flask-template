Feature: Info service feature

  Scenario Outline: Method not Allowed
    When <method> request to api/info is made
    Then should return status code 405 METHOD NOT ALLOWED

      Examples: Methods
          | method |
          | delete |
          | put	   |
          | post   |

  Scenario: api info
    Given I mock server datetime to 2019-02-26 10:04:21
    Given I mock service version to 0.0.0
    When get request to api/info is made
    Then should return status code 200 OK
    Then should have response body
    """
    {
        "version": "0.0.0",
        "server_datetime": "2019-02-26 10:04:21"
    }
    """
