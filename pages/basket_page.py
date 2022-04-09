from .locators import BasketPageLocators
from .base_page import BasePage


class BasketPage(BasePage):
    def should_be_empty_basket(self):
        basket_items = self.browser.find_elements(*BasketPageLocators.BASKET_ITEMS)
        print(len(basket_items))
        assert len(basket_items) == 1, "Basket is not empty"

    def should_be_empty_basket_message(self):
        basket_items = self.browser.find_element(*BasketPageLocators.BASKET_ITEMS).text
        assert "Your basket is empty." in basket_items, "There is no message about empty basket"

    def should_not_be_empty_basket(self):
        basket_items = self.browser.find_elements(*BasketPageLocators.BASKET_ITEMS)
        print(len(basket_items))
        assert not len(basket_items) == 1, "Basket is not empty"

    def should_not_be_empty_basket_message(self):
        basket_items = self.browser.find_element(*BasketPageLocators.BASKET_ITEMS).text
        assert "Your basket is empty." not in basket_items, "There is no message about empty basket"

