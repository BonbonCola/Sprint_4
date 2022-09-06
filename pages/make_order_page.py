from pages import locators
from pages.base_page import BasePage
from selenium.webdriver.support.ui import Select

class MakeOrderPage(BasePage):
    def __init__(self, *args, **kwargs):
        super(MakeOrderPage, self).__init__(*args, **kwargs)

    def full_name(self):
        name_input = self.browser.find_element(*locators.name_input)
        name_input.send_keys("Тестимя")

    def full_surname(self):
        surname_input = self.browser.find_element(*locators.surname_input)
        surname_input.send_keys("тестфамилия")

    def full_address(self):
        address_input = self.browser.find_element(*locators.address_input)
        address_input.send_keys("тестадрес")

    def select_metro_station(self):
        self.browser.find_element(*locators.metro_input).click()
        self.browser.find_element(*locators.metro_selector).click()

    def full_telephone_number(self):
        telephone_number_input = self.browser.find_element(*locators.telephone_number_input)
        telephone_number_input.send_keys("89263031553")