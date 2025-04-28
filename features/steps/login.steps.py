from behave import *
#from asserts import assert_true, assert_equal, assert_raises
from pages.LoginPage import LoginPage

@given(u'the user opens the Amazon app')
def step_impl(context):
    context.login_page = LoginPage(context.driver)

@then('the user should see "{text}" section')
def step_impl(context, text):
    print("text: ", text)

@when('the user taps on "{button_text}" button')
def step_impl(context, button_text):
    print("button_text: ", button_text)

@when('the user enters "{credentials}"')
def step_impl(context, credentials):
    print("credentials: ", credentials)

@then(u'the user should be redirected to the Home section')
def step_impl(context):
    ...

