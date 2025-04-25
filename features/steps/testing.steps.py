from appium.webdriver.common.appiumby import AppiumBy
from behave import *
#from asserts import assert_true, assert_equal, assert_raises

@given('El usuario abre la app "{app_name}"')
def step_impl(context, app_name):
    print("Hola mundirijillo, app : ", app_name)