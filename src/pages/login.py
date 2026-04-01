import time
from src.locators.base_file import BasePage
from src.locators.login_locators import loginelements
from selenium.webdriver.support import expected_conditions as ec

class Login(BasePage):

    def __init__(self, driver, wait):
        super().__init__(driver, wait)

    def enter_email_id(self, email):
        self.enter_value(loginelements.email_field, email)

    def enter_password(self, password):
        self.enter_value(loginelements.password_field, password)

    def click_login(self):
        self.click_on(loginelements.login_button)
    
    def click_on_trouble_login(self):
        self.click_on(loginelements.trouble_login_button)
        self.wait.until(ec.url_contains("forgot-password"))
    
    def enter_number(self, number):
        self.enter_value(loginelements.mobile_no_field, number)
    
    def click_generateopt(self):
        self.click_on(loginelements.generate_otp_button)
        self.wait.until(ec.url_contains("otp-verification"))
        
        
          
    def login(self, email, password):
        self.enter_email_id(email)
        self.enter_password(password)
        time.sleep(1)
        self.click_on(loginelements.login_button)

    
    def forget_password(self, email:str, mobileno: str):
        self.click_on_trouble_login()
        self.enter_email_id(email)
        self.enter_number(mobileno)
        self.click_generateopt()













