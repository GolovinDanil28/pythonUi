from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base


class MainPage(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    link_product_one = "//a[@id='item_4_title_link']"
    link_product_two = "//a[@id='item_0_title_link']"
    link_product_three = "//a[@id='item_1_title_link']"
    product_one = "//button[@class ='btn_primary btn_inventory']"
    card = ".fa-layers svg.svg-inline--fa"
    burger_menu = ".bm-burger-button"
    about_item_menu = "//a[@id='about_sidebar_link']"
    # Getters

    def get_link_product_one(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.link_product_one)))

    def get_link_product_two(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.link_product_two)))

    def get_link_product_three(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.link_product_three)))
    def get_add_card(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.product_one)))

    def get_card(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.card)))

    def get_burger_menu(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.burger_menu)))
    def get_about_item_menu(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.about_item_menu)))

    # Actions

    def click_link_product_one(self):
        self.get_link_product_one().click()
    def click_link_product_two(self):
        self.get_link_product_two().click()
    def click_link_product_three(self):
        self.get_link_product_three().click()
    def click_btn_add_card(self):
        self.get_add_card().click()
        print("Select product one")

    def click_card_product(self):
        self.get_card().click()
        print("Select product")
    def click_burger_menu(self):
        self.get_burger_menu().click()
        print("click burger menu")

    def click_about_item_menu(self):
        self.get_about_item_menu().click()
        print("click burger menu")

    # Method

    def select_product_one(self):
        self.click_link_product_one()
        self.get_current_url()
        self.click_btn_add_card()
        self.click_card_product()
        self.get_current_url()

    def select_product_second(self):
        self.click_link_product_two()
        self.get_current_url()
        self.click_btn_add_card()
        self.click_card_product()
        self.get_current_url()
    def select_product_three(self):
        self.click_link_product_three()
        self.get_current_url()
        self.click_btn_add_card()
        self.click_card_product()
        self.get_current_url()

    def select_item_menu(self):
        self.click_burger_menu()
        self.click_about_item_menu()
        self.get_current_url()
        self.asser_url("https://saucelabs.com/")