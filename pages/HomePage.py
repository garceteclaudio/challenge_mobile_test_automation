from appium.webdriver.common.appiumby import AppiumBy
from pages.BasePage import BasePage

class HomePage(BasePage):

    buscarEnAmazonText = (AppiumBy.ID, "com.amazon.mShop.android.shopping:id/chrome_search_hint_view")



    def __init__(self, driver):
        super().__init__(driver)

    def get_buscar_en_amazon_text(self):
        return self.get_element_text(self.buscarEnAmazonText)


    def send_text_to_search_input(self, text):
        self.send_keys(self.buscarEnAmazonText, text)