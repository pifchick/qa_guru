import pytest
from selene import browser

#For all test and browesrs
@pytest.fixture(scope= "function", autouse=True)
def browser_timeout():
    browser.config.timeout = 8

@pytest.fixture(scope="function",  autouse=False)
def main_fixture(browser_timeout, browser_open_and_quit):
    browser.config.driver.set_window_size(1280, 1080)


#for Chrome browser
@pytest.fixture(scope="function", autouse=False)
def browser_open_and_quit():
    browser.open('https://school.qa.guru/cms/system/login')
    yield
    #browser.driver.delete_all_cookies() - надо доделать
    browser.quit()

#For yandex browser
@pytest.fixture(scope= "function", autouse=False)
def browser_yandex_open_and_quit():
    browser.open('https://ya.ru/')
    yield
    #browser.driver.delete_all_cookies() - надо доделать
    browser.quit()

