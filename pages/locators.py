from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_URL = (By.CSS_SELECTOR, "#login_link")
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    EMAIL_FOR_REGISTRATIOM = (By.CSS_SELECTOR, "#id_registration-email")
    PASSWORD_FOR_REGISTRATION = (By.CSS_SELECTOR, "#id_registration-password1")
    CONFIRM_PASSWORD_FOR_REGISTRATION = (By.CSS_SELECTOR, "#id_registration-password2")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")
    REGISTER_BUTTON = (By.CSS_SELECTOR, "#register_form button")
    EMAIL_ERROR = (By.CSS_SELECTOR, ".error-block")


class ProductPageLocators():
    ADD_TO_BASKET = (By.CSS_SELECTOR, "#add_to_basket_form button")
    ITEM_NAME = (By.CSS_SELECTOR, "#content_inner h1")
    ADDED_ITEM_NAME = (By.CSS_SELECTOR, "#messages strong")  
    ITEM_PRICE = (By.CSS_SELECTOR, "#content_inner p")
    ADDED_ITEM_PRICE = (By.CSS_SELECTOR, "#messages strong")  
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages > div:nth-child(1)")

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    VIEW_BASKET_BUTTON = (By.CSS_SELECTOR, "div.basket-mini.pull-right.hidden-xs > span a")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class BasketPageLocators():
    BASKET_ITEMS = (By.CSS_SELECTOR, "#content_inner p")
