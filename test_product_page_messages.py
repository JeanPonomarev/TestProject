from .pages.product_page import ProductPage
from .pages.links import Links


def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = Links.SHELLCODERS_HANDBOOK_PAGE

    product_page = ProductPage(browser, link)
    product_page.open()

    product_page.add_product_to_basket()

    product_page.should_not_be_success_message()


def test_guest_cant_see_success_message(browser):
    link = Links.SHELLCODERS_HANDBOOK_PAGE

    product_page = ProductPage(browser, link)
    product_page.open()

    product_page.should_not_be_success_message()


def test_message_disappeared_after_adding_product_to_basket(browser):
    link = Links.SHELLCODERS_HANDBOOK_PAGE

    product_page = ProductPage(browser, link)
    product_page.open()

    product_page.add_product_to_basket()

    product_page.element_should_disappear()
