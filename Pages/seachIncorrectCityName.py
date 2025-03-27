import time
from Locators.locators import Locators


class SearchIncorrectCity():

    def __init__(self, driver):

        self.driver = driver
        self.search_city_textbox_xpath = Locators.search_city_textbox_xpath
        self.search_city_button_xpath = Locators.search_city_button_xpath
        self.choose_city_drop_down_css_selector = Locators.choose_city_drop_down_css_selector
        self.city_not_displayed_xpath = Locators.city_not_displayed_xpath


    def search_incorrect_city_name(self, city_name):

        self.driver.implicitly_wait(5)
        self.driver.find_element_by_xpath(self.search_city_textbox_xpath).send_keys(city_name)
        time.sleep(10)
        self.driver.find_element_by_xpath(self.search_city_button_xpath).click()
        time.sleep(10)
        self.no_results_found = self.driver.find_element_by_xpath(self.city_not_displayed_xpath).text
        self.no_results_found_str = str(self.no_results_found)
        print(self.no_results_found)

        if "No results" in self.no_results_found_str:
            print("This Test passed")

        else:
            print("This Test failed")