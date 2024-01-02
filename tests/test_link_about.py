from selenium import webdriver
from pages.card_page import CardPage
from pages.client_info_page import ClientInfoPage
from pages.finish_page import FinishPage
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.payment_page import PaymentPage

def test_link_about():
        driver = webdriver.Chrome()
        print("start tests")
        login = LoginPage(driver)
        main_page = MainPage(driver)
        login.authorisation()
        main_page.select_item_menu()