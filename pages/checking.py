import allure
from pages.base import Base


class Checking(Base):
    @allure.step("Проверяем текст в элементе")
    def check_text(self, element, expected_text):
        message = self.browser.find_element(*element).text
        assert message == expected_text
