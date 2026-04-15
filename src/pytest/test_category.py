import pytest


@pytest.mark.testing
def test_add_new_category(setup):
    conftest = setup
    result = conftest.category_page.add_new_category("Test category")
    if "already exists" in result:
        print("Category already exists, skipping toaster check.")
        assert True
    else:    
        toaster = conftest.base_page.get_toaster_message()
        assert "New Category created successfully" in toaster, pytest.fail(f"Expected toaster not displayed, but got {toaster}")
    
@pytest.mark.testing
def test_udpate_category(setup):
    conftest = setup
    conftest.category_page.update_category("Test category", "Updated category")
    toaster = conftest.base_page.get_toaster_message()
    assert "Category updated successfully" in toaster,\
        pytest.fail(f"Expected toaster not displayed, but got {toaster}")

@pytest.mark.testing
def test_delete_category(setup):
    conftest = setup
    conftest.category_page.delete_category("Updated category")
    toaster = conftest.base_page.get_toaster_message()
    assert "Category deleted successfully." in toaster,\
        pytest.fail(f"Expected toaster message does not appear, but get {toaster}")
