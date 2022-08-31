from selenium.webdriver.common.by import By


class MainLocators:
    enter_button = (
        By.XPATH,
        "/html/body/main/div[2]/div[1]/div[2]/div/div[1]/button",
    )


class LoginLocators:
    login_frame = (By.XPATH, "//iframe[@class='ag-popup__frame__layout__iframe']")
    account_field = (By.XPATH, "//input[@class='input-0-2-71']")
    enter_password_button = (By.XPATH, "//button[@class='base-0-2-79 primary-0-2-93']")
    password_field = (By.XPATH, "//input[@class='input-0-2-71 withIcon-0-2-72']")
    enter_button = (By.XPATH, "//button[@class='base-0-2-79 primary-0-2-93']")


class InboxLocators:
    close_promo = (
        By.CSS_SELECTOR,
        "#ph-whiteline > div > div.ph-projects.svelte-1sqx1fm > div:nth-child(3) > div > "
        "a > div.ph-project-promo-close-icon.svelte-m7oyyo > div",
    )
    write_letter = (By.XPATH, "//span[@class='compose-button__wrapper']")
    field_to = (By.XPATH, "//label[@class='container--zU301']")
    field_theme = (By.XPATH, "//input[@name='Subject']")
    send_button = (By.XPATH, "//span[@class='inner-0-2-16 innerTextWrapper-0-2-17']")
    success_send_message = (By.XPATH, "//div[@class='layer__header']")
