from pages.base import Base
from pages.locators import *


class Main(Base):
    main_url = "https://mail.ru/"
    email = "testasdfghjkl123@mail.ru"
    password = "asdfghjkl;'"

    def open_mail_ru(self):
        self.open(Main.main_url)

    def login(self):
        self.open_mail_ru()
        self.wait_for_element(MainLocators.enter_button)
        self.find_and_click(MainLocators.enter_button)
        self.wait_for_element(LoginLocators.login_frame)
        self.switch_to_frame(LoginLocators.login_frame)
        self.wait_for_element(LoginLocators.account_field)
        self.find_and_send(LoginLocators.account_field, Main.email)
        self.find_and_click(LoginLocators.enter_password_button)
        self.wait_for_element(LoginLocators.password_field)
        self.find_and_send(LoginLocators.password_field, Main.password)
        self.find_and_click(LoginLocators.enter_button)
        self.wait_for_element(InboxLocators.close_promo)
        self.find_and_click(InboxLocators.close_promo)
