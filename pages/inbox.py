from selenium.webdriver import Keys
from pages.main import *


class Inbox(Main):
    def send_email(self):
        self.open_mail_ru()
        self.login()
        self.browser.find_element(*InboxLocators.write_letter).click()
        WebDriverWait(self.browser, 5).until(ec.visibility_of_element_located(InboxLocators.field_to))
        self.browser.find_element(*InboxLocators.field_to).send_keys(*InboxLocators.email)
        self.browser.find_element(*InboxLocators.field_theme).send_keys(f"Hello world!{Keys.TAB}{Keys.TAB}This  is autotest,\ndo not response :)")
        self.browser.find_element(*InboxLocators.send_button).click()
        WebDriverWait(self.browser, 5).until(ec.visibility_of_element_located(InboxLocators.success_send_message))
