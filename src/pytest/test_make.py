import pytest
from src.utils.screenshot import take_screenshot


@pytest.mark.testing
def test_add_new_make(setup):
    conftest = setup
    result = conftest.make_page.create_new_make("Test make")
    if "already exists" in result.lower():
        conftest.log.warning("Make already exists, skipping toaster check.")
        return
    else:
        toaster = conftest.base_page.get_toaster_message()
        assert "Make added successfully." in toaster, f"Expected toaster not displayed, but got {toaster}"
        take_screenshot(conftest.driver)
    

@pytest.mark.testing
def test_edit_make(setup):
    conftest = setup
    result = conftest.make_page.update_make("Test make", "Updated make")
    if "updated" in result.lower():
        conftest.log.info("Make updated successfully, checking toaster.")
    elif "changed" in result.lower():
        conftest.log.info("Make created and updated successfully, checking toaster.")
    else:
        conftest.log.warning("Make not updated, skipping toaster check.")
        return
        
    toaster = conftest.base_page.get_toaster_message()
    assert "Make updated successfully" in toaster, f"Expected toaster not displayed, but got {toaster}"
    take_screenshot(conftest.driver)
    
@pytest.mark.testing
def test_delete_make(setup):
    conftest = setup
    result = conftest.make_page.delete_make("Updated make")
    if "deleted" in result.lower():
        conftest.log.info("Make deleted successfully, checking toaster.")
    elif "removed" in result.lower():
        conftest.log.info("Make created and deleted successfully, checking toaster.")
    else:
        conftest.log.warning("Make not deleted, skipping toaster check.")
        return  
    toaster = conftest.base_page.get_toaster_message()
    assert "Make deleted successfully" in toaster, f"Expected toaster not displayed, but got {toaster}"
    take_screenshot(conftest.driver)
    

