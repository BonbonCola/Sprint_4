# лендинг
from pages import locators
from pages.base_page import BasePage


class MainPage(BasePage):
    def __init__(self, *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs)

    # клик на кнопке Заказать внизу лендинга
    def go_to_make_order_page_down_button(self):
        button = self.browser.find_elements(*locators.to_make_order_buttons)[1]
        # Прокрути страницу до кнопки
        self.browser.execute_script("arguments[0].scrollIntoView();", button)
        button.click()