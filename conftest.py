import pytest
from selenium import webdriver


@pytest.fixture()
def set_up(self):
    url = 'https://www.saucedemo.com/v1/'
    print("Start main test")
    driver = webdriver.Chrome()
    driver.get(url)
    driver.maximize_window()

    yield
    driver.quit()