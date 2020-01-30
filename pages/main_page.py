from .base_page import BasePage  # импорт базового класса
from selenium.webdriver.common.by import By


class MainPage(BasePage):  # класс главной страницы, который наследует методы и конструктор от BasePage
    def go_to_login_page(self):
        login_link = self.browser.find_element(By.CSS_SELECTOR, "#login_link")
        login_link.click()
