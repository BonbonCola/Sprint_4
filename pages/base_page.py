from pages import locators


class BasePage:
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    def go_to_make_order_page_header_button(self):
        order_button = self.browser.find_elements(*locators.make_order_buttons)[0]
        order_button.click()

    def go_to_make_order_page_down_button(self):
        order_button = self.browser.find_elements(*locators.make_order_buttons)[1]
        order_button.click()

    def click_to_samokat_logo(self):
        samokat_button = self.browser.find_element(*locators.samokat_logo)
        samokat_button.click()

    def click_to_yandex_logo(self):
        yandex_button = self.browser.find_element(*locators.yandex_logo)
        yandex_button.click()