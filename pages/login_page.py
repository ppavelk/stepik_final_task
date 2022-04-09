from .base_page import BasePage
from .locators import LoginPageLocators
import time


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_URL), 'Login url is not presented'
        self.browser.find_element(*LoginPageLocators.LOGIN_URL).click()
        assert "login" in self.browser.current_url, "There isn`t login in url"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), 'Login form is not presented'
        

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), 'Register form is not presented'

    def make_email_and_pass(self):
        # генерация почты и передача пароля
        return (str(time.time()) + "@mail.ru", "Pass123")

    def register_new_user(self, email, password):
        
        self.browser.find_element(*LoginPageLocators.EMAIL_FOR_REGISTRATIOM).send_keys(email)
        self.browser.find_element(*LoginPageLocators.PASSWORD_FOR_REGISTRATION).send_keys(password)
        self.browser.find_element(*LoginPageLocators.CONFIRM_PASSWORD_FOR_REGISTRATION).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON).click()
   