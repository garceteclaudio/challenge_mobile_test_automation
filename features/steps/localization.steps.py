from behave import *
from pages.LocalizationPage import LocalizationPage

@given(u'the user opens the Amazon app')
def step_impl(context):
    context.localization_page = LocalizationPage(context.driver)

@when(u'the user selects country and language preferences')
def step_impl(context):
    ...

@when(u'the user taps on Finalizado button')
def step_impl(context):
    context.localization_page.click_notificaciones_button()
    context.localization_page.click_finalizado_button()
