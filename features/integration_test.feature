Feature: API Integration Test for Persons Endpoint

  @integration_test
  Scenario: Create and verify a person record
    Given I have the API endpoint "https://680f16f067c5abddd193cb4f.mockapi.io/persons/testing"
    When I send a POST request with:
      | name | age | profession |
      | Romulo | 77 | Electricista |
    Then the response status code should be 201
    And the response should contain the created person data
    When I send a GET request to "https://680f16f067c5abddd193cb4f.mockapi.io/persons/testing"
    Then the GET response should contain the created record