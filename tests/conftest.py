import time

import pytest
from selene import browser
from selene import have


@pytest.fixture()
def browser_open_and_quit():
    browser.open('https://school.qa.guru/cms/system/login')
    yield
    browser.quit()

@pytest.fixture(scope= "session")
def browser_timeout():
    browser.config.timeout = 8


@pytest.fixture(scope="function")
def main_fixture(browser_timeout, browser_open_and_quit):
    browser.config.driver.set_window_size(1280, 1080)

