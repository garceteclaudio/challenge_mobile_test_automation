from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 15)  # Espera de hasta 15 segundos

    def find_element(self, locator):
        """Encuentra un elemento usando WebDriverWait"""
        return self.wait.until(EC.presence_of_element_located(locator))

    def find_elements(self, locator):
        """Encuentra múltiples elementos usando WebDriverWait"""
        return self.wait.until(EC.presence_of_all_elements_located(locator))

    def click_element(self, locator):
        """Hace click en un elemento después de esperar a que sea clickeable"""
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()

    def send_keys(self, locator, text):
        """Envía texto a un elemento después de esperar a que sea visible"""
        element = self.wait.until(EC.visibility_of_element_located(locator))
        element.clear()
        element.send_keys(text)

    def is_element_visible(self, locator):
        """Verifica si un elemento es visible"""
        try:
            return self.wait.until(EC.visibility_of_element_located(locator))
        except Exception:
            return False

    def get_element_text(self, locator):
        """Obtiene el texto de un elemento"""
        element = self.wait.until(EC.visibility_of_element_located(locator))
        return element.text