import pytest
import time

from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage
from .pages.login_page import generate_random_email
from .pages.product_page import Links


class TestUserAddToBasketFromProductPage:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link = Links.MAIN_PAGE
        page = LoginPage(browser, link)
        page.open()
        page.go_to_login_page()

        email = generate_random_email()
        password = "SomePassword123456789"

        page.register_new_user(email, password)

        page.should_be_authorized_user()

    def test_user_cant_see_product_in_basket_opened_from_product_page(self, browser):
        link = Links.THE_CITY_AND_THE_STARS_95_PAGE
        product_page = ProductPage(browser, link)
        product_page.open()
        product_page.go_to_basket_page()

        basket_page = BasketPage(browser, browser.current_url)
        basket_page.should_not_be_any_products_in_the_basket()
        basket_page.should_be_empty_basket_text()

    def test_user_can_add_product_to_basket(self, browser):
        link = Links.THE_CITY_AND_THE_STARS_95_PAGE
        product_page = ProductPage(browser, link)
        product_page.open()

        initial_product_name = product_page.get_initial_product_name()
        initial_product_price = product_page.get_initial_product_price()

        product_page.add_product_to_basket()
        # product_page.solve_quiz_and_get_code()

        product_page.should_be_correct_product_name(initial_product_name)
        product_page.should_be_correct_price(initial_product_price)

# @pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
#                                   pytest.param(
#                                       "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
#                                       marks=pytest.mark.xfail),
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
# def test_guest_can_add_product_to_basket(browser, link):
#     product_page = ProductPage(browser, link)
#     product_page.open()
#
#     initial_product_name = product_page.get_initial_product_name()
#     initial_product_price = product_page.get_initial_product_price()
#
#     product_page.add_product_to_basket()
#     product_page.solve_quiz_and_get_code()
#
#     time.sleep(240)
#
#     product_page.should_be_correct_product_name(initial_product_name)
#     product_page.should_be_correct_price(initial_product_price)


# def test_guest_should_see_login_link_on_product_page(browser):
#     link = Links.THE_CITY_AND_THE_STARS_95_PAGE
#     product_page = ProductPage(browser, link)
#     product_page.open()
#     product_page.should_be_login_link()
#
#
# def test_guest_can_go_to_login_page_from_product_page(browser):
#     link = Links.THE_CITY_AND_THE_STARS_95_PAGE
#     product_page = ProductPage(browser, link)
#     product_page.open()
#     product_page.go_to_login_page()

# def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
#     link = Links.THE_CITY_AND_THE_STARS_95_PAGE
#     product_page = ProductPage(browser, link)
#     product_page.open()
#     product_page.go_to_basket_page()
#
#     basket_page = BasketPage(browser, browser.current_url)
#     basket_page.should_not_be_any_products_in_the_basket()
#     basket_page.should_be_empty_basket_text()
