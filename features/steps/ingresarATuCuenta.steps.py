from behave import *
from asserts import assert_true, assert_equal, assert_raises
from pages.IngresaATuCuentaPage import IngresaATuCuentaPage

@then('the user should see Ingresar a tu cuenta section')
def step_impl(context):
    context.ingresa_a_tu_cuenta_page = IngresaATuCuentaPage(context.driver)
    assert_equal("Ingresar a tu cuenta", context.ingresa_a_tu_cuenta_page.get_ingresar_a_tu_cuenta_text())

@when('the user taps on ¿Ya eres cliente? Iniciar sesion. button')
def step_impl(context):
    context.ingresa_a_tu_cuenta_page.click_ya_eres_cliente_button()

@when('the user enters "{credentials}"')
def step_impl(context, credentials):
    print("credentials: ", credentials)

@then(u'the user should be redirected to the Home section')
def step_impl(context):
    ...

