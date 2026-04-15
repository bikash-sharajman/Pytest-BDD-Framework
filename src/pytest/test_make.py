import pytest
from src.utils.screenshot import take_screenshot


@pytest.mark.testing
def test_add_new_make(setup):
    conftest = setup
    result = conftest.make_page.create_new_make("Test make")
    if "already exists" in result:
        print("Make already exists, skipping toaster check.")
        take_screenshot(conftest.driver)
        assert True
    else:
        toaster = conftest.base_page.get_toaster_message()
        assert "Make added successfully." in toaster, f"Expected toaster not displayed, but got {toaster}"
        take_screenshot(conftest.driver)
    

@pytest.mark.testing
def test_edit_make(setup):
    conftest = setup
    conftest.make_page.update_make("Test make", "Updated make")
    toaster = conftest.base_page.get_toaster_message()
    assert "Make updated successfully" in toaster, f"Expected toaster not displayed, but got {toaster}"
    take_screenshot(conftest.driver)
    
@pytest.mark.testing
def test_delete_make(setup):
    conftest = setup
    conftest.make_page.delete_make("Updated make")
    toaster = conftest.base_page.get_toaster_message()
    assert "Make deleted successfully" in toaster, f"Expected toaster not displayed, but got {toaster}"
    take_screenshot(conftest.driver)
    

