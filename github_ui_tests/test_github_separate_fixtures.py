from selene import browser, by
import logging

logging.basicConfig(level=logging.INFO)


def test_desktop(desktop_resolution):
    browser.open("https://github.com")
    logging.info("Открыта главная страница GitHub на десктопе.")
    browser.element(by.text("Sign up for GitHub")).click()
    logging.info("Клик по кнопке 'Sign up for GitHub'.")


def test_mobile(mobile_resolution):
    browser.open("https://github.com")
    logging.info("Открыта главная страница GitHub на мобильном устройстве.")
    browser.element(by.text("Sign up for GitHub")).click()
    logging.info("Клик по кнопке 'Sign up for GitHub'.")
