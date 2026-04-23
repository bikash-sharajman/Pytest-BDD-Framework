from src.pages.base_file import BasePage
from src.locators.common_locators import commonelements
from src.locators.make_mstr_locators import makeelement
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import (TimeoutException,
        StaleElementReferenceException, ElementNotInteractableException,
        NoSuchElementException)

from src.utils.screenshot import take_screenshot


class MakePage(BasePage):

    def __init__(self, driver, wait):
        super().__init__(driver, wait)

    def open_make_master(self):
        try:
            if "make" not in self.driver.current_url.lower():
                self.click_on(commonelements.overview_dashboard)
                self.redirect_to_master_module(commonelements.make_master)
                self.wait.until(ec.url_contains("make"))
                self.log.info("User is redirected to make master page.")
            else:
                self.log.info("User is at make module.")
        except TimeoutException as e:
            self.log.error(f"Failed to open Make Master: {e}")
            raise
            

    def create_new_make(self, make):
        try:
            self.open_make_master()
            table_result = self.verify_value_on_table(make)
            if table_result:
                self.log.info(f"{make} already exists.")
                return "already exists"
            else:
                self.log.info(f"{make} not found, adding the new make {make}.")
                self.click_on(makeelement.add_make)
                self.enter_value(makeelement.make_input, make)
                self.click_on(commonelements.modal_save_button)
                self.log.info(f"{make} is sucessfully added into system.")
                return "added"
        except (TimeoutException, StaleElementReferenceException,
                ElementNotInteractableException, NoSuchElementException) as e:
            take_screenshot(self.driver)
            msg = f"error: {type(e).__name__} in create_new_make: {e}"
            self.log.error(msg)
            return msg

        
    def update_make(self, make_name, updated_make):
        try:
            self.open_make_master()
            table_result = self.verify_value_on_table(make_name)
            if table_result:
                self.log.info("Make already exists.")
                self.click_on(commonelements.edit_icon)
                self.enter_value(makeelement.make_input, updated_make)
                self.click_on(commonelements.update_button)
                self.log.info(f"'{make_name}' updated to '{updated_make}'.")
                return "updated"
            else:
                self.log.warning(f"'{make_name}' not found — creating before update.")
                self.click_on(makeelement.add_make)
                self.enter_value(makeelement.make_input, make_name)
                self.click_on(commonelements.modal_save_button)
                self.click_on(commonelements.toaster)
                self.search(make_name)
                self.click_on(commonelements.edit_icon)
                self.enter_value(makeelement.make_input, updated_make)
                self.click_on(commonelements.update_button)
                self.log.info(f"'{make_name}' created and updated to '{updated_make}'.")
                return "changed"
            
        except (TimeoutException, StaleElementReferenceException,
                ElementNotInteractableException, NoSuchElementException) as e:
            msg = f"error: {type(e).__name__} in update_make: {e}"
            self.log.error(msg)
            return msg
    
    def delete_make(self, make_name):
        try:
            self.open_make_master()
            if self.verify_value_on_table(make_name):
                self.log.info(f"{make_name} already exists.")
                self.click_on(commonelements.delete_icon)
                self.click_on(commonelements.delete_button)
                self.log.info(f"'{make_name}' deleted successfully.")
                return "deleted"
            else:
                self.log.warning(f"'{make_name}' not found — creating before delete.")
                self.click_on(makeelement.add_make)
                self.enter_value(makeelement.make_input, make_name)
                self.click_on(commonelements.modal_save_button)
                self.click_on(commonelements.toaster)
                self.search(make_name)
                self.click_on(commonelements.delete_icon)
                self.click_on(commonelements.delete_button)
                self.log.info(f"'{make_name}' created and deleted.")
                return "removed"
            
        except (TimeoutException, StaleElementReferenceException,
                ElementNotInteractableException, NoSuchElementException) as e:
            msg = f"error: {type(e).__name__} in delete_make: {e}"
            self.log.error(msg)
            return msg
                
                
                

            


