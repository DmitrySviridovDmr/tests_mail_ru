from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class Base:
    def __init__(self, browser):
        self.browser = browser

    def wait_for_element(self, what):
        WebDriverWait(self.browser, 10).until(ec.visibility_of_element_located(what))
