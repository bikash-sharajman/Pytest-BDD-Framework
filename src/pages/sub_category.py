from src.pages.base_file import BasePage
from src.locators.common_locators import commonelements
from src.locators.subcat_mstr_locators import subcategory_elements
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import (TimeoutException,
        StaleElementReferenceException, ElementNotInteractableException,
        ElementNotSelectableException, NoSuchElementException)



class SubCategory(BasePage):
    def __init__(self, driver, wait):
        super().__init__(driver, wait)
        
    def open_sub_category_master(self):
        url = self.driver.current_url
        if "subcategory" not in url.lower:
            self.click_on(commonelements.side_bar)
            self.redirect_to(commonelements.master_menu, commonelements.sub_category_master)
            self.wait.until(ec.url_contains("subcategory-master"))
    
    def add_new_subcategory(self, category_option, sub_category_name):
        try:
            self.open_sub_category_master()
            self.click_on(subcategory_elements.add_sub_category_btn)
            self.select_dropdown_option(subcategory_elements.subCat_category_dd, category_option)
            self.enter_value(subcategory_elements.subCat_input, sub_category_name)
            self.click_on(commonelements.modal_save_button)
        except TimeoutException as e:
            print(f"TimeoutException in edit_sub_category: {e}")
        except StaleElementReferenceException as e:
            print(f"StaleElementReferenceException in edit_sub_category: {e}")
        except ElementNotInteractableException as e:
            print(f"ElementNotInteractableException in edit_sub_category: {e}")
        except ElementNotSelectableException as e:
            print(f"ElementNotSelectableException in edit_sub_category: {e}")
        except NoSuchElementException as e:
            print(f"NoSuchElementException in edit_sub_category: {e}")
            
        
    def edit_sub_category(self, search_subcat, category_option=None, sub_category_name=None):
        try:
            self.open_sub_category_master()
            self.search(search_subcat)
            self.click_on(commonelements.edit_icon)
            if category_option is not None:
                self.select_dropdown_option(subcategory_elements.subCat_category_dd, category_option)
            if sub_category_name is not None:
                self.enter_value(subcategory_elements.subCat_input, sub_category_name)
            self.click_on(commonelements.update_button)
        except TimeoutException as e:
            print(f"TimeoutException in edit_sub_category: {e}")
        except StaleElementReferenceException as e:
            print(f"StaleElementReferenceException in edit_sub_category: {e}")
        except ElementNotInteractableException as e:
            print(f"ElementNotInteractableException in edit_sub_category: {e}")
        except ElementNotSelectableException as e:
            print(f"ElementNotSelectableException in edit_sub_category: {e}")
        except NoSuchElementException as e:
            print(f"NoSuchElementException in edit_sub_category: {e}")
        
    def delete_subcategory(self, search_subcat):
        try:
            self.open_sub_category_master()
            self.search(search_subcat)        
            self.click_on(commonelements.delete_icon)
            self.click_on(commonelements.delete_button)
        except (TimeoutException,
            StaleElementReferenceException,
            ElementNotInteractableException,
            ElementNotSelectableException,
            NoSuchElementException) as e:
            print(f"Exception in edit_sub_category: {type(e).__name__}: {e}")
            

        

        
        
            