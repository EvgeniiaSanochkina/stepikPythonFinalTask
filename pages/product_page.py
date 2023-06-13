from .base_page import BasePage
from .locators import MainPageLocators
from .locators import LoginPageLocators

class ProductPage(BasePage):
    def should_be_add_to_basket(self):
        basket_link = self.browser.find_element(*MainPageLocators.BASKET)
        basket_link.click()



