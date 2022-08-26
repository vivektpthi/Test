from pytest_bdd import scenarios, given, when, then, scenario, parsers
from Pages.Googlehomepage import GoogleHomePage
from Pages.Googleresultpage import GoogleResultPage
from Utilities.OutputUtil import OutputUtil

scenarios("ScenarioOutline.feature",features_base_dir="./Tests/Web/features/")

googlehomepage=None
googleresultpage=None

@given("I launch google home page")
def login_to_app(browser):
    global googlehomepage
    googlehomepage = GoogleHomePage(browser)
    OutputUtil.WriteFile("I launch the Google Home page\n")

@when('I search for <key> keyword')
def keyword_search(key):
    assert googlehomepage.verify_keyword_search(key), "Assertion failed for Query with key"

@then('I verify <subcategory> are visible at results page')
def keyword_category_result(browser,subcategory):
    global googleresultpage
    googleresultpage=GoogleResultPage(browser,subcategory)
    assert googleresultpage.verify_keyword_category(subcategory), "Assertion failed with key results"
