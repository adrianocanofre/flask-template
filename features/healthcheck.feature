Feature: Healthcheck service feature

  Scenario Outline: Method not Allowed
    When <method> request to api/healthcheck is made
    Then should return status code 405 METHOD NOT ALLOWED

      Examples: Methods
          | method |
          | delete |
          | put	   |
          | post   |
