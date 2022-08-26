from pytest_bdd import scenarios, given, when, then, scenario, parsers
from Pages.Googlehomepage import GoogleHomePage
from Pages.Googleresultpage import GoogleResultPage
from Utilities.OutputUtil import OutputUtil
import pytest

@scenario("demo.feature",scenario_name="Simple Google search",features_base_dir="./Tests/Web/features/")
def test_search_feature(browser):
    pass

# get the test case key
# scenarioNameForId = "VER-420:Simple Google search"
# xID = scenarioNameForId.split(":")
# VER_ID = xID[0]

googlehomepage=None
googleresultpage=None

@given("I launch google home page")
def login_to_app(browser):
    global googlehomepage
    googlehomepage = GoogleHomePage(browser)
    OutputUtil.WriteFile("I launch the Google Home page\n")

@when(parsers.parse('I search for "{key}" keyword'))
def keyword_search_2(key):
    assert googlehomepage.verify_keyword_search(key), "Assertion failed for Query with key"

@then(parsers.parse('I verify "{key}" keyword results are displayed'))
def keyword_result_2(browser,key):
    global googleresultpage
    googleresultpage=GoogleResultPage(browser,key)
    assert googleresultpage.verify_keyword_result_2(key), "Assertion failed with keyword results"

@then(parsers.parse('Related results include "{key}" keyword'))
def keyword_include(browser, key):
    global googleresultpage
    googleresultpage = GoogleResultPage(browser, key)
    assert googleresultpage.verify_related_result(key), " Assertion failed for related results"

@then(parsers.parse('Related results do not include "{key}" keyword'))
def keyword_not_include(browser, key):
    global googleresultpage
    googleresultpage =  GoogleResultPage(browser, key)
    assert googleresultpage.verify_unrelated_keyword(key), " Assertion failed for unrelated results, Unrelated results found"