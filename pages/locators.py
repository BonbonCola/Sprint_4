from selenium.webdriver.common.by import By
from pages import little_helpers

class URL:
    SCOOTER = "https://qa-scooter.praktikum-services.ru/"
    YANDEX = "https://dzen.ru/?yredirect=true"

# BasePage locators
class BasePageLocators:
    TO_MAKE_ORDER_BUTTONS = (By.XPATH, "//button[contains(text(),'Заказать')]")
    SAMOKAT_LOGO = (By.XPATH, "//body/div[@id='root']//img[@alt='Scooter']")
    YANDEX_LOGO = (By.XPATH, "//body/div[@id='root']//img[@alt='Yandex']")

# MainPage locators
class MainPageLocators:
    MARKETING_BLOCK = (By.CLASS_NAME, "Home_Header__iJKdX")
    FAQ_LIST = (By.CLASS_NAME, "accordion")
    FAQ_QUESTIONS = (By.CLASS_NAME, "accordion__item")
    FAQ_QUESTIONS_PART_FOR_TEXT_SEARCH = [By.XPATH, ""]
    FAQ_ANSWERS = [By.XPATH, ""]

# MakeOrderPage locators
class MakeOrderPageLocators:
    NAME_INPUT = (By.XPATH, "//body/div[@id='root']//input[@placeholder='* Имя']")
    SURNAME_INPUT = (By.XPATH, "//body/div[@id='root']//input[@placeholder='* Фамилия']")
    ADDRESS_INPUT = (By.XPATH, "//body/div[@id='root']//input[@placeholder='* Адрес: куда привезти заказ']")
    METRO_INPUT = (By.XPATH,
                   "//body/div[@id='root']//input[@placeholder='* Станция метро']")  # инпут-кнопка выбора станции метро, по клику на которую появляется выпадающий список со станциями
    METRO_SELECTOR = (
    By.XPATH, "//body/div[@id='root']//div[text()='Сокольники']")  # конкретная строка в выпавшем списке станций метро
    TELEPHONE_NUMBER_INPUT = (By.XPATH, "//body/div[@id='root']//input[@placeholder='* Телефон: на него позвонит курьер']")
    PROCEED_ORDER_BUTTON = (By.XPATH, "//button[contains(text(),'Далее')]")
    CONFIRM_ORDER_BUTTON = (By.XPATH, "//button[contains(text(),'Заказать')]")
    DATE_INPUT = (By.XPATH, "//body/div[@id='root']//input[@placeholder='* Когда привезти самокат']")
    DATE_PICKER = (By.XPATH, "//div[contains(text(),'" + little_helpers.tomorrow() + "')]")
    RENT_INPUT = (By.XPATH, "//div[contains(text(),'* Срок аренды')]") # инпут-кнопка выбора срока аренды, по клику на которую появляется выпадающий список с вариантами
    RENT_SELECTOR = (By.XPATH, "//div[contains(text(),'двое суток')]") # конкретная строка в выпавшем списке вариантов аренды
    SAMOKAT_COLOR = (By.ID, "black")
    YES_BUTTON = (By.XPATH, "//button[contains(text(),'Да')]")
    ORDER_COMPLETE_LABEL = (By.XPATH, "//div[contains(text(),'Заказ оформлен')]")
