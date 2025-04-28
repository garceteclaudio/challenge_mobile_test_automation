from behave import *
from asserts import assert_true, assert_equal, assert_raises
from pages.UserPage import UserPage


@when('the user enters a valid email adress "{credentials}"')
def step_impl(context, credentials):
    context.user_page = UserPage(context.driver)
    context.user_page.send_email_to_input(credentials)

@when('the user taps on Continuar button')
def step_impl(context):
    context.user_page.click_continuar_button()