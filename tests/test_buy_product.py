import allure
from selenium import webdriver
from pages.card_page import CardPage
from pages.client_info_page import ClientInfoPage
from pages.finish_page import FinishPage
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.payment_page import PaymentPage

class TestBuyProduct():
    driver = webdriver.Chrome()
    login = LoginPage(driver)
    main_page = MainPage(driver)
    card_page = CardPage(driver)
    client_info = ClientInfoPage(driver)
    payment_page = PaymentPage(driver)
    finish_page = FinishPage(driver)

    def setup(self):
        self.login.authorisation()
    @allure.description("test_buy_first_product")
    def test_buy_first_product(self):
        self.main_page.select_product_one()
        self.card_page.product_confirm()
        self.client_info.input_information()
        self.payment_page.payment()
        self.finish_page.screenshot()

    @allure.description("test_buy_second")
    def test_buy_second_product(self):
        self.main_page.select_product_second()
        self.card_page.product_confirm()
        self.client_info.input_information()
        self.payment_page.payment()
        self.finish_page.screenshot()

    @allure.description("test_buy_three")
    def test_buy_three_product(self):
        self.main_page.select_product_three()
        self.card_page.product_confirm()
        self.client_info.input_information()
        self.payment_page.payment()
        self.finish_page.screenshot()