import time

import allure

from pages.main_page import MainPage
from pages.make_order_page import MakeOrderPage

class TestLogoClick:
    @allure.title('Переход на главную по клику на лого Самокат')  # декораторы
    @allure.description(' ')
    def test_samokat_logo_click_go_to_main_page(self, browser):
        main_page = MainPage(browser=browser, url="https://qa-scooter.praktikum-services.ru/")
        main_page.open()
        main_page.go_to_make_order_page_header_button()
        make_order_page = MakeOrderPage(browser, browser.current_url)
        make_order_page.click_to_samokat_logo()
        main_page = MainPage(browser, browser.current_url)
        assert main_page.is_marketing_block_visible(), 'Не главная страница: нет маркетингового текста'

    @allure.title('Открывается главная Яндекса по клику на лого Яндекс')  # декораторы
    @allure.description('в отдельном табе')
    def test_yandex_logo_click_go_to_ya_page(self, browser):
        main_page = MainPage(browser=browser, url="https://qa-scooter.praktikum-services.ru/")
        main_page.open()
        main_page.click_to_yandex_logo()
        browser_tabs = browser.window_handles
        browser.switch_to.window(browser_tabs[1])
        time.sleep(5)
        assert browser.current_url == "https://yandex.ru/"


