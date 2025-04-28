from appium.webdriver.common.appiumby import AppiumBy
from pages.BasePage import BasePage

class UserPage(BasePage):
    iniciarSesionOCrearUnaCuentaText = (AppiumBy.XPATH, "//*[contains(@text, 'Iniciar sesión o crear una cuenta')]")
    emailInput = (AppiumBy.XPATH, "//*[@resource-id='ap_email_login']")
    continuarButton = (AppiumBy.XPATH, "//*[contains(@text, 'Continuar')]")


    def __init__(self, driver):
        super().__init__(driver)

    def get_iniciar_sesion_o_crear_cuenta_text(self):
        return self.get_element_text(self.iniciarSesionOCrearUnaCuentaText)

    def click_continuar_button(self):
        self.click_element(self.continuarButton)


    def send_email_to_input(self, text):
        self.send_keys(self.emailInput, text)