from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base
from tests.logger import Logger


class PaymentPage(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    # Locators

    btn_finish= "//a[@class='btn_action cart_button']"

    # Getters

    def get_btn_finish(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.btn_finish)))

    # Actions
    def click_btn_finish(self):
        self.get_btn_finish().click()
        print("finish click")

    #Method
    def payment(self):
        Logger.add_start_step(method="payment")
        self.get_current_url()
        self.click_btn_finish()
        self.get_current_url()
        Logger.add_end_step(url=self.driver.current_url, method="payment")
