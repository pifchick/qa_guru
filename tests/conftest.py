import pytest
from selene import browser
from selenium import webdriver


@pytest.fixture(scope="function", autouse=True)
def main_fixture(browser_conf):
    browser.config.timeout = 3.0


# for Chrome browser
@pytest.fixture(scope="function", autouse=False)
def browser_conf():
    driver_options = webdriver.ChromeOptions()  # Задаем в каком бразере
    # driver_options.add_argument('--headless') # Выключает отображение браузера
    browser.config.driver_options = (
        driver_options  # Передаем конфигарцию в config.driver_options
    )
    # browser.config.driver.set_window_size(1920, 1080) Не работает так как отрабаывает раньше и мешает открыть сайт

    yield
    # browser.driver.delete_all_cookies() - надо доделать
    browser.quit()
