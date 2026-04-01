import pytest
from src.initialization.config_reader import confr
from selenium.webdriver.support import expected_conditions as ec

@pytest.mark.testing
def test_add_new_subcategory(setup):
    conftest = setup
    conftest.login_page.login(confr.email, confr.password)
    conftest.wait.until(ec.url_contains("solar-plant-dashboard"))
    result = conftest.sub_category_page.create_new_subcategory("Demo category", "Test Subcategory")
    if "exist" in result.lower():
        print(result)
        assert True
    elif "added" in result.lower():
        toaster = conftest.base_page.get_toaster_message()
        assert "Sub Category added Successfully" in toaster, pytest.fail(f"Expected toaster not displayed, but got {toaster}")
    else:
        pytest.fail(f"Unexpected result from create_new_subcategory: {result}")

@pytest.mark.smoke
def test_edit_subcategory(setup):
    conftest = setup
    conftest.login_page.login(confr.email, confr.password)
    conftest.wait.until(ec.url_contains("solar-plant-dashboard"))
    conftest.sub_category_page.open_sub_category_master()
    result = conftest.sub_category_page.update_subcategory("Test Subcategory", category_option="Category 2", sub_category_name="Updated Subcategory")
    toaster = conftest.base_page.get_toaster_message()
    assert "successfully" in toaster, f"Expected toaster not displayed, but got {toaster}"

@pytest.mark.smoke
def test_delete_subcategory(setup):
    conftest = setup
    conftest.login_page.login(confr.email, confr.password)
    conftest.wait.until(ec.url_contains("solar-plant-dashboard"))
    conftest.sub_category_page.open_sub_category_master()
    result = conftest.sub_category_page.delete_subcategory("Updated Subcategory")
    toaster = conftest.base_page.get_toaster_message()
    assert "deleted" in toaster, f"Expected toaster message does not appear, but got {toaster}"