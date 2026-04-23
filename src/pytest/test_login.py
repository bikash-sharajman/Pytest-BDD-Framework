import time
import pytest
from src.initialization.config_reader import confr
from src.locators.login_locators import loginelements
from src.locators.common_locators import commonelements
from selenium.webdriver.support import expected_conditions as ec
from src.utils.screenshot import take_screenshot



pytestmark = pytest.mark.no_login



@pytest.mark.smoke
@pytest.mark.order(1)
def test_valid_login(setup):
    conftest = setup
    conftest.login_page.login(confr.email, confr.password)
    conftest.wait.until(ec.url_contains("solar-plant-dashboard"))
    take_screenshot(conftest.driver)
    

@pytest.mark.smoke
@pytest.mark.order(2)
@pytest.mark.parametrize("email, password",[("invalid@email.com", "wrongpass"),("testusergensom@gmail.com", "password123455"),],)
def test_invalid_login(setup, email, password):
    conftest = setup
    conftest.login_page.login(email, password)
    error_message = conftest.base_page.get_toaster_message()
    assert error_message == "Incorrect username or password", "Expected toaster message not found."
    take_screenshot(conftest.driver)
    
    
@pytest.mark.smoke
@pytest.mark.order(3)
@pytest.mark.parametrize("email, password",[("", "Password@1234"),("testusergensom@gmail.com", ""),("", ""),],)
def test_login_button_should_be_disabled_for_blank_fields(setup, email, password):
    conftest = setup
    conftest.login_page.enter_email_id(email)
    conftest.login_page.enter_password(password)
    login_btn = conftest.login_page.driver.find_element(*loginelements.login_button)
    assert not login_btn.is_enabled()
    take_screenshot(conftest.driver)
    
@pytest.skip(reason = "it will block the account after 5 unsuccessful login attempts.")
@pytest.mark.smoke
@pytest.mark.order(5)
def test_the_login_page_deactivate_feature(setup):
    conftest = setup
    conftest.login_page.enter_email_id("testusergensom@gmail.com")
    conftest.login_page.enter_password("Incorrect@12345")

    toasters = []
    for i in range(5):
        conftest.login_page.click_on(loginelements.login_button)
        time.sleep(1)
        toaster = conftest.wait.until(ec.visibility_of_element_located(commonelements.toaster))
        toasters.append(toaster.text)
        take_screenshot(conftest.driver)
        toaster.click()
        
    for i in range(4):
        assert toasters[i] == "Incorrect username or password",\
            f"Mismatch at index {i}"
            
    assert toasters[4] == \
    "Your account has been temporarily blocked. Please try again after one hour.",\
        "Account block message mismatch"
        
@pytest.mark.smoke
@pytest.mark.order(4)
def test_otp_generation_with_valid_input(setup):
    conftest = setup
    conftest.login_page.click_on_trouble_login()
    conftest.login_page.enter_email_id(confr.email)
    conftest.login_page.enter_number(confr.mobile_no)
    conftest.login_page.click_generateopt()
    take_screenshot(conftest.driver)
    
    assert "OTP sent successfully." in conftest.base_page.get_toaster_message(),\
        f"Incorrect toaster message appeared upon clicking on generate opt button."
        
# def test_otp_generation_with_invalid_input(setup):
#     conftest = setup
    
    

        