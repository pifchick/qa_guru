"""
Сделать автоматизацию для https://demoqa.com/automation-practice-form
with_(timeout=4.0) - используется для того чтобы определнный шаг теста ждал сколько-то сек, пример:
 browser.all('...').with_(timeout=4.0).should(have.size(3))
"""
import time

from selene import browser, have, be
from selenium.webdriver.common.devtools.v85.dom import scroll_into_view_if_needed


def test_all_rows_case():
    browser.config.base_url = 'https://demoqa.com/automation-practice-form'
    browser.open('/')
    browser.element('.text-center').should(have.text('Practice Form'))#command + b
    #browser.element('//*[@id="firstName"]').should(be.blank) 16 строчка это повторение
    browser.element('//*[@id="firstName"]').wait.for_(be.blank)
    browser.element('//*[@id="firstName"]').type('Anton')
    browser.element('//*[@id="lastName"]').should(be.blank).type('Pifchi')
    browser.element('//*[@id="userEmail"]').should(be.blank).type('123@mail.ru')
    browser.element('.col-md-9 [value="Male"]').with_(click_by_js=True).click() #Костыль через js
    browser.element('//*[@id="userNumber"]').should(be.blank).type('89000000001')

    browser.element('//*[@id="dateOfBirthInput"]').click()
    browser.element('.react-datepicker__month-select [value="3"]').click() #April
    browser.element('.react-datepicker__year-select [value="2000"]').click()
    browser.element('[aria-label="Choose Tuesday, April 11th, 2000"]').click()

    browser.element('#subjectsInput').click().type('Engli').press_enter().type('Ch').press_enter()
    browser.all('[class="css-1rhbuit-multiValue subjects-auto-complete__multi-value"]').should(have.exact_texts(
        'English',
                'Chemistry'
    ))
    #Если не закоментить эти две строчки, то воспроизводится баг формы
    # browser.element('[class="css-xb97g8 subjects-auto-complete__multi-value__remove"]').click()
    # browser.element('[class="css-xb97g8 subjects-auto-complete__multi-value__remove"]').click()
    browser.element('#hobbies-checkbox-3').with_(click_by_js=True).click()

    file_selection = browser.element('.form-control-file')
    file_selection.send_keys('/Users/locadmin/PycharmProjects/web_e2e/file_for_tests/kit.jpeg')

    browser.element('#currentAddress').should(be.blank).type('Moscow never sleep')

    browser.execute_script("window.scrollBy(0, 300);")
    browser.element('#state').click()
    browser.element('#react-select-3-option-1').click()
    browser.element('#city').click()
    browser.element('#react-select-4-option-1').click()

    browser.element('#submit').should(be.visible).click()

    browser.element('#example-modal-sizes-title-lg').click()
    browser.all('.table-responsive').should(have.exact_texts(
        'Label Values\n'
        'Student Name Anton Pifchi\n'
        'Student Email 123@mail.ru\n'
        'Gender Male\n'
        'Mobile 8900000000\n'
        'Date of Birth 11 April,2000\n'
        'Subjects English, Chemistry\n'
        'Hobbies Music\n'
        'Picture kit.jpeg\n'
        'Address Moscow never sleep\n'
        'State and City Uttar Pradesh Lucknow'
    ))
    browser.element('#closeLargeModal').click()

def test_required_fields():
    browser.config.base_url = 'https://demoqa.com/automation-practice-form'
    browser.open('/')
    browser.element('.text-center').should(have.text('Practice Form'))  # command + b
    browser.element('//*[@id="firstName"]').should(be.blank).type('Anton')
    browser.element('//*[@id="lastName"]').should(be.blank).type('Pifchi')
    browser.element('.col-md-9 [value="Male"]').with_(click_by_js=True).click() #Костыль через js
    browser.element('//*[@id="userNumber"]').should(be.blank).type('89000000001')
    browser.execute_script("window.scrollBy(0, 300);")
    browser.element('#submit').click()

    browser.element('#example-modal-sizes-title-lg').click()
    browser.all('.table-responsive').should(have.exact_texts(
        'Label Values\n'
        'Student Name Anton Pifchi\n'
        'Student Email\n'
        'Gender Male\n'
        'Mobile 8900000000\n'
        'Date of Birth 17 February,2025\n'
        'Subjects\n'
        'Hobbies\n'
        'Picture\n'
        'Address\n'
        'State and City'
    ))
    browser.element('#closeLargeModal').click()

