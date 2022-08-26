Feature: Results Page Components

  Scenario Outline: Verify google search results are having sub category
    Given I launch google home page
    When  I search for <key> keyword
    Then  I verify <subcategory> are visible at results page

    Examples: Vertical
        | key           | usa     | india | russia | france |
        | subcategory   | Images  | Maps  | News   | Videos |