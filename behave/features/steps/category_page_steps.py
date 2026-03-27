import time
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as ec
from src.locators.category_mstr_locators import category
from src.locators.common_locators import commonelements


@given(u'User navigates to Category module')
def step_impl(context):
    try:
        context.log.info("Navigating to make module from sidebar.")
        context.wait.until(ec.element_to_be_clickable(commonelements.side_bar)).click()
        context.wait.until(ec.element_to_be_clickable(commonelements.master_menu)).click()
        context.wait.until(ec.element_to_be_clickable(commonelements.category_master)).click()
        context.wait.until(ec.element_to_be_clickable(commonelements.side_bar)).click()
        context.wait.until(ec.url_contains("category-master"))
    except Exception as e:
        context.log.error(f"Navigation to make module failed: {e}")
        raise


@when(u'User click on add category button')
def step_impl(context):
    context.wait.until(ec.element_to_be_clickable(category.add_category)).click()
    context.wait.until(ec.visibility_of_element_located(category.category_input))


@when(u'User enter category name "{category_name}"')
def step_impl(context, category_name):
    context.wait.until(ec.element_to_be_clickable(category.category_input)).send_keys(category_name)

@then(u'User should see category created success message')
def step_impl(context):
    toast = context.wait.until(ec.visibility_of_element_located(commonelements.toaster))
    toast.text
    assert "New Category created successfully" in toast.text, f"Incorrect toaster message appeared - {toast.text}"


@given(u'category "Test category" exists')
def step_impl(context):
    pass


@then(u'User should see the category details page')
def step_impl(context):
    assert context.wait.until(ec.visibility_of_element_located(category.view_category_modal))
    time.sleep(2)
    context.wait.until(ec.element_to_be_clickable(commonelements.modal_cancel_button)).click()


@then(u'the category name should be "Test category"')
def step_impl(context):
    value = context.wait.until(ec.element_to_be_clickable(category.category_input)).get

@when(u'User clear and enter category name "{updated_category_name}"')
def step_impl(context, updated_category_name):
    input_field = context.wait.until(ec.element_to_be_clickable(category.category_input))
    input_field.clear()
    input_field.send_keys(updated_category_name)
    

@then(u'User should see category updated success message')
def step_impl(context):
    toast = context.wait.until(ec.element_to_be_clickable(commonelements.toaster))
    time.sleep(1)
    toast_text = toast.text.strip()
    assert "Category updated successfully" in toast_text or "success" in toast_text, (
        f"Expected update success toaster, but got: {toast_text}")
    context.wait.until(ec.invisibility_of_element_located(commonelements.toaster))

# @then(u'the category "Test category Updated" should be visible in the list')
# def step_impl(context):
#     raise StepNotImplementedError(u'Then the category "Test category Updated" should be visible in the list')


@given(u'category "Test category Updated" exists')
def step_impl(context):
    pass

# @when(u'User search for category "Test category Updated"')
# def step_impl(context):


@then(u'User should see "{delete_toaster}" success message')
def step_impl(context, delete_toaster):
    toast = context.wait.until(ec.element_to_be_clickable(commonelements.toaster))
    time.sleep(1)
    toast_text = toast.text.strip()
    assert delete_toaster in toast_text or "success" in toast_text, (
        f"Expected update success toaster, but got: {toast_text}")
    context.wait.until(ec.invisibility_of_element_located(commonelements.toaster))

@then(u'"Test category Updated" should not be visible in the list')
def step_impl(context):
    pass