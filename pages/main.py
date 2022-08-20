from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from pages.base import Base
from pages.locators import *


class Main(Base):
    def open_mail_ru(self):
        self.browser.get(MainLocators.main_url)

    def login(self):
        self.open_mail_ru()
        WebDriverWait(self.browser, 5).until(ec.visibility_of_element_located(MainLocators.enter_button))
        self.browser.find_element(*MainLocators.enter_button).click()
        WebDriverWait(self.browser, 5).until(ec.visibility_of_element_located(LoginLocators.login_frame))
        self.browser.switch_to.frame(self.browser.find_element(*LoginLocators.login_frame))
        WebDriverWait(self.browser, 5).until(ec.visibility_of_element_located(LoginLocators.account_field))
        self.browser.find_element(*LoginLocators.account_field).send_keys(*InboxLocators.email)
        self.browser.find_element(*LoginLocators.enter_password_button).click()
        WebDriverWait(self.browser, 10).until(ec.visibility_of_element_located(LoginLocators.password_field))
        self.browser.find_element(*LoginLocators.password_field).send_keys(*InboxLocators.password)
        self.browser.find_element(*LoginLocators.enter_button).click()
        WebDriverWait(self.browser, 10).until(ec.visibility_of_element_located(InboxLocators.close_promo))
        self.browser.find_element(*InboxLocators.close_promo).click()
