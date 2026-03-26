import time
from behave import given, when, then
from src.locators.login_locators import loginelements
from src.locators.common_locators import commonelements
from selenium.webdriver.support import expected_conditions as ec
from src.initialization.config_reader import confr
# from selenium.webdriver.common.by import By



@given(u'User enters "{registered_email}" email address')
def step_impl(context, registered_email):
    try:
        context.log.info("Entering registered email")
        context.wait.until(ec.url_contains("forgot-password"))
        element = context.wait.until(ec.presence_of_element_located(loginelements.email_field))
        element.clear()
        element.send_keys(registered_email)
        # context.wait.until(ec.element_to_be_clickable(loginelements.email_field)).send_keys(registered_email)
        # context.wait.until(ec.element_to_be_clickable(loginelements.email_field)).send_keys(registered_email)

    except Exception as e:
        context.log.error(f"Failed to enter email: {e}")
        raise

@given(u'User enters "{registered_mobileno}" phone number with country code')
def step_impl(context, registered_mobileno):
    try:
        context.log.info("Entering mobile number")
        mob_field = context.wait.until(ec.element_to_be_clickable(loginelements.mobile_no_field))
        mob_field.clear()
        mob_field.send_keys(registered_mobileno)

    except Exception as e:
        context.log.error(f"Failed to enter mobile number: {e}")
        raise

@given(u'User clicks on Generate OTP button')
def step_impl(context):
    try:
        context.log.info("Clicking on Generate OTP button")
        context.wait.until(ec.presence_of_element_located(loginelements.generate_otp_button)).click()
        context.wait.until(ec.visibility_of_element_located(commonelements.toaster))

    except Exception as e:
        context.log.error(f"Failed to click Generate OTP: {e}")
        raise

@given(u'User should redirect to OTP verification page')
def step_impl(context):
    try:
        context.log.info("Verifying OTP verification page")
        otp_title = context.wait.until(ec.visibility_of_element_located\
            (loginelements.otp_verification_text_element)).text.strip()
        assert otp_title == "OTP Verification", \
            f"Expected 'OTP Verification' but got '{otp_title}'"

    except Exception as e:
        context.log.error(f"OTP page validation failed: {e}")
        raise

@when(u'User enters valid OTP in both email and phone number field')
def step_impl(context):
    try:
        context.log.info("Entering valid OTP")
        otp = confr.get_email_otp()
        email_otp = context.wait.until(ec.presence_of_element_located(loginelements.otp_verification_email_otp_field))
        mobile_otp = context.wait.until(ec.presence_of_element_located(loginelements.otp_verification_mobile_otp_field))

        email_otp.clear()
        mobile_otp.clear()

        email_otp.send_keys(otp)
        mobile_otp.send_keys(otp)

    except Exception as e:
        context.log.error(f"Failed to enter valid OTP: {e}")
        raise

@when(u'User clicks on Verify OTP button')
def step_impl(context):
    try:
        context.log.info("Clicking on Verify OTP button")
        context.wait.until(ec.element_to_be_clickable(loginelements.otp_verification_validate_button)).click()

    except Exception as e:
        context.log.error(f"Failed to click Verify OTP button: {e}")
        raise

@then(u'User should redirect to update password page')
def step_impl(context):
    try:
        context.log.info("Verifying redirection to Update Password page")
        text = context.wait.until(ec.visibility_of_element_located\
            (loginelements.update_password_text_element)).text.strip()
        assert text == "Update Password", \
            f"Expected 'Update Password' but got '{text}'"

    except Exception as e:
        context.log.error(f"Update password page validation failed: {e}")
        raise

@when(u'User enters invalid OTP in both email and phone number field')
def step_impl(context):
    try:
        context.log.info("Entering invalid OTP")

        otp_email_field = context.wait.until(ec.presence_of_element_located(loginelements.otp_verification_email_otp_field))
        otp_email_field.clear()
        otp_email_field.send_keys("121212")
        
        otp_mobile_field = context.wait.until(ec.element_to_be_clickable(loginelements.otp_verification_mobile_otp_field))
        otp_mobile_field.clear()
        otp_mobile_field.send_keys("121212")

    except Exception as e:
        context.log.error(f"Failed to enter invalid OTP: {e}")
        raise


@when(u'User try to verify with invalid otp {count:d} times')
def step_impl(context, count):
    try:
        context.log.info(f"Trying OTP verification {count} times")
        context.toaster_messages = []
        for i in range(count):
            context.wait.until(ec.element_to_be_clickable(loginelements.otp_verification_validate_button)).click()
            toaster = context.wait.until(ec.visibility_of_element_located(commonelements.toaster))
            message = toaster.text.strip()
            context.toaster_messages.append(message)
            context.log.info(f"Attempt {i+1}: {message}")
            context.wait.until(ec.invisibility_of_element_located(commonelements.toaster))

    except Exception as e:
        context.log.error(f"OTP retry failed: {e}")
        raise


