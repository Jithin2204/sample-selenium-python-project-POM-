import time

from Locators.locators import Locators


class SearchCorrectCity():

    def __init__(self, driver):

        self.driver = driver
        self.search_city_textbox_xpath = Locators.search_city_textbox_xpath
        self.search_city_button_xpath = Locators.search_city_button_xpath
        self.choose_city_drop_down_css_selector = Locators.choose_city_drop_down_css_selector
        self.city_displayed_label_xpath = Locators.city_displayed_label_xpath


    def search_correct_city_name(self, city_name):

        self.driver.implicitly_wait(5)
        self.driver.find_element_by_xpath(self.search_city_textbox_xpath).send_keys(city_name)
        time.sleep(10)
        self.driver.find_element_by_xpath(self.search_city_button_xpath).click()
        self.city_name_option_text = self.driver.find_element_by_xpath(self.choose_city_drop_down_css_selector).text

        self.driver.find_element_by_xpath(self.choose_city_drop_down_css_selector).click()
        time.sleep(10)
        self.city_name_forecast_text = self.driver.find_element_by_xpath(self.city_displayed_label_xpath).text

        print(self.city_name_option_text)
        print(self.city_name_forecast_text)

        if (self.city_name_option_text == self.city_name_forecast_text):
            print("This Test passed")

        else:
            print("This Test failed")