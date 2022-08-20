from pages.main import *
import allure


class TestMain:
    @allure.title("Smoke тест открытия главной страницы mail.ru")
    def test_open_mail_ru(self, browser):
        page = Main(browser)
        page.open_mail_ru()
        assert browser.find_element(*MainLocators.enter_button).text == "Войти"

    @allure.title("Тест на успешную авторизацию")
    def test_login(self, browser):
        page = Main(browser)
        page.login()
        assert browser.find_element(*InboxLocators.write_letter).text == "Написать письмо"
