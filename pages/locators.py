from selenium.webdriver.common.by import By

#BasePage locators
make_order_buttons = (By.XPATH, "//button[contains(text(),'Заказать')]")
samokat_logo = (By.XPATH, "//body/div[@id='root']//img[@alt='Scooter']")
yandex_logo = (By.XPATH, "//body/div[@id='root']//img[@alt='Yandex']")

#MakeOrderPage locators
name_input = (By.XPATH, "//body/div[@id='root']//input[@placeholder='* Имя']")
surname_input = (By.XPATH, "//body/div[@id='root']//input[@placeholder='* Фамилия']")
address_input = (By.XPATH, "//body/div[@id='root']//input[@placeholder='* Адрес: куда привезти заказ']")
metro_input = (By.XPATH, "//body/div[@id='root']//input[@placeholder='* Станция метро']")
metro_selector = (By.XPATH, "//body/div[@id='root']//div[text()='Сокольники']")
telephone_number_input = (By.XPATH, "//body/div[@id='root']//input[@placeholder='* Телефон: на него позвонит курьер']")
