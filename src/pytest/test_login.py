import time
import pytest
from src.pages.login import Login
from src.initialization.config_reader import confr
from selenium.webdriver.support import expected_conditions as ec
from src.locators.common_locators import commonelements
from src.locators.login_locators import loginelements

@pytest.mark.smoke
def test_valid_login(setup):
    driver,wait = setup
    login_page = Login(driver, wait)

    login_page.login(confr.username, confr.password)
    time.sleep(2)
    # Example assertion (update based on your app)
    assert "solar-plant-dashboard" in login_page.driver.current_url


@pytest.mark.smoke
@pytest.mark.parametrize(
    "email, password",
    [
        ("invalid@email.com", "wrongpass"),
        ("testusergensom@gmail.com", "password123455"),
    ],
)
def test_invalid_login(setup, email, password):
    driver,wait = setup
    login_page = Login(driver, wait)

    login_page.login(email, password)

    # Replace with actual validation message locator check
    error_message = wait.until(ec.element_to_be_clickable(commonelements.toaster)).text

    assert error_message == "Incorrect username or password", "Expected toaster message not found."
    
    
@pytest.mark.smoke
@pytest.mark.parametrize(
    "email, password",
    [
        ("", "Password@1234"),
        ("testusergensom@gmail.com", ""),
        ("", ""),
    ],
)
def test_login_button_should_be_disabled_for_blank_fields(setup, email, password):
    driver, wait = setup
    login_page = Login(driver, wait)

    login_page.enter_email_id(email)
    login_page.enter_password(password)

    login_button = wait.until(
        ec.presence_of_element_located(loginelements.login_button)
    )

    assert not login_button.is_enabled(), (
        "Login button should be disabled when email or password is blank."
    )