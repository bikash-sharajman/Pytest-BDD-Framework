import pytest

@pytest.mark.smoke
def test_add_new_subcategory(setup):
    conftest = setup
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
    result = conftest.sub_category_page.update_subcategory\
        ("Test Subcategory", category_option="Demo category", sub_category_name="Updated Subcategory")
    if "updated" in result.lower():
        toaster = conftest.base_page.get_toaster_message()
        conftest.log.info(toaster)
        print(result)
        assert True
    elif "added" in result.lower():
        toaster = conftest.base_page.get_toaster_message()
        conftest.log.error(toaster)
        assert "Sub Category added Successfully" in toaster, pytest.fail(f"Expected toaster not displayed, but got {toaster}")
    else:
        pytest.fail(f"Unexpected result from edit_subcategory: {result}")
        

@pytest.mark.smoke
def test_delete_subcategory(setup):
    conftest = setup
    result = conftest.sub_category_page.delete_subcategory("Updated Subcategory")
    if "deleted" in result.lower():
        toaster = conftest.base_page.get_toaster_message()
        conftest.log.info(toaster)
        print(result)
        assert "Sub Category removed successfully" in toaster, pytest.fail(f"Expected toaster not displayed, but got {toaster}")
    elif "removed" in result.lower():
        conftest.log.info("Sub category first added and then deleted successfully.")
        toaster = conftest.base_page.get_toaster_message()
        conftest.log.error(toaster)
        assert "Sub Category removed successfully" in toaster, pytest.fail(f"Expected toaster not displayed, but got {toaster}")
    else:
        pytest.fail(f"Unexpected result from edit_subcategory: {result}")
        
