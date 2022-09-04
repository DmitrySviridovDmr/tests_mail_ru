import allure
from pages.base import Base
from allure_commons.types import AttachmentType


class Checking(Base):
    @allure.step("Проверяем точный текст в элементе")
    def check_text(self, element, expected_text):
        message = self.browser.find_element(*element).text
        if message == expected_text:
            assert True
        else:
            with allure.step("Делаем скриншот Бага"):
                allure.attach(self.browser.get_screenshot_as_png(), name="Ожидаемый текст не найден",
                              attachment_type=AttachmentType.PNG)
                assert False
