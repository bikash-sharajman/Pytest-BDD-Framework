from src.pages.base_file import BasePage
from src.locators.common_locators import commonelements
from src.locators.category_mstr_locators import categoryelement
from selenium.webdriver.support import expected_conditions as ec
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
            if "category-master" not in self.driver.current_url.lower():
                self.click_on(commonelements.overview_dashboard)
                self.redirect_to_master_module(commonelements.category_master)
                self.wait.until(ec.url_contains("category-master"))
                self.log.info("Navigated to Category Master page.")
            else:
                self.log.info("User is already at category module.")
        except TimeoutException as e:
            self.log.error(f"TimeoutException in open_category_master: {e}")
            raise
        
        
    def add_new_category(self, category):
        try:
            self.open_category_master()
            if self.verify_value_on_table(category):
                self.log.info(f"{category} already exists.")
                return "already exists"
            else:
                self.log.info(f"{category} not found, adding the new category.")
                self.click_on(categoryelement.add_category_btn)
                self.enter_value(categoryelement.category_input, category)
                self.log.info(f"'{category}' added successfully.")
                return "added"
        except (TimeoutException, StaleElementReferenceException,
                ElementNotInteractableException, NoSuchElementException) as e:
            msg = f"error: {type(e).__name__} in add_new_category: {e}"
            self.log.error(msg)
            return msg
    
    def update_category(self, category_name, updated_category_name):
        try:
            self.open_category_master()
            if self.verify_value_on_table(category_name):
                self.log.info(f"{category_name} exists. Updating.....")
                self.click_on(commonelements.edit_icon)
                self.enter_value(categoryelement.category_input, updated_category_name)
                self.click_on(commonelements.update_button)
                self.log.info(f"'{category_name}' updated to '{updated_category_name}'.")
                return "updated"
            else:
                self.log.warning(f"'{category_name}' not found — creating before update.")
                self.click_on(categoryelement.add_category_btn)
                self.enter_value(categoryelement.category_input, category_name)
                self.click_on(commonelements.modal_save_button)
                self.click_on(commonelements.toaster)
                self.search(category_name)
                self.click_on(commonelements.edit_icon)
                self.enter_value(categoryelement.category_input, updated_category_name)
                self.click_on(commonelements.update_button)
                self.log.info(f"'{category_name}' created and updated to '{updated_category_name}'.")
                return "updated"
        
        except (TimeoutException, StaleElementReferenceException,
                ElementNotInteractableException, NoSuchElementException) as e:
            msg = f"error: {type(e).__name__} in update_category: {e}"
            self.log.error(msg)
            return msg
        
    
    def delete_category(self, category_name):
        try:
            self.open_category_master()
            if self.verify_value_on_table(category_name):
                self.log.info(f"{category_name} exists. Deleting...")
                self.click_on(commonelements.delete_icon)
                self.click_on(commonelements.delete_button)
                self.log.info(f"'{category_name}' deleted.")
                return "deleted"
            else:
                self.log.warning(f"'{category_name}' not found — creating before delete.")
                self.click_on(categoryelement.add_category_btn)
                self.enter_value(categoryelement.category_input, category_name)
                self.click_on(commonelements.modal_save_button)
                self.click_on(commonelements.toaster)
                self.search(category_name)
                self.click_on(commonelements.delete_icon)
                self.click_on(commonelements.delete_button)
                self.log.info(f"'{category_name}' created and deleted.")
                return "deleted"

        except (TimeoutException, StaleElementReferenceException,
                ElementNotInteractableException, NoSuchElementException) as e:
            msg = f"error: {type(e).__name__} in delete_category: {e}"
            self.log.error(msg)
            return msg
    

        
    