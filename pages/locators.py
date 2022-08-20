from selenium.webdriver.common.by import By


class MainLocators:
    main_url = "https://mail.ru/"
    enter_button = (By.CSS_SELECTOR, "#mailbox > div.logged-out-one-click.svelte-hjx44n > button")


class LoginLocators:
    login_frame = (By.CSS_SELECTOR, "body > div.ag_js-popup-frame.ag-popup__frame.ag-popup__frame_onoverlay.ag-popup__frame_show > div > iframe")
    account_field = (By.CSS_SELECTOR, "#root > div > div > div > div.wrapper-0-2-5 > div > div > form > div:nth-child(2) > div:nth-child(2) > div.login-row.username > div > div > div > div > div > div.base-0-2-58.first-0-2-64 > div > input")
    enter_password_button = (By.CSS_SELECTOR, "#root > div > div > div > div.wrapper-0-2-5 > div > div > form > div:nth-child(2) > div:nth-child(2) > div:nth-child(3) > div > div > div.submit-button-wrap > button")
    password_field = (By.CSS_SELECTOR, "#root > div > div > div > div.wrapper-0-2-5 > div > div > form > div:nth-child(2) > div > div.login-row.password > div > div > div > div > div > input")
    enter_button = (By.CSS_SELECTOR, "#root > div > div > div > div.wrapper-0-2-5 > div > div > form > div:nth-child(2) > div > div:nth-child(3) > div > div > div.submit-button-wrap > div > button")


class InboxLocators:
    email = "testasdfghjkl123@mail.ru"
    password = "asdfghjkl;'"
    close_promo = (By.CSS_SELECTOR, "#ph-whiteline > div > div.ph-projects.svelte-1sqx1fm > div:nth-child(3) > div > a > div.ph-project-promo-close-icon.svelte-m7oyyo > div")
    write_letter = (By.CSS_SELECTOR,  "#app-canvas > div > div.application-mail > div.application-mail__overlay > div > div.application-mail__layout.application-mail__layout_main > span > div.layout__column.layout__column_left > div.layout__column-wrapper > div > div > div > div:nth-child(1) > div > div > a > span > span")
    field_to = (By.CSS_SELECTOR, "body > div:nth-child(1) > div > div.compose-app.compose-app_fix.compose-app_popup.compose-app_window.compose-app_adaptive > div > div > div > div.container--rp3CE > div.scrollview--SiHhk.scrollview_main--3Vfg9 > div.head_container--3W05z > div > div > div.wrap--2sfxq > div > div.contacts--1ofjA > div > div > label > div > div > input")
    field_theme = (By.CSS_SELECTOR, "body > div:nth-child(1) > div > div.compose-app.compose-app_fix.compose-app_popup.compose-app_window.compose-app_adaptive > div > div > div > div.container--rp3CE > div.scrollview--SiHhk.scrollview_main--3Vfg9 > div.subject__container--HWnat > div.subject__wrapper--2mk6m > div.container--3QXHv > div > input")
    send_button = (By.CSS_SELECTOR, "body > div:nth-child(1) > div > div.compose-app.compose-app_fix.compose-app_popup.compose-app_window.compose-app_adaptive > div > div > div > div.footer--2dyxG > div.buttons--2Kfbb > div:nth-child(1) > div > button")
    success_send_message = (By.CSS_SELECTOR, ".layer__link")
