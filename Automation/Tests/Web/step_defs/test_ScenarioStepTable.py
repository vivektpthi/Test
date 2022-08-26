from pytest_bdd import scenarios, given, when, then, scenario, parsers
from Pages.Googlehomepage import GoogleHomePage
from Pages.Googleresultpage import GoogleResultPage
from Utilities.OutputUtil import OutputUtil
from typing import List, Union
from sttable import parse_str_table


@scenario("ScenarioStepTable.feature",scenario_name="Verify google search results",features_base_dir="./Tests/Web/features/")
def test_hello(browser):
    pass

googlehomepage=None
googleresultpage=None

@given("I launch google home page")
def login_to_app(browser):
    global googlehomepage
    googlehomepage = GoogleHomePage(browser)
    OutputUtil.WriteFile("I launch the Google Home page\n")

@when(parsers.parse('I search for account:\n{table}'))
def keyword_search(table):
    var=parse_str_table(table)
    for i in range(3):
        print(var.get_row(i))


@then(parsers.parse('I verify names are visible at results page:\n{table}'))
def keyword_category_result(browser,table):
    var=parse_str_table(table)
    for i in range(3):
        print(var.get_row(i)['name'])

