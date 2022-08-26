from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import ElementNotVisibleException
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from Utilities.Log import Log
import sys, traceback


class Waits:
    def __init__(self,driver):
        self.driver = driver

    #***********************************************************************************************#
    #this function allows waiting for an element unless it will not present
    #locator method will be like BY.xpath or BY.id and locator will be Ui locator
    def wait_for_element_presence_return_element(self,locator_method ,locator) :
        try:
            WebDriverWait(self.driver, 60).until(EC.presence_of_element_located((locator_method, locator)))
            element=self.driver.find_element_by_xpath(locator)
            Log.write_info_to_log_file(self,"Element is present")
            print(element.text)
            return element
        except TimeoutException:
            Log.write_info_to_log_file(self, "Element is not present")

    def wait_for_element_presence(self,locator_method ,locator) :
        try:
            element = WebDriverWait(self.driver, 60).until(EC.presence_of_element_located((locator_method, locator)))
            Log.write_info_to_log_file(self,"Element is present")
            return element
        except TimeoutException:
            Log.write_info_to_log_file(self, "Element is not present")


    #********************************************************************************************#
    #this function  allows waiting to find a specific and functionally visible element the specified locator will return.
    #locator method like By.xpath and locator will be page object

    def wait_for_element_visiblity(self, locator_method, locator):
        try:
            element = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((locator_method, locator)))
            Log.write_info_to_log_file(self, "Element is visible")
            return element
        except:
            traceback.print_exc(file=sys.stdout)
            Log.write_errors_to_log_file(self, "Element not visible")

    #********************************************************************************************#
    #this function allows waiting for an element which is invisible or not in the DOM.
    #locator_method will be like by.Xpath by.id and locator will be ui locator
    def wait_for_element_invisiblity(self,locator_method,locator):
        try:
            element = WebDriverWait(self.driver,60).until(EC.invisibility_of_element_located(locator_method,locator))
            Log.write_info_to_log_file(self,"Element Found")
            return element

        except TimeoutError:
            Log.write_errors_to_log_file(self,"Element not found Timeout error occured")

    #********************************************************************************************#
    #this function allows waiting for an element to be clicked
    #locator method will be like BY.xpath etc and locator will be ui locator
    def wait_for_element_clickablity(self, locator_method, locator):
        try:
            element = WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((locator_method, locator)))
            Log.write_info_to_log_file(self, "Element is present")
            return element
        except NoSuchElementException:
            traceback.print_exc(file=sys.stdout)
            Log.write_errors_to_log_file(self, "Element not Found Exception")

    def wait_for_element_invisibility(self, locator_method, locator):
        try:
            element = WebDriverWait(self.driver, 10).until(EC.invisibility_of_element_located((locator_method, locator)))
            Log.write_info_to_log_file(self, "Element is invisible now")
            return element
        except:
            traceback.print_exc(file=sys.stdout)
            Log.write_errors_to_log_file(self, "Element not Found Exception")

    #********************************************************************************************#
    #this function allows waiting for an element unless text is not found
    #locator method will be like BY.Xpath etc and locator will be ui locator and inner_text will be text on which we are finding element.
    def wait_for_element_to_find_by_text(self,locator_method,locator,inner_text):
        try:
            element=WebDriverWait(self.driver,60).until(EC.text_to_be_present_in_element(locator_method,locator,inner_text))
            Log.write_info_to_log_file(self,"Element is present")
            return element
        except:
            Log.write_errors_to_log_file(self,"Element Text Not Found")

    #********************************************************************************************#
    #this function allows waiting for an element unless alter is not present
    #alter will be present after wait
    def wait_for_element_to_alert_is_present(self):
        try:
            myElem = WebDriverWait(self.driver,10).until(EC.alert_is_present())
            myElem.switch_to_alert().accept()
        except TimeoutException:
            Log.write_errors_to_log_file(self,"Alert not appear")




