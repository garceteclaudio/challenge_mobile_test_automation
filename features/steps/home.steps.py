from behave import *
from asserts import assert_true, assert_equal, assert_raises
from pages.HomePage import HomePage

@then(u'the user should be redirected to the Home section')
def step_impl(context):
    context.home_page = HomePage(context.driver)
    assert_equal("Buscar en Amazon", context.home_page.get_buscar_en_amazon_text())
    context.home_page.sleep(2)