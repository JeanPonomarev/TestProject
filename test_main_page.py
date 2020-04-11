from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.links import Links


def test_guest_can_go_to_login_page(browser):
    link = Links.MAIN_PAGE
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()


def test_guest_should_see_login_link(browser):
    link = Links.MAIN_PAGE
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()


def test_guest_should_see_right_login_page(browser):
    link = Links.LOGIN_PAGE
    page = LoginPage(browser, link)
    page.open()
    page.should_be_login_page()
