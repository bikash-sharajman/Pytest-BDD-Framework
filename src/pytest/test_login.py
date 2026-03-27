import pytest
from src.initialization.config_reader import confr
from src.locators.login_locators import loginelements
from selenium.webdriver.support import expected_conditions as ec

# @pytest.mark.smoke
def test_valid_login(setup):
    conftest = setup
    conftest.login_page.login(confr.email, confr.password)
    # current_url = conftest.driver.current_url
    # assert "solar-plant-dashboard" in current_url, \
    #     f"Expected URL to contain 'solar-plant-dashboard', but got '{current_url}'"
    conftest.wait.until(ec.url_contains("solar-plant-dashboard"))


# @pytest.mark.smoke
@pytest.mark.parametrize("email, password",[("invalid@email.com", "wrongpass"),("testusergensom@gmail.com", "password123455"),],)
def test_invalid_login(setup, email, password):
    conftest = setup
    conftest.login_page.login(email, password)
    error_message = conftest.base_page.get_toaster_message()
    assert error_message == "Incorrect username or password", "Expected toaster message not found."
    
    
# @pytest.mark.smoke
@pytest.mark.parametrize("email, password",[("", "Password@1234"),("testusergensom@gmail.com", ""),("", ""),],)
def test_login_button_should_be_disabled_for_blank_fields(setup, email, password):
    conftest = setup
    conftest.login_page.enter_email_id(email)
    conftest.login_page.enter_password(password)
    login_btn = conftest.login_page.driver.find_element(*loginelements.login_button)
    assert not login_btn.is_enabled()