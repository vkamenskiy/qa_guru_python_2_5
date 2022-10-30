from selene.support.shared import browser
from selene import have, command
import os


def test_path(relative_path):
    abspath = os.path.abspath(relative_path)
    return abspathp


def test_submit_student_registration_form():
    browser.open('https://demoqa.com/automation-practice-form')
    browser.all("[id^=google_ads][id$=container__]").should(have.size_greater_than_or_equal(3))
    browser.execute_script(
        'document.querySelectorAll("[id^=google_ads][id$=container__]").forEach(element => element.remove())'
    )
    browser.execute_script('document.querySelector("footer").remove()')
    browser.element('#firstName').type('Vladislav')
    browser.element('#lastName').type('Kamenskiy')
    browser.element('#userEmail').type('dje.fry@mail.ru')
    browser.element('#gender-radio-1').perform(command.js.click)
    browser.element('#userNumber').type('9162754427')
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__year-select [value="1994"]').click()
    browser.element('.react-datepicker__month-select [value="8"]').click()
    browser.element('.react-datepicker__day--019').click()
    browser.element('#subjectsInput').type('en')
    browser.element('#react-select-2-option-0').click()
    browser.element('#hobbies-checkbox-1').perform(command.js.click)
    browser.element('#hobbies-checkbox-3').perform(command.js.click)
    browser.element('#uploadPicture').send_keys(test_path('../resources/test_pictures.webp'))
    browser.element('#currentAddress').type('Moscow Novotushinskiy proezd 8')
    browser.element('[id="state"] [class~="css-19bqh2r"]').click()
    browser.element('#react-select-3-option-1').click()
    browser.element('[id="city"] [class~="css-19bqh2r"]').click()
    browser.element('#react-select-4-option-1').click()
    browser.element('#submit').click()
