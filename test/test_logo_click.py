import time

from pages.main_page import MainPage
from pages.make_order_page import MakeOrderPage

class TestLogoClick:
    def test_samokat_logo_click_go_to_main_page(self, browser):
        main_page = MainPage(browser=browser, url="https://qa-scooter.praktikum-services.ru/")
        main_page.open()
        main_page.go_to_make_order_page_header_button()
        make_order_page = MakeOrderPage(browser, browser.current_url)
        make_order_page.click_to_samokat_logo()
        main_page = MainPage(browser, browser.current_url)
        assert main_page.is_marketing_block_visible(), 'Не главная страница, нет маркетингового текста'