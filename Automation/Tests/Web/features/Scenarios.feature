Feature: Google Sanity UI Test cases
    @sanity
    Scenario: Verify Google title is visible
      Given  I launch google home page
      Then   I verify the Google title

    @sanity
    Scenario: Verify Google query box is visible
      Given  I launch google home page
      Then   I verify Google query box

    @regression
    Scenario: Verify Query with Query results
      Given I launch google home page
      When  I search for "Android" keyword
      Then  I verify "Android" keyword results are displayed