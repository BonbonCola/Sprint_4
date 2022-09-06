from pages.main_page import MainPage
from pages.make_order_page import MakeOrderPage

class TestMakeOrder:
    def test_full_form(self, browser):
        main_page = MainPage(browser=browser, url="https://qa-scooter.praktikum-services.ru/")
        main_page.open()
        main_page.go_to_make_order_page_header_button()
        make_order_page = MakeOrderPage(browser, browser.current_url)
        make_order_page.full_name()
        make_order_page.full_surname()
        make_order_page.full_address()
        make_order_page.select_metro_station()
        make_order_page.full_telephone_number()