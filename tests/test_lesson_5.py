"""
Сделать автоматизацию для https://demoqa.com/automation-practice-form
with_(timeout=4.0) - используется для того чтобы определнный шаг теста ждал сколько-то сек, пример:
 browser.all('...').with_(timeout=4.0).should(have.size(3))

 setTimeout('debugger', 3_000)
"""

import os.path
import time

from selene import browser, have, be, command
from selenium.webdriver.common.devtools.v85.dom import scroll_into_view_if_needed


def test_all_rows_case():
    browser.config.base_url = 'https://demoqa.com'
    browser.open('/automation-practice-form')

    browser.element('.text-center').should(have.text('Practice Form'))  # command + b
    # browser.element('//*[@id="firstName"]').should(be.blank) 16 строчка это повторение
    browser.element('#firstName').wait.for_(be.blank)
    browser.element('#firstName').type('Anton')
    browser.element('#lastName').should(be.blank).type('Pifchi')
    browser.element('#userEmail').should(be.blank).type('123@mail.ru')
    # browser.element('.col-md-9 [value=Male]').with_(
    #     click_by_js=True
    # ).click()  # Костыль через js
    browser.all('[name=gender]').element_by(have.value('Female')).element('..').click()
    browser.element('#userNumber').should(be.blank).type('89000000001')

    browser.element('#dateOfBirthInput').click()
    # browser.element('.react-datepicker__month-select [value="3"]').click()
    browser.element('[class*=month-select]').send_keys('April')
    browser.element('[class*=year-select]').send_keys('2000')
    # browser.element('[aria-label="Choose Tuesday, April 11th, 2000"]').click()
    browser.element('[class*=week] [class*=day--011][aria-label*=April]').click()

    browser.element('#subjectsInput').click().type('English').press_enter().type(
        'Chemistry'
    ).press_enter()
    # browser.all(
    #     '[class="css-1rhbuit-multiValue subjects-auto-complete__multi-value"]'
    # ).should(have.exact_texts('English', 'Chemistry'))
    browser.element('[class^=subjects-auto-complete]').all(
        '[class*=value-container]'
    ).element_by(have.exact_texts('English', 'Chemistry'))
    # Если не закоментить эти две строчки, то воспроизводится баг формы
    # browser.element('[class="css-xb97g8 subjects-auto-complete__multi-value__remove"]').click()
    # browser.element('[class="css-xb97g8 subjects-auto-complete__multi-value__remove"]').click()
    browser.element('#hobbies-checkbox-3').with_(click_by_js=True).click()

    # file_selection = browser.element('.form-control-file')
    # file_selection.send_keys(
    #     '/Users/locadmin/PycharmProjects/web_e2e/file_for_tests/kit.jpeg'
    # )
    import tests

    browser.element('#uploadPicture').set_value(
        os.path.abspath(
            os.path.join(
                os.path.dirname(tests.__file__),
                os.path.pardir,
                'file_for_tests/kit.jpeg',  # os.path.pardir - поднимаемся на один уровень вверх
            )
        )
    )

    browser.element('#currentAddress').should(be.blank).type('Moscow never sleep')

    # browser.execute_script("window.scrollBy(0, 300);")
    browser.element('#state').perform(command.js.scroll_into_view).click()
    browser.element('#react-select-3-option-1').click()
    browser.element('#city').click()
    browser.element('#react-select-4-option-1').click()

    browser.element('#submit').should(be.visible).click()

    browser.element('#example-modal-sizes-title-lg').click()
    browser.all('.table-responsive').should(
        have.exact_texts(
            'Label Values\n'
            'Student Name Anton Pifchi\n'
            'Student Email 123@mail.ru\n'
            'Gender Female\n'
            'Mobile 8900000000\n'
            'Date of Birth 11 April,2000\n'
            'Subjects English, Chemistry\n'
            'Hobbies Music\n'
            'Picture kit.jpeg\n'
            'Address Moscow never sleep\n'
            'State and City Uttar Pradesh Lucknow'
        )
    )
    browser.element('#closeLargeModal').click()


def test_required_fields():
    browser.config.base_url = 'https://demoqa.com/automation-practice-form'
    browser.open('/')
    browser.element('.text-center').should(have.text('Practice Form'))  # command + b
    browser.element('#firstName').should(be.blank).type('Anton')
    browser.element('#lastName').should(be.blank).type('Pifchi')
    browser.element('.col-md-9 [value="Male"]').with_(
        click_by_js=True
    ).click()  # Костыль через js
    browser.element('#userNumber').should(be.blank).type('89000000001')

    browser.element('#dateOfBirthInput').click()
    browser.element('[class*=month-select]').send_keys('April')
    browser.element('[class*=year-select]').send_keys('2000')
    browser.element('[class*=week] [class*=day--011][aria-label*=April]').click()

    browser.execute_script("window.scrollBy(0, 300);")
    browser.element('#submit').click()

    browser.element('#example-modal-sizes-title-lg').click()
    browser.all('.table-responsive').should(
        have.exact_texts(
            'Label Values\n'
            'Student Name Anton Pifchi\n'
            'Student Email\n'
            'Gender Male\n'
            'Mobile 8900000000\n'
            'Date of Birth 11 April,2000\n'
            'Subjects\n'
            'Hobbies\n'
            'Picture\n'
            'Address\n'
            'State and City'
        )
    )
    browser.element('#closeLargeModal').click()
