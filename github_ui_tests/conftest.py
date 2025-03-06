import pytest
from selene import browser


@pytest.fixture(params=[(1920, 1080), (390, 844)])
def setup_browser(request):
    """Настройка размера окна браузера и определение типа устройства"""
    width, height = request.param
    browser.config.window_width = width
    browser.config.window_height = height
    device_type = "desktop" if width > 1024 else "mobile"
    yield device_type
    browser.quit()


@pytest.fixture
def desktop_resolution():
    """Фикстура для десктопного режима"""
    browser.config.window_width = 1920
    browser.config.window_height = 1080
    yield
    browser.quit()


@pytest.fixture
def mobile_resolution():
    """Фикстура для мобильного режима"""
    browser.config.window_width = 390
    browser.config.window_height = 844
    yield
    browser.quit()
