from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_cart(self):
        add_to_cart_button = self.browser.find_element(*ProductPageLocators.ADD_TO_CART_BUTTON)
        add_to_cart_button.click()

    def get_basket_price(self):
        raw_price_in_basket = self.browser.find_element(*ProductPageLocators.PRICE_IN_BASKET).text
        splited_price_in_basket = raw_price_in_basket.split()
        return splited_price_in_basket[2]

    def get_product_price(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text

    def compare_product_price_and_basket_price(self):
        assert self.get_product_price() == self.get_basket_price(), "Product price is no equal price from basket"

    def get_product_name(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text

    def get_added_product_name(self):
        return self.browser.find_element(*ProductPageLocators.ADDED_PRODUCT_NAME).text

    def compare_product_name_and_added_product_name(self):
        assert self.get_product_name() == self.get_added_product_name(), "Product name is no equal added product name"
