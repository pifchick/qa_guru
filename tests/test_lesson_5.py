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
    browser.element('.text-center').should(have.text('Practice Form'))
    browser.element('//*[@id="firstName"]').should(be.blank)
    browser.element('//*[@id="firstName"]').type('Anton')
    browser.element('//*[@id="lastName"]').should(be.blank)
    browser.element('//*[@id="lastName"]').type('Pifchi')
    browser.element('//*[@id="userEmail"]').should(be.blank)
    browser.element('//*[@id="userEmail"]').type('123@mail.ru')
    browser.element('//*[@id="genterWrapper"]/div[2]/div[1]').click() #нужно переделать локатор
    browser.element('//*[@id="userNumber"]').should(be.blank)
    browser.element('//*[@id="userNumber"]').type('89000000001')
    browser.element('//*[@id="dateOfBirthInput"]').click()
    browser.element('.react-datepicker__month-select [value="3"]').click()
    browser.element('.react-datepicker__year-select [value="2000"]').click()
    browser.element('//*[@id="dateOfBirth"]/div[2]/div[2]/div/div/div[2]/div[2]/div[3]/div[4]').click() #нужно переделать локатор





    # time.sleep(5)