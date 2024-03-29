from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure
from base.base_class import Base
from tests.logger import Logger


class CardPage(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    checkout_button = ".checkout_button"

    # Getters

    def get_checkout_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.checkout_button)))


    # Actions
    def checkout_button_click(self):
        self.get_checkout_button().click()
        print("click checkaut button")
    # Method

    def product_confirm(self):
        Logger.add_start_step(method="product_confirm")
        with allure.step("product_confirm"):
            print("checkaut page")
            self.checkout_button_click()
            self.get_current_url()
        Logger.add_end_step(url=self.driver.current_url, method="product_confirm")