from appium.webdriver.common.appiumby import AppiumBy
from pages.BasePage import BasePage
from selenium.webdriver.support import expected_conditions as EC

class HomePage(BasePage):

    buscarEnAmazonText = (AppiumBy.ID, "com.amazon.mShop.android.shopping:id/chrome_search_hint_view")
    buscarEnAmazonInput = (AppiumBy.XPATH, "//*[contains(@text, 'Buscar en Amazon')]")
    productList = (AppiumBy.XPATH, "//android.widget.ListView/*")


    def __init__(self, driver):
        super().__init__(driver)

    def get_buscar_en_amazon_text(self):
        return self.get_element_text(self.buscarEnAmazonText)


    def send_text_to_search_input(self, text):
        self.click_element(self.buscarEnAmazonText)
        self.send_keys(self.buscarEnAmazonInput, text)
        self.press_keycode(66)

    def list_of_products(self):
        items = self.find_elements(self.productList)
        for index, element in enumerate(items, start=1):
            print(f"\nElemento {index}:")
            print(f"Texto: {element.text}")
            print(f"ID: {element.id}")
            print(f"Atributos: {element.get_attribute('content-desc')}")  # Para Android
            print(f"Coordenadas: {element.location}")
            print(f"Tamaño: {element.size}")
        return len (items)


