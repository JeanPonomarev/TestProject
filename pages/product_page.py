from .base_page import BasePage
from .locators import ProductPageLocators
from .links import Links


class ProductPage(BasePage):
    def add_product_to_basket(self):
        add_to_basket_button = self.browser.find_element(*ProductPageLocators.BASKET_BUTTON)
        add_to_basket_button.click()

    def should_be_correct_product_name(self, initial_name):
        name_after_adding_to_basket = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_AFTER_ADDING).text
        assert initial_name == name_after_adding_to_basket, f"Initial name {initial_name} is not equals to name after adding {name_after_adding_to_basket}"

    def should_be_correct_price(self, initial_price):
        price_after_adding_to_basket = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE_AFTER_ADDING).text
        assert initial_price == price_after_adding_to_basket, f"Initial price {initial_price} is not equals to price after adding {price_after_adding_to_basket}"

    def get_initial_product_name(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME)
        product_name_text = product_name.text
        return product_name_text

    def get_initial_product_price(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE)
        product_price_text = product_price.text
        return product_price_text
