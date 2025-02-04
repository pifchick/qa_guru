from selene import browser, query
from selene import have

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
    text1 = browser.element('[id="xdget89548_1_1"]').get(query.text)
    assert text1 == 'Регистрация', f"Ошибка! Ожидали другое"
    assert text1 != 'Авторизация', f"Ошибка! Ожидали другое"

