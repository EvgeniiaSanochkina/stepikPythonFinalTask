from .base_page import BasePage #импорт базового класса BasePage
from selenium.webdriver.common.by import By
from .locators import MainPageLocators
from .login_page import LoginPage

class MainPage(BasePage): #наследник класса BasePage. Класс-предок в Python указывается в скобках

    def go_to_login_page(self):
        login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        login_link.click()
       # return LoginPage(browser=self.browser, url=self.browser.current_url)
    def should_be_login_link(self):
        #self.browser.find_element(By.CSS_SELECTOR, "#login_link_invalid")
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not presented"
