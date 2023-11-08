from selene.support.shared import browser
from selene import be, have
import pytest


@pytest.fixture
def browser_management():
    browser.config.window_width = 412
    browser.config.window_height = 915

    yield browser
    browser.quit()


def test_search(browser_management):
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))


def test_not_find(browser_management):
    browser.open('https://google.com')
    srch='vnfeiwubvrwiucvhmriewbhxtniwuhrebvnciuwmbvx'
    browser.element('[name="q"]').should(be.blank).type(srch).press_enter()
    browser.element('.card-section').should(have.text('По запросу ' + srch + ' ничего не найдено.'))
