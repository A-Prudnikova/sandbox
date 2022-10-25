from selene.support.shared import browser
from selene import have


def test():
    browser.open('https://demoqa.com/automation-practice-form')
    browser.element('#userName-label').should(have.text('Name'))