@then(u'First three toaster messages should display "{invalid_otp_toaster}"')
def step_impl(context, invalid_otp_toaster):
    try:
        context.log.info("Validating first three toaster messages")
        for i in range(3):
            assert invalid_otp_toaster.lower() in context.toaster_messages[i].lower(), \
                f"Mismatch at attempt {i+1}: {context.toaster_messages[i]}"

    except Exception as e:
        context.log.error(f"Validation failed for first three toaster messages: {e}")
        raise


@then(u'forth toaster message should display "{maximum_retry_acheived_error}"')
def step_impl(context, maximum_retry_achieved_error):
    try:
        context.log.info("Validating fourth toaster message")
        actual = context.toaster_messages[3]
        assert maximum_retry_achieved_error.lower() in actual.lower(), \
            f"Expected: {maximum_retry_achieved_error}, Got: {actual}"

    except Exception as e:
        context.log.error(f"Fourth attempt validation failed: {e}")
        raise


@then(u'User should redirect to login page to retry again')
def step_impl(context):
    try:
        context.log.info("Verifying redirection to login page after failed OTP")
        assert context.driver.current_url.endswith('login'), \
            f"User not redirected to login page. URL: {context.driver.current_url}"

    except Exception as e:
        context.log.error(f"Retry login redirection failed: {e}")
        raise


@when(u'User enters "{valid_password}" in New Password field')
def step_impl(context, valid_password):
    try:
        context.log.info("Entering new password")
        valid_password_field = context.wait.until(ec.presence_of_element_located(loginelements.update_password_new_password_field))
        valid_password_field.clear()
        valid_password_field.send_keys(valid_password)

    except Exception as e:
        context.log.error(f"Failed to enter new password: {e}")
        raise

@when(u'User enters "{valid_password}" in Confirm password field')
def step_impl(context, valid_password):
    try:
        context.log.info("Entering new password")
        valid_cofirm_field = context.wait.until(ec.presence_of_element_located(loginelements.update_password_confirm_password_field))
        valid_cofirm_field.clear()
        valid_cofirm_field.send_keys(valid_password)

    except Exception as e:
        context.log.error(f"Failed to enter new password in confirm password filed.: {e}")
        raise

@when(u'User clicks on show password checkbox')
def step_impl(context):
    try:
        context.log.info("Clicking on show password checkbox")
        show_pass_chckbox = context.wait.until(ec.presence_of_element_located(loginelements.show_password_checkbox))
        show_pass_chckbox.click()

    except Exception as e:
        context.log.error(f"Failed to click show password checkbox: {e}")
        raise


@when(u'User clicks on Update Password button')
def step_impl(context):
    try:
        context.log.info("Clicking on update password button")
        context.wait.until(ec.element_to_be_clickable(loginelements.update_password_button)).click()

    except Exception as e:
        context.log.error(f"Failed to click update password button: {e}")
        raise

@then(u'Password should be updated successfully')
def step_impl(context):
    try:
        context.log.info("Validating password update success")
        toast = context.wait.until(ec.visibility_of_element_located(commonelements.toaster)).text.lower()
        assert "success" in toast or "updated" in toast, \
            f"Unexpected toaster message: {toast}"

    except Exception as e:
        context.log.error(f"Password update validation failed: {e}")
        raise

@then(u'User should be redirected to login page')
def step_impl(context):
    try:
        context.log.info("Verifying redirection to login page after password update")
        assert "login" in context.wait.until(ec.url_contains("login")), \
            f"User not redirected to login page. Current URL: {context.driver.current_url}"

    except Exception as e:
        context.log.error(f"Login redirection validation failed: {e}")
        raise


@when(u'User enters "{valid_incorrect_password}" valid incorrect password in Confirm password field')
def step_impl(context, valid_incorrect_password):
    try:
        context.log.info("Entering the mismatched password in confirm password field")
        context.driver.find_element(*loginelements.update_password_confirm_password_field)\
            .send_keys(valid_incorrect_password)
    
    except Exception as e:
        context.log.error("Unable to enter valid incorrect password in confirm password field.")
        raise


@then(u'Password mismatch error toaster message should appear')
def step_impl(context):
    try:
        context.log.info("Validating password mismatch error")
        message = context.wait.until(ec.visibility_of_element_located(commonelements.toaster)).text.strip()
        assert "password" in message.lower() and "match" in message.lower(), \
            f"Unexpected message: {message}"

    except Exception as e:
        context.log.error(f"Password mismatch validation failed: {e}")
        raise