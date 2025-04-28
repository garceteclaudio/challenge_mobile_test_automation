from appium.webdriver.common.appiumby import AppiumBy
from pages.BasePage import BasePage

class PasswordPage(BasePage):

    passwordInput = (AppiumBy.XPATH, "//*[@resource-id='ap_password']")
    #iniciarSesionButton = (AppiumBy.ID, "signInSubmit")
    iniciarSesionButton = (AppiumBy.XPATH, "//*[@resource-id='signInSubmit']")


    def __init__(self, driver):
        super().__init__(driver)

    def send_password_to_input(self, text):
        self.send_keys(self.passwordInput, text)

    def click_iniciar_sesion_button(self):
        self.click_element(self.iniciarSesionButton)