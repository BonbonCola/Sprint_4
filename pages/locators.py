from selenium.webdriver.common.by import By
from pages import little_helpers

# BasePage locators

to_make_order_buttons = (By.XPATH, "//button[contains(text(),'Заказать')]")
samokat_logo = (By.XPATH, "//body/div[@id='root']//img[@alt='Scooter']")
yandex_logo = (By.XPATH, "//body/div[@id='root']//img[@alt='Yandex']")

# MainPage locators
marketing_block = (By.CLASS_NAME, "Home_Header__iJKdX")
faq_list = (By.CLASS_NAME, "accordion")
faq_questions = (By.CLASS_NAME, "accordion__item")
faq_questions_part_for_text_search = [By.XPATH, ""]
faq_answers = [By.XPATH, ""]

# MakeOrderPage locators
name_input = (By.XPATH, "//body/div[@id='root']//input[@placeholder='* Имя']")
surname_input = (By.XPATH, "//body/div[@id='root']//input[@placeholder='* Фамилия']")
address_input = (By.XPATH, "//body/div[@id='root']//input[@placeholder='* Адрес: куда привезти заказ']")
metro_input = (By.XPATH,
               "//body/div[@id='root']//input[@placeholder='* Станция метро']")  # инпут-кнопка выбора станции метро, по клику на которую появляется выпадающий список со станциями
metro_selector = (
By.XPATH, "//body/div[@id='root']//div[text()='Сокольники']")  # конкретная строка в выпавшем списке станций метро
telephone_number_input = (By.XPATH, "//body/div[@id='root']//input[@placeholder='* Телефон: на него позвонит курьер']")
proceed_order_button = (By.XPATH, "//button[contains(text(),'Далее')]")
confirm_order_button = (By.XPATH, "//button[contains(text(),'Заказать')]")
date_input = (By.XPATH, "//body/div[@id='root']//input[@placeholder='* Когда привезти самокат']")
date_picker = (By.XPATH, "//div[contains(text(),'" + little_helpers.tomorrow() + "')]")
rent_input = (By.XPATH, "//div[contains(text(),'* Срок аренды')]") # инпут-кнопка выбора срока аренды, по клику на которую появляется выпадающий список с вариантами
rent_selector = (By.XPATH, "//div[contains(text(),'двое суток')]") # конкретная строка в выпавшем списке вариантов аренды
samokat_color = (By.ID, "black")
yes_button = (By.XPATH, "//button[contains(text(),'Да')]")
order_complete_label = (By.XPATH, "//div[contains(text(),'Заказ оформлен')]")
