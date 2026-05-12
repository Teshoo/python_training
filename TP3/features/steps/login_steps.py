from behave import *

@given(u"the user is on the login page")
def step_impl(context):
    context.login_page.open(context.login_page.URL)
    context.login_page.wait_login_form_to_be_visible()
    assert context.login_page.get_login_form() is not None, f"Login form should be visible"

@when(u"the user log in with their {username} and their {password}")
def step_impl(context, username, password):
    context.login_page.login(username, password)
    
@then(u"the user is connected")
def step_impl(context):
    assert context.inventory_page.PATH in context.driver.current_url
    
@then(u"the user is on the catalogue page")
def step_impl(context):
    context.inventory_page.wait_inventory_list_to_be_visible()
    assert context.inventory_page.get_inventory_list() is not None