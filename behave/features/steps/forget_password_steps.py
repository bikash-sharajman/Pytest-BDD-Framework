from behave import given, when, then
from src.initialization.config_reader import confr
from src.locators.login_locators import loginelements
from src.locators.common_locators import commonelements
from selenium.webdriver.support import expected_conditions as ec
import time



@given(u'User should navigate to login page')
def step_impl(context):
    context.log.info("Navigating to login page")
    url = confr.get_baseurl()
    context.driver.get(f"{url}/login")


@given(u'User clicks on Forgot Password link')
def step_impl(context):
    context.log.info("clicking on Trouble logging in? Click here link")
    context.wait.until(ec.element_to_be_clickable(loginelements.trouble_login_button)).click()
    time.sleep(2)

@then(u'User should be redirected to forgot password page')
def step_impl(context):
    context.log.info("verifying the forget password page")
    assert context.driver.current_url.endswith('forgot-password'),\
        "User is not redirected to forgot password page"
    assert context.wait.until(ec.element_to_be_clickable(loginelements.forget_password_text)).is_displayed(),\
        "User is not redirected to forgot password page"


@when(u'User enters "{registered_email}" email address')
def step_impl(context, registered_email):
    context.log.info("Entering registered email address")
    context.wait.until(ec.element_to_be_clickable(loginelements.email_field)).send_keys(registered_email)

@when(u'User enters "{mobile_number}" phone number with country code')
def step_impl(context, mobile_number):
    context.log.info("Entering registered phone number with country code")
    context.wait.until(ec.element_to_be_clickable(loginelements.mobile_no_field)).send_keys(mobile_number)

@when(u'User clicks on Generate OTP button')
def step_impl(context):
    context.log.info("Clicking on Generate OTP button")
    context.wait.until(ec.element_to_be_clickable(loginelements.generate_otp_button)).click()

@then(u'User should redirect to OTP verification page')
def step_impl(context):
    context.log.info("Verifying redirection to OTP verification page")
    otp_title = context.wait.until(ec.visibility_of_element_located(loginelements.otp_verification_text_element)).text
    assert otp_title == "OTP Verification", "User is not redirected to OTP verification page"

@then(u'success toaster message should be displayed')
def step_impl(context):
    context.log.info("Verifying success toaster message")
    toaster = context.wait.until(ec.visibility_of_element_located(commonelements.toaster))
    toaster_message = toaster.text
    assert "OTP sent successfully" in toaster_message, "Expected success message not displayed in toaster"

@when(u'User keeps the email field blank')
def step_impl(context):
    context.log.info("keeping the email field blank")
    context.wait.until(ec.element_to_be_clickable(loginelements.email_field)).click()
    # assert context.wait.until(ec.visibility_of_element_located(commonelements.toaster)).text == "Please fill all required fields",\
    #     "Expected toaster message not displayed if email field remains blank."

@then(u'Toaster message should be displayed and prompt user to enter all required fields')
def step_impl(context):
    context.log.info("Verifying toaster message for blank email field")
    toaster = context.wait.until(ec.visibility_of_element_located(commonelements.toaster))
    toaster_message = toaster.text
    assert "Please fill all required fields" in toaster_message, "Expected error message not displayed in toaster"

@when(u'User keeps the phone number field blank')
def step_impl(context):
    context.log.info("keeping the phone number field blank")
    context.driver.find_element(*loginelements.mobile_no_field).click()
    # assert context.driver.find_element(*loginelements.forget_page_mobile_field_error_message).text == "Mobile number is required.", "Expected error message for blank phone number field is not displayed"

