from pages.inbox import *
import allure


class TestInbox:
    @allure.title("Тест на успешную отправку письма")
    def test_send_email(self, browser):
        page = Inbox(browser)
        page.send_email()
        assert browser.find_element(*InboxLocators.success_send_message).text == "Письмо отправлено"
