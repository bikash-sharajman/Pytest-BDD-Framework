import time
from behave import given, when, then

from src.initialization.config_reader import confr
from src.locators.login_locators import loginelements
from src.locators.common_locators import commonelements
from selenium.webdriver.support import expected_conditions as ec    

@when(u'User enters "{valid_password}" password')
def step_impl(context, valid_password):
    try:
        context.log.info("Entering registered password")
        pass_field = context.wait.until(ec.presence_of_element_located(loginelements.password_field))
        pass_field.clear()
        pass_field.send_keys(valid_password)

    except Exception as e:
        context.log.error(f"Failed to enter password: {e}")
        raise

@when(u'User clicks on Login button')
def step_impl(context):
    try:
        context.log.info("Clicking on login button")
        context.wait.until(ec.element_to_be_clickable(loginelements.login_button)).click()

    except Exception as e:
        context.log.error(f"Failed to click login button: {e}")
        raise

@then(u'User should be redirected to overview dashboard page')
def step_impl(context):
    try:
        context.log.info("Verifying dashboard redirection")
        assert context.wait.until(ec.url_contains('solar-plant-dashboard'))\
        , "User not redirected to dashboard"

    except Exception as e:
        context.log.error(f"Dashboard validation failed: {e}")
        raise

@when(u'User enters "{unregistered_email}" unregistered email address')
def step_impl(context, unregistered_email):
    try:
        context.log.info("Entering unregistered email")
        context.wait.until(ec.element_to_be_clickable(loginelements.email_field))\
            .send_keys(unregistered_email)

    except Exception as e:
        context.log.error(f"Failed to enter email: {e}")
        raise

@when(u'User enters "{incorrect_password}" incorrect password')
def step_impl(context, incorrect_password):
    try:
        context.log.info("Entering incorrect password")
        context.wait.until(ec.element_to_be_clickable(loginelements.password_field))\
            .send_keys(incorrect_password)

    except Exception as e:
        context.log.error(f"Failed to enter incorrect password: {e}")
        raise

@then(u'Error toaster message should be displayed')
def step_impl(context):
    try:
        context.log.info("Validating error toaster")
        toaster_text = context.wait.until(ec.visibility_of_element_located(commonelements.toaster)).text

        assert "Incorrect username or password" in toaster_text, f"Unexpected toaster message: {toaster_text}"

    except Exception as e:
        context.log.error(f"Toaster validation failed: {e}")
        raise

@when(u'User keeps email field and password field blank')
def step_impl(context):
    try:
        context.log.info("Keeping email & password blank")
        

    except Exception as e:
        context.log.error(f"Error in blank field step: {e}")
        raise
        
        
@then(u'Validation message should appear under email field and password field')
def step_impl(context):
    try:
        context.log.info("Validating required field messages")
        email_msg = context.wait.until(
            ec.visibility_of_element_located(loginelements.login_email_field_error_message)).text

        password_msg = context.wait.until(ec.visibility_of_element_located\
            (loginelements.login_password_field_error_message)).text
        
        assert email_msg == "Email is required", f"Email validation mismatch: {email_msg}"
        assert password_msg == "Password is required", f"Password validation mismatch: {password_msg}"

    except Exception as e:
        context.log.error(f"Validation message check failed: {e}")
        raise

@when(u'User clicks on Login button {count:d} times')
def step_impl(context, count):
    try:
        context.log.info(f"Clicking login button {count} times")
        context.toaster_messages = []

        for i in range(count):
            context.wait.until(ec.element_to_be_clickable(loginelements.login_button)).click()
            time.sleep(1)
            toastr = context.wait.until(ec.visibility_of_element_located(commonelements.toaster))
            context.toaster_messages.append(toastr.text)
            toastr.click()

    except Exception as e:
        context.log.error(f"Error during multiple login attempts: {e}")
        raise

@then(u'First four toaster messages should display "{incorrect_credential_message}"')
def step_impl(context, incorrect_credential_message):
    try:
        context.log.info("Validating first four toaster messages")
        for i in range(4):
            assert context.toaster_messages[i] == incorrect_credential_message, f"Mismatch at index {i}"

    except Exception as e:
        context.log.error(f"First four toaster validation failed: {e}")
        raise

@then(u'Fifth toaster message should display "{account_blocked_message}"')
def step_impl(context, account_blocked_message):
    try:
        context.log.info("Validating fifth toaster message")
        assert context.toaster_messages[4] == account_blocked_message, "Account block message mismatch"

    except Exception as e:
        context.log.error(f"Fifth toaster validation failed: {e}")
        raise



















