import pytest
from selene import browser, by
import logging

logging.basicConfig(level=logging.INFO)


def test_desktop(setup_browser):
    if setup_browser == "mobile":
        logging.info("Пропуск теста: мобильное разрешение не подходит для десктопного теста.")
        pytest.skip("Мобильное разрешение не подходит.")
    browser.open("https://github.com")
    browser.element(by.text("Sign up for GitHub")).click()
    logging.info("Клик по кнопке 'Sign up for GitHub' на десктопе.")


def test_mobile(setup_browser):
    if setup_browser == "desktop":
        logging.info("Пропуск теста: десктопное разрешение не подходит для мобильного теста.")
        pytest.skip("Десктопное разрешение не подходит.")
    browser.open("https://github.com")
    browser.element(by.text("Sign up for GitHub")).click()
    logging.info("Клик по кнопке 'Sign up for GitHub' на мобильном устройстве.")

