from selene import browser
from selene import have
#import time
#time.sleep(3)
#browser.config.hold_driver_at_exit = True #Only selenium 4.5.0




def test_login_pozitive(main_fixture):
    browser.element('.login-form [name=email]').type('anton200061@gmail.com').press_tab()
    browser.element('.login-form [name=password]').type('Anton366').press_tab().press_enter()
    browser.element('.gc-account-leftbar [title=Профиль]').click()
    browser.element('[class=menu-item-profile]').click()
    browser.element('[for=User_first_name]').should(have.text('Имя'))

def test_login_unluck(main_fixture):
    browser.element('.login-form [name=email]').type('anton200061@gmail.com').press_tab()
    browser.element('.login-form [name=password]').type('hyu').press_tab().press_enter()
    browser.element('.login-form .btn-success').should(have.exact_text('Неверный пароль'))


def test_registration(main_fixture):
    browser.element('.btn-register').click()
    browser.element('.register-form  .form-field-email .form-field-email').type('pupkin@yandex.ru').press_tab()
    browser.element('.register-form .field-input-block .form-field-full_name').type('Епифан Гриша Владимирович')
#пока не работает browser.element('.html-content [href="/cms/system/contact"]').should(have.exact_texts('Обратная связь'))
#надо пробовать assert browser.element('checkbox-text').should(have.exact_text('Я согласен на обработку моих персональных данных в соответствии с ')) !=  browser.element('checkbox-text').should(have.exact_text('обработку моих персональных данных в соответствии с '))



    #time.sleep(8)