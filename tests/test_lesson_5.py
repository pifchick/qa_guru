"""
Сделать автоматизацию для https://demoqa.com/automation-practice-form
with_(timeout=4.0) - используется для того чтобы определнный шаг теста ждал сколько-то сек, пример:
 browser.all('...').with_(timeout=4.0).should(have.size(3))
"""
import time

from selene import browser, have, be


def test_pozitive_case():
    browser.config.base_url = 'https://demoqa.com/automation-practice-form'
    browser.open('/')
    browser.element('.text-center').should(have.text('Practice Form'))#command + b
    #browser.element('//*[@id="firstName"]').should(be.blank) 16 строчка это повторение
    browser.element('//*[@id="firstName"]').wait.for_(be.blank)
    browser.element('//*[@id="firstName"]').type('Anton')
    browser.element('//*[@id="lastName"]').should(be.blank)
    browser.element('//*[@id="lastName"]').type('Pifchi')
    browser.element('//*[@id="userEmail"]').should(be.blank)
    browser.element('//*[@id="userEmail"]').type('123@mail.ru')
    browser.element('.col-md-9 [value="Male"]').with_(click_by_js=True).click() #Костыль через js
    browser.element('//*[@id="userNumber"]').should(be.blank)
    browser.element('//*[@id="userNumber"]').type('89000000001')

    browser.element('//*[@id="dateOfBirthInput"]').click()
    browser.element('.react-datepicker__month-select [value="3"]').click() #April
    browser.element('.react-datepicker__year-select [value="2000"]').click()
    browser.element('[aria-label="Choose Tuesday, April 11th, 2000"]').click()

    browser.element('#subjectsInput').click().type('Engli').press_enter().type('Ch').press_enter()
    browser.all('[class="css-1rhbuit-multiValue subjects-auto-complete__multi-value"]').should(have.exact_texts('English', 'Chemistry'))

    #Если не закоментить эти две строчки, то воспроизводится баг формы
    # browser.element('[class="css-xb97g8 subjects-auto-complete__multi-value__remove"]').click()
    # browser.element('[class="css-xb97g8 subjects-auto-complete__multi-value__remove"]').click()


    browser.element('#hobbies-checkbox-3').with_(click_by_js=True).click()

    # browser.element('#uploadPicture').click()



    #time.sleep(5)