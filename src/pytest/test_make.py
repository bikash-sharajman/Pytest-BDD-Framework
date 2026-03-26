import time

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as ec

from src.initialization.config_reader import confr
from src.locators.common_locators import commonelements
from src.locators.make_mstr_locators import makemodule
from src.pages.login import Login


def _login_to_application(driver, wait):
    login_page = Login(driver, wait)
    login_page.login(confr.username, confr.password)
    wait.until(ec.presence_of_element_located(commonelements.dashboard_menu))


def _navigate_to_make_module(wait):
    wait.until(ec.element_to_be_clickable(commonelements.side_bar)).click()
    wait.until(ec.element_to_be_clickable(commonelements.master_menu)).click()
    wait.until(ec.element_to_be_clickable(commonelements.make_master)).click()
    wait.until(ec.url_contains("make"))


def _search_make(wait, make_name):  
    search_box = wait.until(ec.element_to_be_clickable(commonelements.search_bar))
    search_box.clear()
    search_box.send_keys(make_name)
    search_box.send_keys(Keys.ENTER)


@pytest.mark.smoke
def test_add_make_successfully(setup):
    driver, wait = setup
    make_name = f"Test Make {int(time.time())}"

    _login_to_application(driver, wait)
    _navigate_to_make_module(wait)

    wait.until(ec.element_to_be_clickable(makemodule.add_make)).click()
    make_input = wait.until(ec.visibility_of_element_located(makemodule.make_input))
    make_input.clear()
    make_input.send_keys(make_name)
    wait.until(ec.element_to_be_clickable(commonelements.modal_save_button)).click()

    toast = wait.until(ec.visibility_of_element_located(commonelements.toaster))
    toast_text = toast.text.strip()
    assert "success" in toast_text.lower(), (
        f"Expected success toaster message, but got: {toast_text}"
    )

    _search_make(wait, make_name)
    make_row = wait.until(
        ec.visibility_of_element_located(
            (By.XPATH, f"//p-table//tbody//tr[contains(normalize-space(.), '{make_name}')]")
        )
    )
    assert make_name in make_row.text, f'"{make_name}" was not found in the make list.'


@pytest.mark.smoke
def test_add_make_without_name_shows_validation_message(setup):
    driver, wait = setup

    _login_to_application(driver, wait)
    _navigate_to_make_module(wait)

    wait.until(ec.element_to_be_clickable(makemodule.add_make)).click()
    wait.until(ec.element_to_be_clickable(commonelements.modal_save_button)).click()

    validation_message = wait.until(
        ec.visibility_of_element_located(commonelements.input_field_required_error_message)
    ).text.strip()
    assert validation_message == "This field is required.", (
        f'Expected validation message "This field is required.", but got "{validation_message}".'
    )


