import pytest
from selene import browser, Browser, Config
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from utils import attach


def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        help="Браузер для запуска тестов",
        choices=["firefox", "chrome"],
        default="chrome"
    )
    parser.addoption(
        "--browser_version",
        help="Версия браузера",
        default="100.0"
    )
    parser.addoption(
        "--remote_browser",
        help="Адрес удаленного браузера",
        default="https://user1:1234@selenoid.autotests.cloud/wd/hub"
    )


@pytest.fixture(scope="session")
def setup_browser(request):
    browser.config.window_width = 1600
    browser.config.window_height = 1200
    browser_name = request.config.getoption("--browser")
    browser_version = request.config.getoption("--browser_version")
    remote_browser = request.config.getoption("--remote_browser")

    options = Options()
    selenoid_capabilities = {
        "browserName": browser_name,
        "browserVersion": browser_version,
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": True
        }
    }
    options.capabilities.update(selenoid_capabilities)
    driver = webdriver.Remote(
        command_executor=remote_browser,
        options=options
    )

    browser.config.driver = driver

    yield browser

    attach.add_screenshot(browser)
    attach.add_logs(browser)
    attach.add_html(browser)
    attach.add_video(browser)

    browser.quit()
