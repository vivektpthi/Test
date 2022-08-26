from pytest_bdd import scenarios, given, when, then, scenario, parsers
from Pages.Googlehomepage import GoogleHomePage
from Pages.Googleresultpage import GoogleResultPage
from Utilities.OutputUtil import OutputUtil
import pytest

@scenario("Scenario.feature",scenario_name="Verify Google title is visible",features_base_dir="./Tests/Web/features/")
def test_verify_title(browser):
    pass

@scenario("Scenario.feature",scenario_name="Verify Google query box is visible",features_base_dir="./Tests/Web/features/")
def test_verify_query(browser):
    pass

@scenario("Scenario.feature",scenario_name="Verify Query with Query results",features_base_dir="./Tests/Web/features/")
def test_verify_result(browser):
    pass

@scenario("Scenario.feature",scenario_name="Verify I am Feeling Lucky Button",features_base_dir="./Tests/Web/features/")
def test_verify_button(browser):
    pass

@scenario("Scenario.feature", scenario_name="Click on Images button", features_base_dir="./Tests/Web/features/")
def test_click_images_button(browser):
    pass

@scenario("Scenario.feature",scenario_name="Simple Google search",features_base_dir="./Tests/Web/features/")
def test_search_feature(browser):
    pass


googlehomepage=None
googleresultpage=None

@given("I launch google home page")
def login_to_app(browser):
    global googlehomepage
    googlehomepage = GoogleHomePage(browser)
    OutputUtil.WriteFile("I launch the Google Home page\n")

@then('I verify the Google title')
def newly_created_device():
    assert googlehomepage.verify_google_title(), "Assertion failed for Title"

@then('I verify Google query box')
def newly_created_device():
    assert googlehomepage.verify_google_query_box(), "Assertion failed for Query Box"

@when(parsers.parse('I search for "{key}" keyword'))
def keyword_search(key):
    assert googlehomepage.verify_keyword_search(key), "Assertion failed for Query with key"

@then(parsers.parse('I verify "{key}" keyword results are displayed'))
def keyword_result(browser,key):
    global googleresultpage
    googleresultpage=GoogleResultPage(browser,key)
    assert googleresultpage.verify_keyword_result(key), "Assertion failed with key results"

@then('I verify I am Feeling Lucky Button')
def button_finder():
    assert googlehomepage.verify_lucky_button(), " Assertion failed for feeling Lucky button"

@then('I click on Images button')
def click_images_button():
    assert googlehomepage.click_images_button(), "Assertion failed for clicking Images button"

# ******************************************************************************************************************

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


