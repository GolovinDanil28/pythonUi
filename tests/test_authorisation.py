from selenium import webdriver
from pages.login_page import LoginPage

def test_first():
    driver = webdriver.Chrome()
    print("start tests")

    login = LoginPage(driver)
    login.authorisation()
