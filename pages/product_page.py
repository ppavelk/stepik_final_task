from .locators import ProductPageLocators
from .base_page import BasePage


class ProductPage(BasePage):
    def should_be_promo_in_url(self):
        assert self.browser.current_url.find("?promo=newYear"), "Wrong URL"

    def add_item_to_bascket(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET), "Add button is not presented"
        add_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        add_button.click()

    def check_item_name(self):
        item_name = self.browser.find_element(*ProductPageLocators.ITEM_NAME).text
        added_item_name = self.browser.find_elements(*ProductPageLocators.ADDED_ITEM_NAME)[0].text
        assert item_name == added_item_name, "Item name:" + item_name + ". Added item name;" + added_item_name

    def check_item_price(self):
        item_price = self.browser.find_element(*ProductPageLocators.ITEM_PRICE).text
        added_item_price = self.browser.find_elements(*ProductPageLocators.ADDED_ITEM_PRICE)[2].text
        assert item_price == added_item_price, "Item price:" + item_price + ". Added item price;" + added_item_price

    def should_not_be_success_message(self):
        assert not self.is_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is presented"

    def should_not_be_success_message_is_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is presented"