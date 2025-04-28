from behave import *
from asserts import assert_true, assert_equal, assert_raises
from pages.PasswordPage import PasswordPage
import os

@when('the user enters a valid password')
def step_impl(context):
    context.password_page = PasswordPage(context.driver)
    passwordEnv = os.getenv('APP_PASSWORD')
    context.password_page.send_password_to_input(passwordEnv)


@when('the user taps on Iniciar Sesion button')
def step_impl(context):
    context.password_page.click_iniciar_sesion_button()