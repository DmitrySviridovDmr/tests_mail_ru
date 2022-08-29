from pages.inbox import *
import allure
from pages.checking import Checking


class TestInbox:
    @staticmethod
    @allure.title("Тест на успешную отправку письма")
    @allure.description("Авторизуемся под тестовым пользователем и отправляем письмо")
    def test_send_email(browser):
        page = Inbox(browser)
        page.send_email()
        check = Checking(browser)
        check.check_text(InboxLocators.success_send_message, "Письмо отправлено")
