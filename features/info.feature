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
    When get request to api/info is made
    Then should return status code 200 OK
    Then should have response body with key version
    Then should have response body with key server_datetime
    Then should have valid datetime for the key server_datetime


