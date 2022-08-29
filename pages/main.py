from pages.base import Base
from pages.locators import *


class Main(Base):
    main_url = "https://mail.ru/"
    email = "testasdfghjkl123@mail.ru"
    password = "asdfghjkl;'"

    def open_mail_ru(self):
        self.browser.get(Main.main_url)

    def login(self):
        self.open_mail_ru()
        self.wait_for_element(MainLocators.enter_button)
        self.browser.find_element(*MainLocators.enter_button).click()
        self.wait_for_element(LoginLocators.login_frame)
        self.browser.switch_to.frame(
            self.browser.find_element(*LoginLocators.login_frame)
        )
        self.wait_for_element(LoginLocators.account_field)
        self.browser.find_element(*LoginLocators.account_field).send_keys(Main.email)
        self.browser.find_element(*LoginLocators.enter_password_button).click()
        self.wait_for_element(LoginLocators.password_field)
        self.browser.find_element(*LoginLocators.password_field).send_keys(
            Main.password
        )
        self.browser.find_element(*LoginLocators.enter_button).click()
        self.wait_for_element(InboxLocators.close_promo)
        self.browser.find_element(*InboxLocators.close_promo).click()
