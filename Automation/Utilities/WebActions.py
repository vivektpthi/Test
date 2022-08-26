from Utilities.Log import Log
import time
import sys, traceback
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
from selenium.common.exceptions import ElementNotInteractableException
from selenium.common.exceptions import TimeoutException
from Utilities.Log import Log
from selenium.webdriver.common.keys import Keys


class WebActions:


    def __init__(self,driver):
        self.driver = driver

    #this function will send value to text box argument value is some text and element is text box object where we are sending value
    #value = "ABC"

    #element will be the locator
    def custom_scroll(self,element):
        try:
            desired_y = (element.size['height'] / 2) + element.location['y']
            window_h = self.driver.execute_script('return window.innerHeight')
            window_y = self.driver.execute_script('return window.pageYOffset')
            current_y = (window_h / 2) + window_y
            scroll_y_by = desired_y - current_y
            self.driver.execute_script("window.scrollBy(0, arguments[0]);", scroll_y_by)
            Log.write_info_to_log_file(self,"scroll success")
        except:
            traceback.print_exc(file=sys.stdout)
            Log.write_errors_to_log_file(self,"scroll failed")

    def send_value_to_textbox(self,value,element):
        try:
            element.send_keys(value)
            Log.write_info_to_log_file(self,"value send to text box")
            return True
        except:
            Log.write_errors_to_log_file(self,"Element not found")
            return False

    def clear_value_in_textbox(self,element):
        try:
            element.clear()
            Log.write_info_to_log_file(self,"value cleared in text box")
        except:
            Log.write_errors_to_log_file(self,"Element not found")

    #this function will click on element where element is object on
    # which we are going to perform click operation
    #element will be the locator of page
    def click_on_element(self,element):
        try:
            element.click()
            Log.write_info_to_log_file(self,"Clicked successfully")
            return True
        except:
            # traceback.print_exc(file=sys.stdout)
            Log.write_errors_to_log_file(self,"Element not found to perform click action")
            return False

    def scroll_to_home(self,xpath):
        self.driver.find_element_by_xpath(xpath).send_keys(Keys.HOME)
        time.sleep(5)

    #this functions is used to apply some wait in between the functions
    def wait(self,time_in_seconds):
        try:
            time.sleep(time_in_seconds)
            Log.write_info_to_log_file(self,"wait for "+str(time_in_seconds)+" seconds")
        except TimeoutException:
            Log.write_errors_to_log_file(self,"wait Failed")

    #mouse hover action is performed by using this function where element
    #is page object on which we are going to hover
    def hover_on_mouse_action(self,element):
        try:
            action = ActionChains(self.driver)
            action.move_to_element(element).perform()
            Log.write_info_to_log_file(self, "hover on mouse action performed successfully")
        except ElementNotInteractableException:
            Log.write_errors_to_log_file(self,"Element not found for hover action")

    #this function will select the element from drop down by using value .Element is dropdown locator
    def select_element_from_dropdown_by_value(self,element,value):
        try:
            print("------------A----------")
            s1 = Select(self.driver.find_element_by_xpath(element)[2])
            s1.select_by_visible_text(value)
            print("------------B---------")
            Log.write_info_to_log_file(self,"element is selected f`rom dropdown")
        except ElementNotInteractableException:
            Log.write_errors_to_log_file(self,"Element not found")

    #this function will perform  keyboard event where key is keyboard key  element is page object and value is the text that we want.
    def press_keyboard_enter_key(self,keys,element,value):
        try:
            element.send_keys(value,keys)
            Log.write_info_to_log_file(self,"keyboard key is pressed")
        except:
            Log.write_errors_to_log_file(self,"keyboard is not pressed")

    #this function will check if element is selected or not where element is object that we want to select
    def check_element_selected(self,element):
        try:
            element_status = element.is_selected()
            Log.write_info_to_log_file(self, "element is selected")
            return element_status
        except ElementNotInteractableException:
            Log.write_errors_to_log_file(self,"Element is not selected")

    #this function will check if element is displayed or not where element is page object
    def check_element_displayed(self,element):
        try:
            element_status = element.is_displayed()
            Log.write_info_to_log_file(self,"Element is displayed")
            return element_status
        except ElementNotInteractableException:
            Log.write_errors_to_log_file(self,"Element is not displayed")

    #this function will check if element is enabled or not where element is page object
    def check_element_enabled(self,element):
        try:
            element_status = element.is_enabled()
            Log.write_info_to_log_file(self,"Element is enabled")
            return element_status
        except ElementNotInteractableException:
            Log.write_errors_to_log_file(self,"Element not found")

    #this function will take user to previous page
    def navigate_to_previous_page(self):
        try:
            self.driver.execute_script("window.histroy.go(-1)")
            Log.write_info_to_log_file(self,"Navigate to previous page")
        except TimeoutException:
            Log.write_errors_to_log_file(self,"Page not fund")

    #this function will refresh the current page
    def refresh_current_page(self):
        try:
            self.driver.refresh()
            Log.write_info_to_log_file(self, "page refreshed successfully")
        except:
            Log.write_errors_to_log_file(self,"Page refresh failed")

    #this function will switch the window between two window
    def switch_window(self,window_handle):
        try:
            self.driver.switch_to_window(window_handle)
            Log.write_info_to_log_file(self,"switch window successfully")
        except:
            Log.write_errors_to_log_file(self,"Switch window failed")

    #this function is used to extract the text from element
    def get_text(self,element):
        try:
            return str(element.text)
        except ElementNotInteractableException:
            Log.write_errors_to_log_file(self, "Text is not present")

    #this function is used to extract the  attribute value from element
    def get_attribute_value(self,element,attr_name):
        try:
            return element.get_attribute(attr_name)
        except ElementNotInteractableException:
            Log.write_errors_to_log_file(self,"Attribute value is not present")

    #by using this function we can find the size of element
    def get_element_size(self,element):
        try:
            #output will be in the form of dict {hight:100,width:200}
            return element.get_size()
        except ElementNotInteractableException:
            Log.write_errors_to_log_file(self,"element not found")

    #this function is used to submit the form
    def submit_form(self,element):
        try:
            element.submit()
        except ElementNotInteractableException:
            Log.write_errors_to_log_file(self, "Element not found")

    #this function is used to drag and drop the element
    def drag_and_drop_element(self,source_element,target_element):
        try:
            driver = self.driver
            action_chains = ActionChains(driver)
            action_chains.drag_and_drop(source_element, target_element)
        except ElementNotInteractableException:
            Log.write_errors_to_log_file(self,"Element Not Found")

    def add_cookies(self,cookie):
        #cookie is the variable which stored actual value like cookie:{'name':'foo','value':'bar'}
        try:
            self.driver.add_cookie(cookie)
            Log.write_info_to_log_file(self,"cookies added successfully")
        except:
            Log.write_errors_to_log_file(self,"cookies not added successfully")

    def get_all_cookies(self):
        #this function will return all the cookies from current url
        self.driver.get_cookies()

    def select_value_from_list(self,xpath):
        try:
            element = self.driver.find_element_by_xpath(xpath)
            element.click()
            Log.write_info_to_log_file(self, "Element is selected from values")

        except:
            Log.write_info_to_log_file(self, "Element is not selected from values")

