from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.links import Links


def test_guest_can_go_to_login_page(browser):
    # Задаём переменную link для url (для наглядности), берём её из енума
    link = Links.MAIN_PAGE

    # Создаём объект page класса MainPage, используя конструктор, описанный в BasePage
    page = MainPage(browser, link)

    # Вызываем метод open (описан в BasePage), чтобы зайти на нужную страницу по полю url,
    # которое инициализировано в конструкторе
    page.open()

    # Переходим на страницу с авторизацией
    page.go_to_login_page()

    # Создаём объект класса LoginPage, используя текущий url, до которого дошли с использованием объекта page
    login_page = LoginPage(browser, browser.current_url)

    # Проверяем, что все необходимые элементы страницы с авторизацией на месте
    login_page.should_be_login_page()


def test_guest_should_see_login_link(browser):
    # Создаём объект класса MainPage и заходим по нужному url
    link = Links.MAIN_PAGE
    page = MainPage(browser, link)
    page.open()

    # Проверяем наличие ссылки на страницу с авторизацией
    page.should_be_login_link()
