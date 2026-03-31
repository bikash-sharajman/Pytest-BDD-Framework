import pytest
from src.locators.subcat_mstr_locators import subcategory_elements
from src.locators.common_locators import commonelements
from src.pages.sub_category import SubCategory
from src.initialization.config_reader import confr
from src.utils.screenshot import take_screenshot
from selenium.common.exceptions import (
    TimeoutException, StaleElementReferenceException,
     ElementNotInteractableException,
    ElementNotSelectableException, NoSuchElementException 
)


# @pytest.mark.testing
def test_add_new_subcategory(setup):
    
    conftest = setup
    conftest.login_page.login(confr.email, confr.password)
    conftest.subCategory_page.open_sub_category_master()
    conftest.subCategory_page.add_new_subcategory("Demo category", "Demo Subcategory")
    toaster = conftest.base_page.get_toaster_message()
    assert "Sub Category added Successfully" in toaster, \
        f"Incorrect toaster message appeared while creating the sub category."
    take_screenshot(conftest.driver)
    

# def test_edit_subcategory(setup):
#     conftest = setup
    

@pytest.mark.testing
def test_delete_subcategory(setup):
    conftest = setup
    conftest.login_page.login(confr.email, confr.password)
    conftest.subCategory_page.open_sub_category_master()
    conftest.subCategory_page.search("demo test subcategory")
    conftest.subCategory_page.click_on(commonelements.delete_icon)
    conftest.subCategory_page.click_on(commonelements.delete_button)

    

    
        
        
    
    
    
        