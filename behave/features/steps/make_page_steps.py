import time
from behave import given, when, then
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as ec
from pages.base_file import BasePage
from src.pages.make import MakePage
from src.initialization.config_reader import confr
from src.locators.common_locators import commonelements
from src.locators.login_locators import loginelements
from src.locators.make_mstr_locators import makemodule


def search_item(context, element: str):
    try:
        search = context.wait.until(ec.element_to_be_clickable(commonelements.search_bar))
        search.clear()
        search.send_keys(element)
        search.send_keys(Keys.ENTER)
    except Exception as e:
        context.log.error(f"{element} does not appear on search result. {e}")


@given(u'User is logged into the application')
def step_impl(context):
    try:
        context.log.info("Logging into the application.")
        url = confr.get_baseurl()
        context.driver.get(f"{url}/login")
        context.wait.until(ec.element_to_be_clickable(loginelements.email_field))\
            .send_keys("testuser100@testmail.com")
        context.wait.until(ec.element_to_be_clickable(loginelements.password_field))\
            .send_keys("Password@1234")
        context.wait.until(ec.element_to_be_clickable(loginelements.login_button)).click()
        context.wait.until(ec.url_contains("solar-plant-dashboard"))
        context.log.info("Successfully logged into the application.")
    except Exception as e:
        context.log.error(f"Login step failed: {e}")
        raise
    pass


@given(u'User navigates to make module')
def step_impl(context):
    try:
        context.log.info("Navigating to make module from sidebar.")
        context.wait.until(ec.element_to_be_clickable(commonelements.side_bar)).click()
        context.wait.until(ec.element_to_be_clickable(commonelements.master_menu)).click()
        context.wait.until(ec.element_to_be_clickable(commonelements.make_master)).click()
        context.wait.until(ec.url_contains("make"))
    except Exception as e:
        context.log.error(f"Navigation to make module failed: {e}")
        raise


@when(u'User click on add make button')
def step_impl(context):
    context.wait.until(ec.element_to_be_clickable(makemodule.add_make)).click()
    context.wait.until(ec.visibility_of_element_located(makemodule.make_input))


@when(u'User enter make name "{make_name}"')
def step_impl(context, make_name):
    make_input = context.wait.until(ec.element_to_be_clickable(makemodule.make_input))
    make_input.clear()
    make_input.send_keys(make_name)


@when(u'User click save button')
def step_impl(context):
    context.wait.until(ec.element_to_be_clickable(commonelements.modal_save_button)).click()


@then(u'User should see make created success message')
def step_impl(context):
    toast = context.wait.until(ec.visibility_of_element_located(commonelements.toaster))
    time.sleep(1)
    toast_text = toast.text.strip()
    assert "Make added successfully." in toast_text, \
        (f"Expected creation success toaster, but got: {toast_text}")
    context.wait.until(ec.invisibility_of_element_located(commonelements.toaster))


@then(u'"{element_name}" should be visible in the list')
def step_impl(context, element_name):
    assert context.wait.until(ec.visibility_of_element_located(commonelements.master_list_table))
    time.sleep(2)
    item = context.wait.until(ec.element_to_be_clickable\
        ((By.XPATH, "//p-table//ngb-highlight[text()='{element_name}']")))
    i_text = item.text
    assert i_text == element_name, "Expected item not fetched"
    
    
@given(u'make "{make_name}" exists')
def step_impl(context, make_name):
    try:
        context.log.info(f"Checking if category '{make_name}' exists")

        search_item(context, make_name)
        base = BasePage(context.driver, context.wait)
        # Verify category present in table
        element = base.verify_value_on_table(make_name)

        if element:
            context.log.info(f"Make '{make_name}' exist.")
            return
        else:
            make_page = MakePage(context.driver, context.wait)
            make_page.create_new_make(make_name)
            search_item(context, make_name)
            make_search = base.verify_value_on_table(make_name)
            assert make_search, f"Make '{make_name}' creation failed."

    except Exception as e:
        context.log.error(f"Error in Given step: {str(e)}")
        raise


