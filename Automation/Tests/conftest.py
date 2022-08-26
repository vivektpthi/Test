import time
import pytest
from BrowserType.BrowserType import BrowserType
from Utilities.OutputUtil import OutputUtil
from Config import config

driver = None
jr = None
status = True
test_case_id = None
key = None


# Pass browser name in the command line as parameter , if not passed the chrome is the default
# --browser_name firefox

def pytest_addoption(parser):
    parser.addoption(
        "--browser", action="store", default="chrome"
    )
    parser.addoption(
        "--env_name", action="store", default="test"
    )

@pytest.fixture
def browser(request):
    global driver
    browser_name = request.config.getoption("browser")
    if browser_name == "chrome":
        driver = BrowserType.get_browser_value(request, "chrome")
    elif browser_name == "firefox":
        driver = BrowserType.get_browser_value(request, "firefox")
    elif browser_name == "ie":
        driver = BrowserType.get_browser_value(request, "ie")

    driver.implicitly_wait(2)
    driver.maximize_window()
    return driver

#--------Hooks--------------
# hooks have a pytest prefix
def pytest_bdd_before_scenario(request, scenario):
    OutputUtil.OpenFileInWriteMode()


# run at teardown of test case
def pytest_bdd_after_scenario(request,scenario):
    if driver is not None:
        driver.get_screenshot_as_file(config.SCREENSHOT_FILE)
    OutputUtil.CloseFile()

    # get the test case ID from scenario name
    print(scenario.name)
    # get the test result of pass/fail
    scenario_report = request.node.__scenario_report__.serialize()
    for step in range(len(scenario_report['steps'])):
        if scenario_report['steps'][step]['failed']:
            status = False
            print(f'steps failed to execute: {status}')
            break
        else:
            status = True
            print(f'steps executed successfully: {status}')
    if driver is not None:
        driver.close()
        driver.quit()

@pytest.fixture(scope='function')
def context():
    return {}

