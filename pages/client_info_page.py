from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure
from base.base_class import Base
from tests.logger import Logger


class ClientInfoPage(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    # Locators

    first_name= "//input[@id='first-name']"
    last_name = "//input[@id='last-name']"
    zip_code = "//input[@id = 'postal-code']"
    continue_button = ".btn_primary"

    # Getters

    def get_first_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.first_name)))

    def get_last_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.last_name)))

    def get_zip_code(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.zip_code)))
    def get_continue_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.continue_button)))

    # Actions

    def input_first_name(self, first_name):
        self.get_first_name().send_keys(first_name)
        print("input first_name")

    def input_last_name(self, last_name):
        self.get_last_name().send_keys(last_name)
        print("input last_name")
    def input_zip_code(self, zip_code):
        self.get_zip_code().send_keys(zip_code)
        print("input zip code")
    def click_continue_button(self):
        self.get_continue_button().click()
        print("continue button click")


    def input_information(self):
        Logger.add_start_step(method="input_information")
        with allure.step("input_information"):
            self.get_current_url()
            self.input_first_name("Ivan")
            self.input_last_name("Ivanov")
            self.input_zip_code("1234")
            self.click_continue_button()
            self.get_current_url()
        Logger.add_end_step(url=self.driver.current_url, method="input_information")