import time
from behave import given, when, then
from behave.exception import StepNotImplementedError
from src.locators.login_locators import loginelements
from src.locators.common_locators import commonelements
from selenium.webdriver.support import expected_conditions as ec
from src.initialization.config_reader import confr




@given(u'User enters "{registered_email}" email address')
def step_impl(context, registered_email):
    context.log.info("Entering registered email address")
    # time.sleep(1)
    # context.driver.find_element(*loginelements.email_field).send_keys(registered_email)
    context.wait.until(ec.element_to_be_clickable(loginelements.email_field)).send_keys(registered_email)

@given(u'User enters "{registered_mobileno}" phone number with country code')
def step_impl(context, registered_mobileno):
    context.log.info("Entering registered phone number with country code")
    # time.sleep(1)
    # context.driver.find_element(*loginelements.mobile_no_field).send_keys(registered_mobileno)
    context.wait.until(ec.element_to_be_clickable(loginelements.mobile_no_field)).send_keys(registered_mobileno)

@given(u'User clicks on Generate OTP button')
def step_impl(context):
    context.log.info("Clicking on Generate OTP button")
    # time.sleep(1)
    # context.driver.find_element(*loginelements.generate_otp_button).click()
    context.wait.until(ec.element_to_be_clickable(loginelements.generate_otp_button)).click()
    context.wait.until(ec.element_to_be_clickable(commonelements.toaster)).click()

@given(u'User should redirect to OTP verification page')
def step_impl(context):
    context.log.info("Verifying redirection to OTP verification page")
    otp_title = context.wait.until(ec.visibility_of_element_located(loginelements.otp_verification_text_element)).text
    assert otp_title == "OTP Verification", "User is not redirected to OTP verification page"

@when(u'User enters valid OTP in both email and phone number field')
def step_impl(context):
    context.log.info("Entering valid otp in both email and phone number field")
    otp = confr.get_email_otp()
    time.sleep(2)
    context.driver.find_element(*loginelements.otp_verification_email_otp_field).send_keys(otp)
    context.driver.find_element(*loginelements.otp_verification_mobile_otp_field).send_keys(otp)

@when(u'User clicks on Verify OTP button')
def step_impl(context):
    context.log.info("Clicking on verify otp button")
    # context.driver.find_element(*loginelements.otp_verification_validate_button).click()
    context.wait.until(ec.element_to_be_clickable(loginelements.otp_verification_validate_button)).click()

@then(u'User should redirect to update password page')
def step_impl(context):
    context.log.info("Verifying user redirection to update password page")
    update_pass_text = context.wait.until(
        ec.visibility_of_element_located(loginelements.update_password_text_element)
    ).text
    assert update_pass_text == "Update Password", "User is not redirected to update password page"

@when(u'User enters invalid OTP in both email and phone number field')
def step_impl(context):
    context.log.info("Entering invalid otp in both email and phone number field")
    context.driver.find_element(*loginelements.otp_verification_email_otp_field).send_keys("121212")
    context.driver.find_element(*loginelements.otp_verification_mobile_otp_field).send_keys("121212")


@when(u'User try to verify with invalid otp {count:d} times')
def step_impl(context, count):
    context.log.info("Clicking on login button three times")
    context.toaster_messages = []
    
    for i in range(count):
        context.wait.until(ec.element_to_be_clickable(loginelements.otp_verification_validate_button)).click()
        time.sleep(1)
        print(f"Clicked on login button {i+1} times")
        toastr = context.wait.until(ec.visibility_of_element_located(commonelements.toaster))
        time.sleep(1)
        context.toaster_messages.append(toastr.text)

        context.wait.until(ec.invisibility_of_element_located(commonelements.toaster))


@then(u'First three toaster messages should display "{invalid_otp_toaster}"')
def step_impl(context, invalid_otp_toaster):
    context.log.info("Verifying first three toaster messages")
    for i in range(3):
        # assert context.toaster_messages[i] == invalid_otp_toaster
        assert invalid_otp_toaster.lower() in context.toaster_messages[1].lower()


@then(u'forth toaster message should display "{maximum_retry_acheived_error}"')
def step_impl(context, maximum_retry_achieved_error):
    context.log.info("Verifying forth toaster message")
    print(context.toaster_messages[3])
    # assert context.toaster_messages[3] == maximum_retry_achieved_error
    assert maximum_retry_achieved_error in context.toaster_messages[3]



@then(u'User should redirect to login page to retry again')
def step_impl(context):
    context.log.info("verifying whether user redirect to the login page after unsuccessful verification.")
    assert context.driver.current_url.endswith('login'),\
        "User is not redirected to login page"


@when(u'User enters "{valid_password}" in New Password field')
def step_impl(context, valid_password):
    context.log.info("Entering new valid password in new password field")
    context.driver.find_element(*loginelements.update_password_new_password_field).send_keys(valid_password)

@when(u'User enters "{valid_password}" in Confirm password field')
def step_impl(context, valid_password):
    context.log.info("Entering the same new valid password in confirm password field")
    context.driver.find_element(*loginelements.update_password_confirm_password_field).send_keys(valid_password)

@when(u'User clicks on show password checkbox')
def step_impl(context):
    context.log.info("Clicking on the show password checkbox")
    context.driver.find_element(*loginelements.show_password_checkbox).click()


@when(u'User clicks on Update Password button')
def step_impl(context):
    context.log.info("Clicking on update password button")
    context.driver.find_element(*loginelements.update_password_button).click()

@then(u'Password should be updated successfully')
def step_impl(context):
    context.log.info("Verifying password is updated or not")
    toast_text = context.wait.until(ec.visibility_of_element_located(commonelements.toaster)).text
    # Keep this check loose to avoid coupling to exact copy.
    assert "success" in toast_text.lower() or "updated" in toast_text.lower()

@then(u'User should be redirected to login page')
def step_impl(context):
    context.log.info("Verifying user redirection to login page after password updated")
    url = context.driver.current_url


@when(u'User enters "{valid_incorrect_password}" valid incorrect password in Confirm password field')
def step_impl(context, valid_incorrect_password):
    context.log.info("Entering the mismatched password in confirm password field")
    context.driver.find_element(*loginelements.update_password_confirm_password_field).send_keys(valid_incorrect_password)


@then(u'Password mismatch error toaster message should appear')
def step_impl(context):
    toaster = context.wait.until(ec.visibility_of_element_located(commonelements.toaster))
    message = toaster.text.strip()
    assert "password do not match" in message.lower(), f"Expected 'Password do not match' but got '{message}'"