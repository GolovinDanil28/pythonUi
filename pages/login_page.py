from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base


class LoginPage(Base):
    url = 'https://www.saucedemo.com/v1/'


    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    # Locators

    user_name= "//input[@id = 'user-name']"
    user_password = "//input[@id='password']"
    login_button = "//input[@id = 'login-button']"
    main_world = "//div[@class='product_label']"

    # Getters

    def get_user_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.user_name)))

    def get_user_password(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.user_password)))

    def get_login_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.login_button)))
    def get_main_word(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.main_world)))

    # Actions

    def input_user_name(self, user_name):
        self.get_user_name().send_keys(user_name)
        print("input user name")

    def input_user_password(self, password):
        self.get_user_password().send_keys(password)
        print("input user password")

    def click_login_button(self):
        self.get_login_button().click()
        print("login button click")


    def authorisation(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.get_current_url()
        self.input_user_name("standard_user")
        self.input_user_password("secret_sauce")
        self.click_login_button()
        self.asser_word(self.get_main_word(), "Products")