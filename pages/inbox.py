from selenium.webdriver import Keys
from pages.main import *


class Inbox(Main):
    def send_email(self):
        self.open_mail_ru()
        self.login()
        self.find_and_click(InboxLocators.write_letter)
        self.wait_for_element(InboxLocators.field_to)
        self.find_and_send(InboxLocators.field_to, Main.email)
        self.find_and_send(
            InboxLocators.field_theme,
            f"Hello world!{Keys.TAB}{Keys.TAB}This  is "
            f"autotest,\ndo not response :)",
        )
        self.find_and_click(InboxLocators.send_button)
        self.wait_for_element(InboxLocators.success_send_message)
