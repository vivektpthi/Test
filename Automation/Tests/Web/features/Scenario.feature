#pytest -v -s  -m regression Tests/Web/step_defs/test_Scenario.py --html-report=./Reports/reports.html
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

    @sanity
    Scenario: Verify I am Feeling Lucky Button
      Given I launch google home page
      Then  I verify I am Feeling Lucky Button

    @sanity
    Scenario: Click on Images button
      Given I launch google home page
      Then  I click on Images button

    @abc
    Scenario: Simple Google search
      Given I launch google home page
      When  I search for "myntra" keyword
      Then  I verify "myntra" keyword results are displayed
      And   Related results include "flipkart" keyword
      But   Related results do not include "python" keyword



