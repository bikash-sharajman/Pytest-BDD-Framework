import time
from behave import given, when, then
from behave.exception import StepNotImplementedError
from selenium.webdriver.support import expected_conditions as ec
from src.locators.subcat_mstr_locators import subcategory_elements
from src.locators.common_locators import commonelements
from selenium.webdriver.common.by import By



@given(u'User navigates to sub category module')
def step_impl(context):
    try:
        context.log.info("Navigating to sub category module from sidebar.")
        context.wait.until(ec.element_to_be_clickable(commonelements.side_bar)).click()
        context.wait.until(ec.element_to_be_clickable(commonelements.master_menu)).click()
        context.wait.until(ec.element_to_be_clickable(commonelements.sub_category_master)).click()
        context.wait.until(ec.element_to_be_clickable(commonelements.side_bar)).click()
        context.wait.until(ec.url_contains("category-master"))
    except Exception as e:
        context.log.error(f"Navigation to sub category module failed: {e}")
        raise


@when(u'User clicks on add subcategory button')
def step_impl(context):
    context.wait.until(ec.element_to_be_clickable(subcategory_elements.add_sub_category_btn)).click()
    time.sleep(5)
    context.wait.until(ec.visibility_of_element_located(subcategory_elements.subCat_input))


@when(u'User selects category "{category_name}"')
def step_impl(context, category_name):
    context.wait.until(ec.element_to_be_clickable(subcategory_elements.subCat_category_dd)).click()
    time.sleep(1)
    option_locator = By.XPATH,f"//p-selectitem//li//span[normalize-space()='{category_name}']"
    time.sleep(1)
    context.wait.until(ec.element_to_be_clickable(option_locator)).click()

@when(u'User enters name "{subcategory_name}"')
def step_impl(context, subcategory_name):
    context.wait.until(ec.element_to_be_clickable(subcategory_elements.subCat_input)).send_keys(subcategory_name)


@then(u'User should see sub category created success message')
def step_impl(context):
    toast = context.wait.until(ec.element_to_be_clickable(commonelements.toaster))
    assert "Sub Category added Successfully" in toast.text, "Expected toaster message does not displayed."

@given(u'sub category "Demo sub category" exists')
def step_impl(context):
    pass

@then(u'User should see the sub category details page')
def step_impl(context):
    assert context.wait.until(ec.visibility_of_element_located(subcategory_elements.view_subcat_modal))

# @then(u'the name should be "Demo sub category"')
# def step_impl(context):
#     raise StepNotImplementedError(u'Then the name should be "Demo sub category"')   


@when(u'User clear and enter name "{updated_sub_category_name}"')
def step_impl(context, updated_sub_category_name):
    sub_cat_input = context.wait.until(ec.element_to_be_clickable(subcategory_elements.subCat_input))
    sub_cat_input.clear()
    sub_cat_input.send_keys(updated_sub_category_name)

@then(u'User should see sub category updated success message')
def step_impl(context):
    toast = context.wait.until(ec.element_to_be_clickable(commonelements.toaster))
    assert "Sub Category updated successfully" in toast.text, "Expected toaster does not dispalyed."

# @given(u'sub category "Demo sub category updated" exists')
# def step_impl(context):
#     raise StepNotImplementedError(u'Given sub category "Demo sub category updated" exists')


@then(u'User should see sub category deleted success message')
def step_impl(context):
    toast = context.wait.until(ec.element_to_be_clickable(commonelements.toaster))
    assert "Sub Category removed successfully" in toast.text, "Expected toaster does not dispalyed."
    
@then(u'sub category Validation message "{validation_message}" should be displayed')
def step_impl(context, validation_message):
    validation_text = context.wait.until(ec.visibility_of_element_located\
        (subcategory_elements.category_field_value_required_message)).text.strip()
    assert validation_text == validation_message, (
        f'Expected validation text "{validation_message}", but got "{validation_text}".')


@then(u'sub category Toaster message contains "{subcategory_toatermessage}" should be displayed')
def step_impl(context, subcategory_toatermessage):
    toast = context.wait.until(ec.visibility_of_element_located(commonelements.toaster))
    time.sleep(1)
    toast_text = toast.text
    assert f"{subcategory_toatermessage}" in toast_text, (
        f'Expected "{subcategory_toatermessage}" in toaster, but got: {toast_text}')
    context.wait.until(ec.invisibility_of_element_located(commonelements.toaster))