@when(u'User search for "{element_name}"')
def step_impl(context, element_name):
    search_item(context, element_name)


@when(u'User click on view button')
def step_impl(context):
    time.sleep(1)
    context.wait.until(ec.element_to_be_clickable(commonelements.view_icon)).click()


@then(u'User should see the make details page')
def step_impl(context):
    context.wait.until(ec.visibility_of_element_located(makemodule.view_make_modal))


@then(u'the make name should be "{make_name}"')
def step_impl(context, make_name):
    value = context.wait.until(ec.visibility_of_element_located(makemodule.make_input)).get_attribute("value")
    assert value.strip() == make_name, f'Expected make name "{make_name}", but got "{value}".'
    context.wait.until(ec.element_to_be_clickable(commonelements.modal_cancel_button)).click()


@when(u'User click on edit button')
def step_impl(context):
    context.wait.until(ec.visibility_of_element_located(commonelements.edit_icon))
    context.wait.until(ec.element_to_be_clickable(commonelements.edit_icon)).click()
    # context.wait.until(ec.visibility_of_element_located(makemodule.make_input))


@when(u'User clear and enter make name "{updated_make_name}"')
def step_impl(context, updated_make_name):
    make_input = context.wait.until(ec.element_to_be_clickable(makemodule.make_input))
    make_input.clear()
    make_input.send_keys(updated_make_name)


@when(u'User click update button')
def step_impl(context):
    time.sleep(2)
    context.wait.until(ec.element_to_be_clickable(commonelements.update_button)).click()


@then(u'User should see make updated success message')
def step_impl(context):
    toast = context.wait.until(ec.element_to_be_clickable(commonelements.toaster))
    time.sleep(1)
    toast_text = toast.text.strip()
    assert "updated successfully" in toast_text or "success" in toast_text, (
        f"Expected update success toaster, but got: {toast_text}")
    context.wait.until(ec.invisibility_of_element_located(commonelements.toaster))


@when(u'User click on delete button')
def step_impl(context):
    delete_icon = context.wait.until(ec.visibility_of_element_located(commonelements.delete_icon))
    delete_icon.click()    
    context.wait.until(ec.visibility_of_element_located(commonelements.confirm_delete_text))


@when(u'User confirm delete')
def step_impl(context):
    context.wait.until(ec.element_to_be_clickable(commonelements.delete_button)).click()


@then(u'User should see make deleted success message')
def step_impl(context):
    toast = context.wait.until(ec.visibility_of_element_located(commonelements.toaster))
    time.sleep(1)
    toast_text = toast.text
    assert "deleted successfully" in toast_text or "success" in toast_text, (
        f"Expected delete success toaster, but got: {toast_text}")
    context.wait.until(ec.invisibility_of_element_located(commonelements.toaster))


@then(u'"{make_name}" should not be visible in the list')
def step_impl(context, make_name):
    base = BasePage(context.driver, context.wait)
    try:
        context.log.info(f"Verifying '{make_name}' is NOT visible in the list")

        result = base.verify_value_on_table(make_name)

        if result == make_name:
            raise AssertionError(f"'{make_name}' is visible in the list ❌")

        context.log.info(f"'{make_name}' is not present in the list ✅")

    except Exception as e:
        context.log.error(f"Error while verifying absence of '{make_name}': {str(e)}")
        raise

@then(u'Toaster message contains "already exists" should be displayed')
def step_impl(context):
    toast = context.wait.until(ec.visibility_of_element_located(commonelements.toaster))
    time.sleep(1)
    toast_text = toast.text
    assert "Make already exists." in toast_text, (
        f'Expected "Make already exists." in toaster, but got: {toast_text}')
    context.wait.until(ec.invisibility_of_element_located(commonelements.toaster))


@then(u'Validation message "This field is required!" should be displayed')
def step_impl(context):
    validation_text = context.wait.until(ec.visibility_of_element_located\
        (makemodule.make_validation_message)).text.strip()
    assert validation_text == "This field is required.", (
        f'Expected validation text "This field is required!", but got "{validation_text}".')
