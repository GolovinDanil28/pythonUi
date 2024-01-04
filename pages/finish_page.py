from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base
from tests.logger import Logger


class FinishPage(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
    # Method

    def finish(self):
        Logger.add_start_step(method="finish")
        self.get_current_url()
        self.screenshot()
        self.asser_url("https://www.saucedemo.com/v1/checkout-complete.html")
        Logger.add_end_step(url=self.driver.current_url, method="finish")