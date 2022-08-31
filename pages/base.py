from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class Base:
    def __init__(self, browser):
        self.browser = browser

    """Переходим по ссылке"""

    def open(self, url):
        self.browser.get(url)

    """Ждем элемент"""

    def wait_for_element(self, what):
        WebDriverWait(self.browser, 10).until(ec.visibility_of_element_located(what))

    """Находим и кликаем по элементу"""

    def find_and_click(self, which):
        self.browser.find_element(*which).click()

    """Находим и вводим данные в элемент"""

    def find_and_send(self, which, key):
        self.browser.find_element(*which).send_keys(key)

    """Переключаемся на Фрейм"""

    def switch_to_frame(self, which):
        self.browser.switch_to.frame(self.browser.find_element(*which))
