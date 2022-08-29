from selenium.webdriver import Keys
from pages.main import *


class Inbox(Main):
    def send_email(self):
        self.open_mail_ru()
        self.login()
        self.browser.find_element(*InboxLocators.write_letter).click()
        self.wait_for_element(InboxLocators.field_to)
        self.browser.find_element(*InboxLocators.field_to).send_keys(Main.email)
        self.browser.find_element(*InboxLocators.field_theme).send_keys(
            f"Hello world!{Keys.TAB}{Keys.TAB}This  is "
            f"autotest,\ndo not response :)"
        )
        self.browser.find_element(*InboxLocators.send_button).click()
        self.wait_for_element(InboxLocators.success_send_message)
