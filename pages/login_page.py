from .base_page import BasePage
from .locators import LoginPageLocators
import random
import string
from .links import Links


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        current_link = self.browser.current_url
        assert "login" in current_link, "Wrong URL has been found"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"

    # регистрация пользователя
    def register_new_user(self, email, password):
        self.go_to_login_page()

        email_field = self.browser.find_element(*LoginPageLocators.EMAIL_FIELD)
        email_field.send_keys(email)

        password1 = self.browser.find_element(*LoginPageLocators.PASSWORD1)
        password1.send_keys(password)

        password2 = self.browser.find_element(*LoginPageLocators.PASSWORD2)
        password2.send_keys(password)

        register_button = self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON)
        register_button.click()


def generate_random_email():
    domains = ["gmail.com", "mail.ru", "yahoo.com", "aol.com"]
    letters = string.ascii_lowercase[:12]

    random_domain = random.choice(domains)
    random_name = ''.join(random.choice(letters) for i in range(10))

    return [random_name + '@' + random_domain]
