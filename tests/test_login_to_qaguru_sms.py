from selene import browser
from selene import have
#import time
#time.sleep(3)
#browser.config.hold_driver_at_exit = True #Only selenium 4.5.0

browser.config.timeout = 8
def teardown_function():
    browser.quit()

def test_login_pozitive():
    browser.open('https://school.qa.guru/cms/system/login')
    browser.element('.login-form [name=email]').type('anton200061@gmail.com').press_tab()
    browser.element('.login-form [name=password]').type('Anton366').press_tab().press_enter()
    browser.element('.gc-account-leftbar [title=Профиль]').click()
    browser.element('[class=menu-item-profile]').click()
    browser.element('[for=User_first_name]').should(have.text('Имя'))

def test_login_unluck():
    browser.open('https://school.qa.guru/cms/system/login')
    browser.element('.login-form [name=email]').type('anton200061@gmail.com').press_tab()
    browser.element('.login-form [name=password]').type('hyu').press_tab().press_enter()
    browser.element('.login-form .btn-success').should(have.exact_text('Неверный пароль'))