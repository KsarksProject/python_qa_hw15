import pytest
from selene import browser, by


@pytest.mark.parametrize("desktop_resolution", [(1920, 1080)], indirect=True)
def test_desktop(desktop_resolution):
    browser.open("http://github.com")
    browser.element(by.text("Sign up for GitHub")).click()


@pytest.mark.parametrize("mobile_resolution", [(390, 844)], indirect=True)
def test_mobile(mobile_resolution):
    browser.open("http://github.com")
    browser.element(by.text("Sign up for GitHub")).click()
