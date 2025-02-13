from pickle import FALSE

import pytest
from selene import browser
from selenium import webdriver

#For all test and browesrs
@pytest.fixture(scope= "function", autouse=True)
def browser_timeout():
    browser.config.timeout = 8

@pytest.fixture(scope="function",  autouse=False)
def main_fixture(browser_timeout, browser_open_and_quit):
    browser.config.driver.set_window_size(1920, 1080)

#for Chrome browser
@pytest.fixture(scope="function", autouse=False)
def browser_open_and_quit():
    browser.open('https://school.qa.guru/cms/system/login')
    driver_options = webdriver.ChromeOptions() # Задаем в каком бразере
    driver_options.add_argument('--headless') # Выключает отображение браузера
    browser.config.driver_options = driver_options # Передаем конфигарцию в config.driver_options
    yield
    #browser.driver.delete_all_cookies() - надо доделать
    browser.quit()

#For yandex browser
@pytest.fixture(scope= "function", autouse=False)
def browser_yandex_open_and_quit():
    # browser.config.driver_name = 'chrome' #Или так
    driver_options = webdriver.FirefoxOptions() # Задаем в каком бразере, надо разобрать как яндекс добавить
    driver_options.add_argument('--headless') # Выключает отображение браузера
    browser.config.driver_options = driver_options
    browser.open('https://ya.ru/')

    yield
    #browser.driver.delete_all_cookies() - надо доделать
    browser.quit()

