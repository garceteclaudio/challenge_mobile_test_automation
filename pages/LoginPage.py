from appium.webdriver.common.appiumby import AppiumBy
from pages.BasePage import BasePage


class LoginPage(BasePage):
    # Locators
    USERNAME_FIELD = (AppiumBy.ACCESSIBILITY_ID, "username")
    PASSWORD_FIELD = (AppiumBy.ID, "com.example.app:id/password")
    LOGIN_BUTTON = (AppiumBy.XPATH, "//android.widget.Button[@text='LOGIN']")
    ERROR_MESSAGE = (AppiumBy.ID, "com.example.app:id/error_message")

    def __init__(self, driver):
        super().__init__(driver)

    def enter_username(self, username):
        """Ingresa el nombre de usuario"""
        self.send_keys(self.USERNAME_FIELD, username)
        return self  # Permite method chaining

    def enter_password(self, password):
        """Ingresa la contraseña"""
        self.send_keys(self.PASSWORD_FIELD, password)
        return self  # Permite method chaining

    def click_login_button(self):
        """Hace click en el botón de login"""
        self.click_element(self.LOGIN_BUTTON)
        return self  # Permite method chaining

    def login(self, username, password):
        """Método completo para realizar login"""
        (self.enter_username(username)
         .enter_password(password)
         .click_login_button())
        return self

    def get_error_message(self):
        """Obtiene el mensaje de error si existe"""
        if self.is_element_visible(self.ERROR_MESSAGE):
            return self.get_element_text(self.ERROR_MESSAGE)
        return None