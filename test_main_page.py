from selenium.webdriver.common.by import By
from .pages.main_page import MainPage
from .pages.login_page import LoginPage


def go_to_login_page(browser):
    login_link = browser.find_element(By.CSS_SELECTOR, "#login_link")
    login_link.click()

def no_test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()  # открываем страницу
    page.go_to_login_page() # выполняем метод страницы — переходим на страницу логина
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()
def no_test_guest_should_see_login_link(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()

def no_test_should_see_login_in_urlString(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()  # открываем страницу
    link1 = page.go_to_login_page()
    pageLogin = LoginPage(browser, link1)
    pageLogin.should_be_login_url()

def no_test_should_see_login_form(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()  # открываем страницу
    link1 = page.go_to_login_page()
    pageLogin = LoginPage(browser, link1)
    pageLogin.should_be_login_form()

def no_test_should_see_registration_form(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()  # открываем страницу
    link1 = page.go_to_login_page()
    pageLogin = LoginPage(browser, link1)
    pageLogin.should_be_register_form()


