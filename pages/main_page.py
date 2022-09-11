# лендинг
import time

import allure
from selenium.common import NoSuchElementException

from pages import locators
from pages.base_page import BasePage


class MainPage(BasePage):
    def __init__(self, *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs)

    @allure.step('клик на кнопке Заказать внизу лендинга')
    def go_to_make_order_page_down_button(self):
        button = self.browser.find_elements(*locators.BasePageLocators.TO_MAKE_ORDER_BUTTONS)[1]
        # Прокрути страницу до кнопки
        self.browser.execute_script("arguments[0].scrollIntoView();", button)
        time.sleep(1)
        button.click()

    @allure.step('проверка виден ли на лендинге промо текст')
    def is_marketing_block_visible(self):
        try:
            self.browser.find_element(*locators.MainPageLocators.MARKETING_BLOCK)
        except NoSuchElementException:
            return False
        return True

    @allure.step('скролл до списка вопросов')
    def scroll_to_faq_list(self):
        faq_list = self.browser.find_element(*locators.MainPageLocators.FAQ_LIST)
        # Прокрути страницу до списка вопросов
        self.browser.execute_script("arguments[0].scrollIntoView();", faq_list)
        time.sleep(1)

    @allure.step('клик на один из списка вопрос')
    def click_to_faq_question(self, index):
        faq_questions = self.browser.find_elements(*locators.MainPageLocators.FAQ_QUESTIONS)
        faq_questions[index].click()
        faq_questions[index].click()

    @allure.step('сверяем текст вопроса')
    def is_text_in_faq_question_correct(self, question):
        locators.MainPageLocators.FAQ_QUESTIONS_PART_FOR_TEXT_SEARCH[1] = ""
        locators.MainPageLocators.FAQ_QUESTIONS_PART_FOR_TEXT_SEARCH[1] = "//div[contains(text(),'" + question + "')]"
        try:
            self.browser.find_element(*locators.MainPageLocators.FAQ_QUESTIONS_PART_FOR_TEXT_SEARCH)
        except NoSuchElementException:
            return False
        return True

    @allure.step('проверяем, появился ли ответ на него')
    def is_faq_answer_correct_and_visible(self, answer):
        locators.MainPageLocators.FAQ_ANSWERS[1] = ""
        locators.MainPageLocators.FAQ_ANSWERS[1] = "//p[contains(text(),'" + answer + "')]"
        try:
            self.browser.find_element(*locators.MainPageLocators.FAQ_ANSWERS)
        except NoSuchElementException:
            return False
        return self.browser.find_element(*locators.MainPageLocators.FAQ_ANSWERS).is_displayed()
