Feature: google search demo feature
  @demo
  Scenario: Simple Google search
    Given I launch google home page
    When  I search for "myntra" keyword
    Then  I verify "myntra" keyword results are displayed
    And   Related results include "flipkart" keyword
    But   Related results do not include "python" keyword


