from pytest_bdd import scenarios, given, when, then, scenario, parsers
from Pages.Googlehomepage import GoogleHomePage
from Pages.Googleresultpage import GoogleResultPage
from Utilities.OutputUtil import OutputUtil

scenarios("Scenarios.feature",features_base_dir="./Tests/Web/features/")

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
