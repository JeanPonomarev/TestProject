from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_not_be_any_products_in_the_basket(self):
        assert self.is_not_element_present(
            *BasketPageLocators.ANY_PRODUCTS), "There are some items in the basket without customer's choice"

    def should_be_empty_basket_text(self):
        basket_message = self.browser.find_element(*BasketPageLocators.EMPTY_BASKET_MESSAGE).text
        assert "Your basket is empty" in basket_message, "Something wrong with empty basket message"
