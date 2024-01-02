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