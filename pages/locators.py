from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators:
    BASKET_BUTTON = (By.CSS_SELECTOR, '.btn-add-to-basket')
    PRODUCT_NAME = (By.TAG_NAME, "h1")
    PRODUCT_PRICE = (By.CLASS_NAME, "price_color")
    PRODUCT_NAME_AFTER_ADDING = (By.CSS_SELECTOR, ".alert:nth-child(1) strong")
    PRODUCT_PRICE_AFTER_ADDING = (By.CSS_SELECTOR, ".alert:nth-child(3) strong")
