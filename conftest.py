import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


# Добавьте в файл contest.py обработчик, который считывает из командной строки параметр language.
def pytest_addoption(parser):
    parser.addoption('--language', action='store', default="en",
                     help="Choose language: ru, eng...")

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()

    yield browser
    print("\nquit browser..")
    browser.quit()





