# страница, на которой оформляется заказ


from pages import locators
from pages.base_page import BasePage


class MakeOrderPage(BasePage):
    def __init__(self, *args, **kwargs):
        super(MakeOrderPage, self).__init__(*args, **kwargs)

    # заполняем поле Имя
    def full_name(self):
        name_input = self.browser.find_element(*locators.name_input)
        name_input.send_keys("Тестимя")

    # заполняем поле Фамилия
    def full_surname(self):
        surname_input = self.browser.find_element(*locators.surname_input)
        surname_input.send_keys("тестфамилия")

    # заполняем поле Адрес
    def full_address(self):
        address_input = self.browser.find_element(*locators.address_input)
        address_input.send_keys("тестадрес")

    # выбираем станцию метро в выпадающем списке
    def select_metro_station(self):
        self.browser.find_element(*locators.metro_input).click()
        self.browser.find_element(*locators.metro_selector).click()

    # заполняем поле Телефон
    def full_telephone_number(self):
        telephone_number_input = self.browser.find_element(*locators.telephone_number_input)
        telephone_number_input.send_keys("89263031553")

    # заполнение всех полей для оформления заказа объединяем в шаг
    def full_all_order_data(self):
        self.full_name()
        self.full_surname()
        self.full_address()
        self.select_metro_station()
        self.full_telephone_number()

    # клик на кнопку Далее после заполнения данных о заказчике
    def click_proceed_order_button(self):
        proceed_order_button = self.browser.find_element(*locators.proceed_order_button)
        proceed_order_button.click()

    # выбираем завтрашний день в пикере даты
    def pick_data(self):
        date_input = self.browser.find_element(*locators.date_input)
        date_input.click()
        date_picker = self.browser.find_element(*locators.date_picker)
        date_picker.click()

    # выбираем срок аренды
    def pick_rent_time(self):
        rent_input = self.browser.find_element(*locators.rent_input)
        rent_input.click()
        rent_selector = self.browser.find_element(*locators.rent_selector)
        rent_selector.click()

    # выбор цвета самоката
    def choose_your_color(self):
        color_checkbox = self.browser.find_element(*locators.samokat_color)
        color_checkbox.click()

    # клик на кнопку Заказать после заполнения данных о самокате
    def click_confirm_order_button(self):
        confirm_order_button = self.browser.find_elements(*locators.confirm_order_button)[1]
        confirm_order_button.click()

    # клик на кнопку Да для подтверждения заказа
    def click_yes_button(self):
        yes_button = self.browser.find_element(*locators.yes_button)
        yes_button.click()
