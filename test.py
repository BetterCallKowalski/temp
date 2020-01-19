import time
from selenium.webdriver.chrome.webdriver import WebDriver

chrome = WebDriver(executable_path='/mnt/c/selenium/chromedriver.exe')

chrome.get("https://yandex.ru")

chrome.find_element_by_css_selector('.input__control.input__input').send_keys("nice cats")

time.sleep(3)

chrome.find_element_by_css_selector('.button.button_theme_websearch').click()


time.sleep(5)

chrome.quit()
