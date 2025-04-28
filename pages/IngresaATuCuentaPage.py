from appium.webdriver.common.appiumby import AppiumBy
from pages.BasePage import BasePage


class IngresaATuCuentaPage(BasePage):
    ingresarATuCuentaText = (AppiumBy.XPATH, "//*[contains(@text, 'Ingresar a tu cuenta')]")
    omitirInicioDeSesionButton = (AppiumBy.XPATH, "//*[contains(@text, 'Omitir inicio de sesión')]")
    yaEresClienteButton = (AppiumBy.ID, "com.amazon.mShop.android.shopping:id/sign_in_button")


    def __init__(self, driver):
        super().__init__(driver)

    def click_ya_eres_cliente_button(self):
        self.click_element(self.yaEresClienteButton)
        #self.click_element(self.yaEresClienteButton)
    def tap_omitir_inicio_de_sesion_button(self):
        self.click_element(self.omitirInicioDeSesionButton)
    def get_ingresar_a_tu_cuenta_text(self):
        return self.get_element_text(self.ingresarATuCuentaText)
