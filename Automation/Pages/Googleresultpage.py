import sys,traceback
from Utilities.WebActions import WebActions
from Utilities.Log import Log
from Waits.waits import Waits
from selenium.webdriver.common.by import By
from Utilities.OutputUtil import OutputUtil
from selenium.webdriver.common.keys import Keys
from time import sleep
from pytest_html_reporter import attach


class GoogleResultPage:

    def __init__(self, driver, key):
        self.driver = driver
        self.key_result_xpath="//*[text()='"+key+"']"
        self.subcategory_xpath="//a[text()='"+key+"']"
        self.key_xpath = "//*[text()='"+key+"']"
        self.key2_xpath = "//*[text()='"+key+"']"
        self.key3_xpath = "//*[text()='"+key+"']"

    def verify_keyword_result(self,key):
        try:
            elements=self.driver.find_elements_by_xpath(By.XPATH,self.key_result_xpath)
            if len(elements)>5:
                OutputUtil.WriteFile("Results for "+key+" are visible \n")
                Log.write_info_to_log_file(self,"Results for "+key+" are visible")
                return True
            else:
                return False

        except:
            traceback.print_exc(file=sys.stdout)
            Log.write_errors_to_log_file(self, "Not able to get results")
            return False

    def verify_keyword_category(self,subcategory):
        try:
            Waits.wait_for_element_presence(self,By.XPATH,self.subcategory_xpath)
            OutputUtil.WriteFile(subcategory+" category is visible \n")
            Log.write_info_to_log_file(self,subcategory+" category is visible")
            return True

        except:
            traceback.print_exc(file=sys.stdout)
            Log.write_errors_to_log_file(self, "Not able to get sub-category")
            return False

# ********************************************************************************************************************

    # results for myntra keyword
    def verify_keyword_result_2(self, key):
        try:
            element = Waits.wait_for_element_presence(self, By.XPATH, self.key_xpath)
            OutputUtil.WriteFile('I am able to find results for "'+key+'"\n')
            Log.write_info_to_log_file(self, "Results for "+key+" are visible")
            return True
        except:
            traceback.print_exc(file=sys.stdout)
            Log.write_errors_to_log_file(self, "Not able to find results")
            return False

    # results for related keyword flipkart
    def verify_related_result(self, key):
        try:
            element = Waits.wait_for_element_visiblity(self, By.XPATH, self.key2_xpath)
            OutputUtil.WriteFile('I am able to find related results for "'+key+'" \n')
            Log.write_info_to_log_file(self, "Related Results for " + key + " are visible")
            return True

        except:
            traceback.print_exc(file=sys.stdout)
            Log.write_errors_to_log_file(self, "Not able to find related results")
            return False

    # results for unrelated keywords
    def verify_unrelated_keyword(self, key):
        try:
            element = Waits.wait_for_element_visiblity(self, By.XPATH, self.key2_xpath)
            if element is None:
                OutputUtil.WriteFile('I am not able to find unrelated results for "'+key+'" \n')
                Log.write_info_to_log_file(self, "Related results for " + key + " are not found")
                return True
            else:
                return False
        except:
            traceback.print_exc(file=sys.stdout)
            Log.write_errors_to_log_file(self, "Not able to find unrelated results")
            return False






