from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators():
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRICE_IN_BASKET = (By.CSS_SELECTOR, "div.basket-mini.pull-right.hidden-xs")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main>p.price_color")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main>h1")
    ADDED_PRODUCT_NAME = (By.CSS_SELECTOR, ".alert-success>.alertinner>strong")
