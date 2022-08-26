import sys,traceback
from Utilities.WebActions import WebActions
from Utilities.Log import Log
from Waits.waits import Waits
from selenium.webdriver.common.by import By
from Utilities.OutputUtil import OutputUtil
from selenium.webdriver.common.keys import Keys
from time import sleep

class GoogleHomePage:

    def __init__(self, driver):
        self.driver=driver
        self.queryBox='//input[@title="Search"]'
        self.luckyButton ='//input[@name="btnI"]'
        self.imagesButton = 'Images'

    def verify_google_title(self):
        try:
            title =self.driver.title
            if title=="Google":
                OutputUtil.WriteFile("I am able to find Google as title \n")
                Log.write_info_to_log_file(self, "I am able to find Google as title")
                return True
            else:
                OutputUtil.WriteFile("Not able to find Google as title \n")
                Log.write_errors_to_log_file(self, "Not able to find Google as title")
                return False

        except:
            traceback.print_exc(file=sys.stdout)
            Log.write_errors_to_log_file(self, "Not able to verify title")
            return False

    def verify_google_query_box(self):
        try:
            Waits.wait_for_element_presence(self,By.XPATH,self.queryBox)
            OutputUtil.WriteFile("I am able to find Google query box \n")
            Log.write_info_to_log_file(self, "I am able to find Google query box")
            return True

        except:
            traceback.print_exc(file=sys.stdout)
            Log.write_errors_to_log_file(self, "Not able to verify google qyery box")
            return False

    def verify_keyword_search(self,key):
        try:
            element=Waits.wait_for_element_presence(self,By.XPATH,self.queryBox)
            WebActions.send_value_to_textbox(self,key+Keys.ENTER,element)
            OutputUtil.WriteFile("I am able to search "+key+" in query box \n")
            Log.write_info_to_log_file(self, "I am able to search "+key+" in query box")
            return True

        except:
            traceback.print_exc(file=sys.stdout)
            Log.write_errors_to_log_file(self, "Not able to search key in query box")
            return False

# *****************************************************************************************************************

    def verify_lucky_button(self):
        try:
            Waits.wait_for_element_presence(self, By.XPATH, self.luckyButton)
            OutputUtil.WriteFile("I am able to find 'I am feeling lucky' button \n")
            Log.write_info_to_log_file(self,"I am able to find 'I am feeling lucky' button")
            return True

        except:
            traceback.print_exc(file=sys.stdout)
            Log.write_errors_to_log_file(self, " Not able to find feeling lucky button")
            return False


    def click_images_button(self):
        try:
            Waits.wait_for_element_clickablity(self, By.LINK_TEXT, self.imagesButton)
            OutputUtil.WriteFile("I am able to click Images button")
            Log.write_info_to_log_file(self, "I am able to click on the Images button")
            return True
        except:
            traceback.print_exc(file=sys.stdout)
            Log.write_errors_to_log_file(self, "I am not able to click on Images button")
            return False

