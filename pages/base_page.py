# базовая страница(в основном хэдер), с общими для всех страниц элементами, от нее наследуем остальные страницы
import allure

from pages import locators


class BasePage:
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    @allure.step('клик на кнопке Заказать в хэдере')
    def go_to_make_order_page_header_button(self):
        order_button = self.browser.find_elements(*locators.to_make_order_buttons)[0]
        order_button.click()

    @allure.step('клик на лого Самокат в хэдере')
    def click_to_samokat_logo(self):
        samokat_button = self.browser.find_element(*locators.samokat_logo)
        samokat_button.click()

    @allure.step('клик на лого Яндекс в хэдере')
    def click_to_yandex_logo(self):
        yandex_button = self.browser.find_element(*locators.yandex_logo)
        yandex_button.click()