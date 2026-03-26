from selenium.webdriver.common.by import  By



class LoginLocators:

    email_field = By.XPATH, "//input[@formcontrolname='email']"
    password_field = By.XPATH, "//input[@formcontrolname='password']"
    login_button = By.XPATH, "//button[@type='submit']"
    trouble_login_button = By.XPATH, "//span[normalize-space()='Click Here']"
    
    mobile_no_field = By.XPATH, "//input[@formcontrolname='mobile']"
    generate_otp_button = By.XPATH, "//button[text() ='Generate OTP']"
    forget_password_text = By.XPATH, "//h1[text()='Forgot Password']"
    
    otp_verification_text_element = By.XPATH, "//h1[text()='OTP Verification']"
    otp_verification_email_otp_field = By.XPATH, "//input[@formcontrolname='emailOtp']"
    otp_verification_mobile_otp_field = By.XPATH, "//input[@formcontrolname='mobileOtp']"
    otp_verification_validate_button = By.XPATH, "//button[text()='Validate']"
    otp_verification_resend_emailotp_button = By.XPATH, "//button[text()='Re-Send OTP (on email)']"
    otp_verification_resend_mobileotp_button = By.XPATH, "//button[text()='Re-Send OTP (on mobile)']"
    
    update_password_text_element = By.XPATH, "//h1[text()='Update Password']"
    update_password_new_password_field = By.ID, "newPassword"
    update_password_confirm_password_field = By.ID, "confirmPassword"
    update_password_button = By.XPATH, "//button[text()='Update Password']"
    update_password_i_button = By.XPATH, "//app-update-password/div/div[1]/div/div/div/a/i"
    show_password_checkbox = By.ID, "showPassword"
    password_match_element = By.XPATH, "//div[text()=' Password is matched ']"

    
    
    # NOTE: Selenium cannot locate XPath text() nodes; it must locate an element, then read .text.
    login_email_field_error_message = By.XPATH, "//*[@id='loginform']/div[1]/div/span"
    login_password_field_error_message = By.XPATH, "//*[@id='loginform']/div[2]/div/span"
    forget_page_email_field_error_message = By.XPATH, "//app-forgot-password/div/div[1]/div/form/div[1]/div/span"
    forget_page_mobile_field_error_message = By.XPATH, "//app-forgot-password/div/div[1]/div/form/div[2]/div/span"
    otp_verification_email_field_error_message = By.XPATH, "//app-otp-varification/div/div[1]/div/form/div[1]/div/small"
    otp_verification_mobile_field_error_message = By.XPATH, "//app-otp-varification/div/div[1]/div/form/div[2]/div/small"

    
loginelements = LoginLocators()

