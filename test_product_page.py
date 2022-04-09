
  
import email
from .pages.main_page import MainPage
from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage
import pytest



@pytest.mark.need_review
@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                   pytest.param
                                  ("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",marks=pytest.mark.xfail),
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
def test_guest_can_add_product_to_basket(browser, link):
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()
    add_item = ProductPage(browser, browser.current_url)
    add_item.add_item_to_bascket()
    add_item.solve_quiz_and_get_code()
    add_item.check_item_name()
    add_item.check_item_price()


link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    add_item = ProductPage(browser, link)
    add_item.open()
    add_item.add_item_to_bascket()
    add_item.should_not_be_success_message()


def test_guest_cant_see_success_message(browser):
    add_item = ProductPage(browser, link)
    add_item.open()
    add_item.should_not_be_success_message()


@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    add_item = ProductPage(browser, link)
    add_item.open()
    add_item.add_item_to_bascket()
    add_item.should_not_be_success_message_is_disappeared()


def test_guest_should_see_login_link_on_product_page(browser):
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
    page.should_be_login_link()


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    basket_page = BasketPage(browser, link)
    basket_page.open()
    basket_page.go_to_basket()
    basket_page.should_be_empty_basket()
    basket_page.should_be_empty_basket_message()



def test_guest_cant_not_see_product_in_basket_opened_from_product_page(browser):
    basket_page = BasketPage(browser, link)
    basket_page.open()
    basket_page.go_to_basket()
    basket_page.should_not_be_empty_basket()
    basket_page.should_not_be_empty_basket_message()



@pytest.mark.registered_user
class TestUserAddToBasketFromProductPage():

    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser, timeout=5):
        link = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
        self.browser = browser
        self.browser.implicitly_wait(timeout)
        self.login = LoginPage(browser, link)
        self.login.go_to_login_page()
        self.login.open()
        email, password = self.login.make_email_and_pass()
        self.login.register_new_user(email,password)

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        page = MainPage(browser, link)
        page.open()
        add_item = ProductPage(browser, browser.current_url)
        add_item.add_item_to_bascket()
        #add_item.solve_quiz_and_get_code()
        add_item.check_item_name()
        add_item.check_item_price()

    @pytest.mark.xfail
    def test_user_cant_see_success_message(self, browser):
        add_item = ProductPage(browser, link)
        add_item.open()
        add_item.should_not_be_success_message()

    