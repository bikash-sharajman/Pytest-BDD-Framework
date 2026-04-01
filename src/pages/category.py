from src.locators.base_file import BasePage
from src.locators.common_locators import commonelements
from src.locators.category_mstr_locators import categoryelement
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import (
    TimeoutException,
    StaleElementReferenceException,
    ElementNotInteractableException,
    NoSuchElementException
)


class CategoryPage(BasePage):
    def __init__(self, driver, wait):
        super().__init__(driver, wait)
        
    def open_category_master(self):
        try:
            url = self.driver.current_url
            if "category-master" not in url.lower():
                self.click_on(commonelements.side_bar)
                self.redirect_to(commonelements.master_menu, commonelements.category_master)
                self.wait.until(ec.url_contains("category-master"))
            else:
                self.log.info("User is at category module.")
        except TimeoutException as e:
            print(f"TimeoutException in open_category_master: {e}")
        except StaleElementReferenceException as e:
            print(f"StaleElementReferenceException in open_category_master: {e}")
        except ElementNotInteractableException as e:
            print(f"ElementNotInteractableException in oopen_category_master: {e}")
        except NoSuchElementException as e:
            print(f"NoSuchElementException in open_category_master: {e}")

        
    def add_new_category(self, category):
        try:
            self.open_category_master()
            if self.verify_value_on_table(category):
                self.log.info("Category already exists.")
                return("Category already exists.")
            else:
                self.log.info(f"{category} not found, adding the new make {category}.")
                self.click_on(categoryelement.add_category_btn)
                self.enter_value(categoryelement.category_input, category)
                self.click_on(commonelements.modal_save_button)
                return f"{category} added successfully."
        except TimeoutException as e:
            self.log.error(f"TimeoutException in create_new_make: {e}")
            return e
        except StaleElementReferenceException as e:
            self.log.error(f"StaleElementReferenceException in create_new_make: {e}")
            return e
        except ElementNotInteractableException as e:
            self.log.error(f"ElementNotInteractableException in create_new_make: {e}")
            return e
        except NoSuchElementException as e:
            self.log.error(f"NoSuchElementException in create_new_make: {e}")
            return e
    
    def update_category(self, category_name, updated_category_name):
        try:
            self.open_category_master()
            if self.verify_value_on_table(category_name):
                self.log.info("Category already exists.")
                self.click_on(commonelements.edit_icon)
                self.enter_value(categoryelement.category_input, updated_category_name)
                self.click_on(commonelements.update_button)
            else:
                self.click_on(categoryelement.add_category_btn)
                self.enter_value(categoryelement.category_input, category_name)
                self.click_on(commonelements.modal_save_button)
                self.click_on(commonelements.toaster)
                self.search(category_name)
                self.click_on(commonelements.edit_icon)
                self.enter_value(categoryelement.category_input, updated_category_name)
                self.click_on(commonelements.update_button)
            self.log.info(f"{category_name} is successfully updated with {updated_category_name}.")
        except TimeoutException as e:
            self.log.error(f"TimeoutException in create_new_make: {e}")
            return e
        except StaleElementReferenceException as e:
            self.log.error(f"StaleElementReferenceException in create_new_make: {e}")
            return e
        except ElementNotInteractableException as e:
            self.log.error(f"ElementNotInteractableException in create_new_make: {e}")
            return e
        except NoSuchElementException as e:
            self.log.error(f"NoSuchElementException in create_new_make: {e}")
            return e
        
    
    def delete_category(self, category_name):
        try:
            self.open_category_master()
            if self.verify_value_on_table(category_name):
                self.log.info("Category already exists.")
                self.click_on(commonelements.delete_icon)
                self.click_on(commonelements.delete_button)
            else:
                self.click_on(categoryelement.add_category_btn)
                self.enter_value(categoryelement.category_input, category_name)
                self.click_on(commonelements.modal_save_button)
                self.click_on(commonelements.toaster)
                self.search(category_name)
                self.click_on(commonelements.delete_icon)
                self.click_on(commonelements.delete_button)
            self.log.info(f"{category_name} is successfully deleted.")
        except TimeoutException as e:
            self.log.error(f"TimeoutException in create_new_make: {e}")
            return e
        except StaleElementReferenceException as e:
            self.log.error(f"StaleElementReferenceException in create_new_make: {e}")
            return e
        except ElementNotInteractableException as e:
            self.log.error(f"ElementNotInteractableException in create_new_make: {e}")
            return e
        except NoSuchElementException as e:
            self.log.error(f"NoSuchElementException in create_new_make: {e}")
            return e
    

        
    