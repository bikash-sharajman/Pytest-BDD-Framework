import pytest
from src.initialization.config_reader import confr
from selenium.webdriver.support import expected_conditions as ec


@pytest.mark.smoke
def test_add_new_make(setup):
    conftest = setup
    conftest.login_page.login(confr.email, confr.password)
    conftest.wait.until(ec.url_contains("solar-plant-dashboard"))
    result = conftest.make_page.create_new_make("Test make")
    if "already exists" in result:
        print("Make already exists, skipping toaster check.")
        assert True
    else:
        toaster = conftest.base_page.get_toaster_message()
        assert "Data Saved Sucessfully" in toaster, f"Expected toaster not displayed, but got {toaster}"
    

@pytest.mark.smoke
def test_edit_make(setup):
    conftest = setup
    conftest.login_page.login(confr.email, confr.password)
    conftest.wait.until(ec.url_contains("solar-plant-dashboard"))
    conftest.make_page.update_make("Test make", "Updated make")
    toaster = conftest.base_page.get_toaster_message()
    assert "Make updated successfully" in toaster, f"Expected toaster not displayed, but got {toaster}"
    
@pytest.mark.smoke
def test_delete_make(setup):
    conftest = setup
    conftest.login_page.login(confr.email, confr.password)
    conftest.wait.until(ec.url_contains("solar-plant-dashboard"))
    conftest.make_page.delete_make("Updated make")
    toaster = conftest.base_page.get_toaster_message()
    assert "Make deleted successfully" in toaster, f"Expected toaster not displayed, but got {toaster}"
    


