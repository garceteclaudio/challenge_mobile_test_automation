from appium.webdriver.common.appiumby import AppiumBy
from pages.BasePage import BasePage

class LocalizationPage(BasePage):
    noPermitirButton = (AppiumBy.XPATH, "//*[contains(@text, 'No permitir')]")
    finalizadoButton = (AppiumBy.XPATH, "//*[contains(@text, 'Finalizado')]")

    def __init__(self, driver):
        super().__init__(driver)

    def click_notificaciones_button(self):
        self.click_element_if_present(self.noPermitirButton, timeout=2)

    def click_finalizado_button(self):
        self.click_element_if_present(self.finalizadoButton, timeout=2)