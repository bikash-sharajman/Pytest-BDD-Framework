from behave import given, when, then
from src.initialization.config_reader import confr
from src.locators.login_locators import loginelements
from src.locators.common_locators import commonelements
from selenium.webdriver.support import expected_conditions as ec



@given(u'User should navigate to login page')
def step_impl(context):
    try:
        context.log.info("Navigating to login page")
        url = confr.get_baseurl()
        context.driver.get(f"{url}/login")
    except Exception as e:
        context.log.error(f"Failed to navigate to login page: {e}")
        raise


@given(u'User clicks on Forgot Password link')
def step_impl(context):
    try:
        context.log.info("Clicking on Trouble logging in link")
        forget_link =context.wait.until(ec.presence_of_element_located(loginelements.trouble_login_button))
        forget_link.click()
        
    except Exception as e:
        context.log.error(f"Failed to click Forgot Password link: {e}")
        raise

@then(u'User should be redirected to forgot password page')
def step_impl(context):
    try:
        context.log.info("Verifying forgot password page")
        assert context.wait.until(ec.url_contains("forgot-password")), \
            "User is not redirected to forgot password page"
        assert context.wait.until(ec.visibility_of_element_located\
            (loginelements.forget_password_text)), \
            "Forgot password page text not visible"

    except Exception as e:
        context.log.error(f"Forgot password page validation failed: {e}")
        raise


@when(u'User enters "{registered_email}" email address')
def step_impl(context, registered_email):
    try:
        context.log.info("Entering registered email address")
        email_field = context.wait.until(ec.presence_of_element_located(loginelements.email_field))
        email_field.clear()
        email_field.send_keys(registered_email)
                
    except Exception as e:
        context.log.error(f"Failed to enter email: {e}")
        raise

@when(u'User enters "{mobile_number}" phone number with country code')
def step_impl(context, mobile_number):
    try:
        context.log.info("Entering phone number")
        phone_no = context.wait.until(ec.presence_of_element_located(loginelements.mobile_no_field))
        phone_no.clear()
        phone_no.send_keys(mobile_number)
            
    except Exception as e:
        context.log.error(f"Failed to enter phone number: {e}")
        raise

@when(u'User clicks on Generate OTP button')
def step_impl(context):
    try:
        context.log.info("Clicking on Generate OTP button")
        generate_btn = context.wait.until(ec.presence_of_element_located(loginelements.generate_otp_button))
        generate_btn.click()
        
    except Exception as e:
        context.log.error(f"Failed to click Generate OTP button: {e}")
        raise

@then(u'User should redirect to OTP verification page')
def step_impl(context):
    try:
        context.log.info("Verifying OTP verification page")
        otp_title = context.wait.until(ec.visibility_of_element_located\
            (loginelements.otp_verification_text_element)).text
        
        assert otp_title.strip() == "OTP Verification", \
            f"Expected 'OTP Verification' but got '{otp_title}'"

    except Exception as e:
        context.log.error(f"OTP verification page validation failed: {e}")
        raise

@then(u'success toaster message should be displayed')
def step_impl(context):
    try:
        context.log.info("Verifying success toaster message")
        toaster = context.wait.until(ec.visibility_of_element_located(commonelements.toaster))
        toaster_message = toaster.text
        assert "OTP sent successfully" in toaster_message, \
                f"Expected success message not found. Actual: {toaster_message}"

    except Exception as e:
        context.log.error(f"Success toaster validation failed: {e}")
        raise

@when(u'User keeps the email field blank')
def step_impl(context):
    try:
        context.log.info("Keeping email field blank")
        email_field = context.wait.until(ec.presence_of_element_located(loginelements.email_field))
        email_field.clear()
        
    except Exception as e:
        context.log.error(f"Failed to handle blank email field: {e}")
        raise


@then(u'Toaster message should be displayed and prompt user to enter all required fields')
def step_impl(context):
    try:
        context.log.info("Verifying toaster message for blank fields")
        toaster = context.wait.until(ec.visibility_of_element_located(commonelements.toaster))
        toaster_message = toaster.text
        assert "Please fill all required fields" in toaster_message, \
            f"Expected validation message not found. Actual: {toaster_message}"

    except Exception as e:
        context.log.error(f"Validation toaster check failed: {e}")
        raise

@when(u'User keeps the phone number field blank')
def step_impl(context):
    try:
        context.log.info("Keeping phone number field blank")
        phone_no = context.wait.until(ec.presence_of_element_located(loginelements.mobile_no_field))
        phone_no.clear()
        
    except Exception as e:
        context.log.error(f"Failed to handle blank phone number field: {e}")
        raise

