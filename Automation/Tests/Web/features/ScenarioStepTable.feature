Feature: Results Page Components

  Scenario: Verify google search results
    Given I launch google home page
    When  I search for account:
      | name   | email              | twitter         | digit |
      | Aslak  | aslak@cucumber.io  | @aslak_hellesoy | 1     |
      | Julien | julien@cucumber.io | @jbpros         | 2     |
      | Matt   | matt@cucumber.io   | @mattwynne      | 3     |

    Then  I verify names are visible at results page:
      | name   |
      | Aslak  |
      | Julien |
      | Matt   |
