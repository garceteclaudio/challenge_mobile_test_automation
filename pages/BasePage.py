import time
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 15)  # Espera máxima general

    def is_element_present(self, locator, timeout=9):
        """Verifica si un elemento está presente dentro de un tiempo específico"""
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located(locator)
            )
            return True
        except TimeoutException:
            return False

    def click_element_if_present(self, locator, timeout=9):
        """Hace click en un elemento si está presente, sino continúa sin error"""
        if self.is_element_present(locator, timeout):
            self.click_element(locator)
        else:
            print("Elemento: ", locator, " no encontrado.")
        return self

    def sleep(self, seconds):
        """Espera fija (usar solo cuando sea estrictamente necesario)"""
        print("Dormir: ", seconds)
        time.sleep(seconds)
        return self

    def find_element(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    def find_elements(self, locator):
        return self.wait.until(EC.presence_of_all_elements_located(locator))

    def click_element(self, locator):
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()
        return self

    def send_keys(self, locator, text):
        element = self.wait.until(EC.visibility_of_element_located(locator))
        element.clear()
        element.send_keys(text)
        return self

    def is_element_visible(self, locator, timeout=None):
        try:
            wait = self.wait if timeout is None else WebDriverWait(self.driver, timeout)
            return wait.until(EC.visibility_of_element_located(locator))
        except TimeoutException:
            return False

    def get_element_text(self, locator):
        element = self.wait.until(EC.visibility_of_element_located(locator))
        return element.text

    def press_keycode(self, keycode):
        self.driver.press_keycode(keycode)