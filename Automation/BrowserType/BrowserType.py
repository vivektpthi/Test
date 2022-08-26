from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from Config import config
from selenium.webdriver.chrome.service import Service
from webdriver_manager.microsoft import IEDriverManager
from webdriver_manager.firefox import GeckoDriverManager


class BrowserType:

    # this function will setup the path for chrome browser
    def setup_chrome_webdriver(self):
        self.driver =webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        return self.driver

    # this function will setup the path for IE browser
    def setup_IE_webdriver(self):
        self.driver = webdriver.Ie(IEDriverManager().install())
        return self.driver

    # this function will setup the path for FireFox browser
    def setup_firefox_webdriver(self):
        self.driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
        return self.driver


    # this function will take browser type as value and initiated the browser
    # browser type value will be 'Chrome','IE','FireFox'
    def get_browser_value(self, browser_type):
        if browser_type == "chrome":
            self.driver = BrowserType.setup_chrome_webdriver(self)
            self.driver.get(config.APPLICATION_URL)
        elif browser_type == "ie":
            self.driver = BrowserType.setup_IE_webdriver(self)
            self.driver.get(config.APPLICATION_URL)
        elif browser_type == "firefox":
            self.driver = BrowserType.setup_firefox_webdriver(self)
            self.driver.get(config.APPLICATION_URL)
        else:
            print("Invalid Value")
        return self.driver

