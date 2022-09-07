from pages.main_page import MainPage
from pages.make_order_page import MakeOrderPage

class TestMakeOrder:
    def test_make_order_via_header_button_successful(self, browser):
        main_page = MainPage(browser=browser, url="https://qa-scooter.praktikum-services.ru/")
        main_page.open()
        main_page.go_to_make_order_page_header_button()
        make_order_page = MakeOrderPage(browser, browser.current_url)
        make_order_page.full_all_order_data()
        make_order_page.click_proceed_order_button()
        make_order_page.pick_data()
        make_order_page.pick_rent_time()
        make_order_page.choose_your_color()
        make_order_page.click_confirm_order_button()
        make_order_page.click_yes_button()

    def test_make_order_via_down_button_successful(self, browser):
        main_page = MainPage(browser=browser, url="https://qa-scooter.praktikum-services.ru/")
        main_page.open()
        main_page.go_to_make_order_page_down_button()
        make_order_page = MakeOrderPage(browser, browser.current_url)
        make_order_page.full_all_order_data()
        make_order_page.click_proceed_order_button()
        make_order_page.pick_data()
        make_order_page.pick_rent_time()
        make_order_page.choose_your_color()
        make_order_page.click_confirm_order_button()
        make_order_page.click_yes_button()