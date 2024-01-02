import datetime


class Base():
    def __init__(self, driver):
        self.driver = driver

    """Method GET current url"""

    def get_current_url(self):
        get_url = self.driver.current_url
        print("current url" + get_url)

    """Method asserd equel text """
    def asser_word(self, word, result):
        value_world = word.text
        assert value_world == result
        print("Good value word")


    """Method Screenshot"""
    def screenshot(self):
        now_date = datetime.datetime.utcnow().strftime("%Y.%m.%d.%H.%M.%S")
        name_screenshot = 'screenshot' + now_date + '.png'
        self.driver.save_screenshot('.\\screenshot' + name_screenshot)

    """Method asserd url"""
    def asser_url(self,result):
        get_url = self.driver.current_url
        assert get_url == result
        print("Good value url")