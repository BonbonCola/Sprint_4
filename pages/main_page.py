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
        button = self.browser.find_elements(*locators.to_make_order_buttons)[1]
        # Прокрути страницу до кнопки
        self.browser.execute_script("arguments[0].scrollIntoView();", button)
        time.sleep(1)
        button.click()

    @allure.step('проверка виден ли на лендинге промо текст')
    def is_marketing_block_visible(self):
        try:
            self.browser.find_element(*locators.marketing_block)
        except NoSuchElementException:
            return False
        return True

    @allure.step('скролл до списка вопросов')
    def scroll_to_faq_list(self):
        faq_list = self.browser.find_element(*locators.faq_list)
        # Прокрути страницу до списка вопросов
        self.browser.execute_script("arguments[0].scrollIntoView();", faq_list)
        time.sleep(1)

    @allure.step('клик на один из списка вопрос')
    def click_to_faq_question(self, index):
        faq_questions = self.browser.find_elements(*locators.faq_questions)
        faq_questions[index].click()
        faq_questions[index].click()

    @allure.step('сверяем текст вопроса')
    def is_text_in_faq_question_correct(self, question):
        locators.faq_questions_part_for_text_search[1] = ""
        locators.faq_questions_part_for_text_search[1] = "//div[contains(text(),'" + question + "')]"
        try:
            self.browser.find_element(*locators.faq_questions_part_for_text_search)
        except NoSuchElementException:
            return False
        return True

    @allure.step('проверяем, появился ли ответ на него')
    def is_faq_answer_correct_and_visible(self, answer):
        locators.faq_answers[1] = ""
        locators.faq_answers[1] = "//p[contains(text(),'" + answer + "')]"
        try:
            self.browser.find_element(*locators.faq_answers)
        except NoSuchElementException:
            return False
        return self.browser.find_element(*locators.faq_answers).is_displayed()
