import pytest
from src.initialization.config_reader import confr
from selenium.webdriver.support import expected_conditions as ec


@pytest.mark.smoke
def test_add_new_category(setup):
    conftest = setup
    conftest.login_page.login(confr.email, confr.password)
    conftest.wait.until(ec.url_contains("solar-plant-dashboard"))
    result = conftest.category_page.add_new_category("Test category")
    if "already exists" in result:
        print("Category already exists, skipping toaster check.")
        assert True
    else:    
        toaster = conftest.base_page.get_toaster_message()
        assert "New Category created successfully" in toaster, pytest.fail(f"Expected toaster not displayed, but got {toaster}")
    
@pytest.mark.smoke
def test_udpate_category(setup):
    conftest = setup
    conftest.login_page.login(confr.email, confr.password)
    conftest.wait.until(ec.url_contains("solar-plant-dashboard"))
    conftest.category_page.update_category("Test category", "Updated category")
    toaster = conftest.base_page.get_toaster_message()
    assert "Category updated successfully" in toaster,\
        pytest.fail(f"Expected toaster not displayed, but got {toaster}")

@pytest.mark.smoke
def test_delete_category(setup):
    conftest = setup
    conftest.login_page.login(confr.email, confr.password)
    conftest.wait.until(ec.url_contains("solar-plant-dashboard"))
    conftest.category_page.delete_category("Updated category")
    toaster = conftest.base_page.get_toaster_message()
    assert "Category deleted successfully." in toaster,\
        pytest.fail(f"Expected toaster message does not appear, but get {toaster}")