from pages.main import *
import allure
from pages.checking import Checking


class TestMain:
    @staticmethod
    @allure.title(f"Smoke тест открытия главной страницы {Main.main_url}")
    @allure.description(
        f"Открываем главную страницу {Main.main_url} и проверяем что страница открылась"
    )
    def test_open_mail_ru(browser):
        page = Main(browser)
        page.open_mail_ru()
        check = Checking(browser)
        check.check_text(MainLocators.enter_button, "Войти")

    @staticmethod
    @allure.title("Тест на успешную авторизацию")
    @allure.description("Проверяем авторизацию под тестовым пользователем")
    def test_login(browser):
        page = Main(browser)
        page.login()
        check = Checking(browser)
        check.check_text(InboxLocators.write_letter, "Написать письмо")
