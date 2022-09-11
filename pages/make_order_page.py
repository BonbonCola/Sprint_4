# страница, на которой оформляется заказ
import allure
from selenium.common import NoSuchElementException

from pages import locators
from pages.base_page import BasePage

from mimesis import Person, Address
from mimesis.locales import Locale


class MakeOrderPage(BasePage):

    def __init__(self, *args, **kwargs):
        super(MakeOrderPage, self).__init__(*args, **kwargs)
        self.user = Person(Locale.RU)
        self.address = Address(Locale.RU)

    # заполняем поле Имя
    def full_name(self):
        name_input = self.browser.find_element(*locators.MakeOrderPageLocators.NAME_INPUT)
        name_input.send_keys(self.user.first_name())

    # заполняем поле Фамилия
    def full_surname(self):
        surname_input = self.browser.find_element(*locators.MakeOrderPageLocators.SURNAME_INPUT)
        surname_input.send_keys(self.user.last_name())

    # заполняем поле Адрес
    def full_address(self):
        address_input = self.browser.find_element(*locators.MakeOrderPageLocators.ADDRESS_INPUT)
        address_input.send_keys(self.address.address())

    # выбираем станцию метро в выпадающем списке
    def select_metro_station(self):
        self.browser.find_element(*locators.MakeOrderPageLocators.METRO_INPUT).click()
        self.browser.find_element(*locators.MakeOrderPageLocators.METRO_SELECTOR).click()

    # заполняем поле Телефон
    def full_telephone_number(self):
        telephone_number_input = self.browser.find_element(*locators.MakeOrderPageLocators.TELEPHONE_NUMBER_INPUT)
        telephone_number_input.send_keys(self.user.telephone(mask="8##########"))

    @allure.step('заполнение всех полей для оформления заказа')
    def full_all_order_data(self):
        self.full_name()
        self.full_surname()
        self.full_address()
        self.select_metro_station()
        self.full_telephone_number()

    @allure.step('клик на кнопку Далее после заполнения данных о заказчике')
    def click_proceed_order_button(self):
        proceed_order_button = self.browser.find_element(*locators.MakeOrderPageLocators.PROCEED_ORDER_BUTTON)
        proceed_order_button.click()

    @allure.step('выбираем завтрашний день в пикере даты')
    def pick_data(self):
        date_input = self.browser.find_element(*locators.MakeOrderPageLocators.DATE_INPUT)
        date_input.click()
        date_picker = self.browser.find_element(*locators.MakeOrderPageLocators.DATE_PICKER)
        date_picker.click()

    @allure.step('выбираем срок аренды')
    def pick_rent_time(self):
        rent_input = self.browser.find_element(*locators.MakeOrderPageLocators.RENT_INPUT)
        rent_input.click()
        rent_selector = self.browser.find_element(*locators.MakeOrderPageLocators.RENT_SELECTOR)
        rent_selector.click()

    @allure.step('выбор цвета самоката')
    def choose_your_color(self):
        color_checkbox = self.browser.find_element(*locators.MakeOrderPageLocators.SAMOKAT_COLOR)
        color_checkbox.click()

    @allure.step('клик на кнопку Заказать после заполнения данных о самокате')
    def click_confirm_order_button(self):
        confirm_order_button = self.browser.find_elements(*locators.MakeOrderPageLocators.CONFIRM_ORDER_BUTTON)[1]
        confirm_order_button.click()

    @allure.step('клик на кнопку Да для подтверждения заказа')
    def click_yes_button(self):
        yes_button = self.browser.find_element(*locators.MakeOrderPageLocators.YES_BUTTON)
        yes_button.click()

    @allure.step('проверка виден ли текст Заказ оформлен')
    def is_order_complete(self):
        try:
            self.browser.find_element(*locators.MakeOrderPageLocators.ORDER_COMPLETE_LABEL)
        except NoSuchElementException:
            return False
        return True
