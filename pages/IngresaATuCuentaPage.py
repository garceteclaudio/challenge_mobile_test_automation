from appium.webdriver.common.appiumby import AppiumBy
from pages.BasePage import BasePage


class IngresaATuCuentaPage(BasePage):
    ingresarATuCuentaText = (AppiumBy.XPATH, "//*[contains(@text, 'Ingresar a tu cuenta')]")
    yaEresClienteButton = (AppiumBy.ID, "com.amazon.mShop.android.shopping:id/sign_in_button")


    def __init__(self, driver):
        super().__init__(driver)

    def click_ya_eres_cliente_button(self):
        self.click_element(self.yaEresClienteButton)
        #self.click_element(self.yaEresClienteButton)

    def get_ingresar_a_tu_cuenta_text(self):
        return self.get_element_text(self.ingresarATuCuentaText)
