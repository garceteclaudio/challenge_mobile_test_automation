from behave import *
from asserts import assert_true, assert_equal, assert_raises
from pages.HomePage import HomePage

@then(u'the user should be redirected to the Home section')
def step_impl(context):
    context.home_page = HomePage(context.driver)
    assert_equal("Buscar en Amazon", context.home_page.get_buscar_en_amazon_text())

@when('the user search a product "{product}"')
def step_impl(context, product):
    context.home_page.send_text_to_search_input(product)

@then(u'the user should see a list of products')
def step_impl(context):
    items = context.home_page.list_of_products()
    assert(items>0)
