from src.locators.base_file import BasePage
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
            url = self.driver.current_url
            if "no-privilege" in url.lower():
                self.log.warning("No authorization to access the make master.")
                self.click_on(commonelements.go_back_button)
                return self.driver.quit()
            elif "make" not in url.lower():
                self.click_on(commonelements.overview_dashboard)
                self.redirect_to(commonelements.master_menu, commonelements.make_master)
                self.wait.until(ec.url_contains("make"))
                self.log.info("User is redirected to make master page.")
            else:
                self.log.info("User is at make module.")
        except TimeoutException as e:
            print(f"TimeoutException in open_make_master: {e}")
            

    def create_new_make(self, make):
        try:
            self.open_make_master()
            table_result = self.verify_value_on_table(make)
            if table_result:
                self.log.info("Make already exists.")
                take_screenshot(self.driver)
                return("Make already exists")
            
            else:
                self.log.info(f"{make} not found, adding the new make {make}.")
                self.click_on(makeelement.add_make)
                self.enter_value(makeelement.make_input, make)
                self.click_on(commonelements.modal_save_button)
                self.log.info(f"{make} is sucessfully added into system.")
                take_screenshot(self.driver)
                return "Make added successfully."
        except TimeoutException as e:
            self.log.error(f"TimeoutException in create_new_make: {e}")
            take_screenshot(self.driver)
            return e
        except StaleElementReferenceException as e:
            self.log.error(f"StaleElementReferenceException in create_new_make: {e}")
            take_screenshot(self.driver)
            return e
        except ElementNotInteractableException as e:
            self.log.error(f"ElementNotInteractableException in create_new_make: {e}")
            take_screenshot(self.driver)
            return e
        except NoSuchElementException as e:
            self.log.error(f"NoSuchElementException in create_new_make: {e}")
            take_screenshot(self.driver)
            return e
        
    def update_make(self, make_name, updated_make):
        try:
            self.open_make_master()
            table_result = self.verify_value_on_table(make_name)
            if table_result:
                self.log.info("Make already exists.")
                self.click_on(commonelements.edit_icon)
                self.enter_value(makeelement.make_input, updated_make)
                self.click_on(commonelements.update_button)
                take_screenshot(self.driver)
            else:
                self.click_on(makeelement.add_make)
                self.enter_value(makeelement.make_input, make_name)
                self.click_on(commonelements.modal_save_button)
                self.click_on(commonelements.toaster)
                self.search(make_name)
                self.click_on(commonelements.edit_icon)
                self.enter_value(makeelement.make_input, updated_make)
                self.click_on(commonelements.update_button)
                take_screenshot(self.driver)
            self.log.info(f"{make_name} is successfully updated with {updated_make}.")
        except TimeoutException as e:
            self.log.error(f"TimeoutException in update_make: {e}")
            take_screenshot(self.driver)
            return e
        except StaleElementReferenceException as e:
            self.log.error(f"StaleElementReferenceException in update_make: {e}")
            take_screenshot(self.driver)
            return e
        except ElementNotInteractableException as e:
            self.log.error(f"ElementNotInteractableException in update_make: {e}")
            take_screenshot(self.driver)
            return e
        except NoSuchElementException as e:
            self.log.error(f"NoSuchElementException in update_make: {e}")
            take_screenshot(self.driver)
            return e
    


    def delete_make(self, make_name):
        try:
            self.open_make_master()
            table_result = self.verify_value_on_table(make_name)
            if table_result:
                self.log.info("Make already exists.")
                self.click_on(commonelements.delete_icon)
                self.click_on(commonelements.delete_button)
                take_screenshot(self.driver)
            else:
                self.click_on(makeelement.add_make)
                self.enter_value(makeelement.make_input, make_name)
                self.click_on(commonelements.modal_save_button)
                self.click_on(commonelements.toaster)
                self.search(make_name)
                self.click_on(commonelements.delete_icon)
                self.click_on(commonelements.delete_button)
            self.log.info(f"{make_name} is successfully deleted.")
            toaster = self.get_toaster_message()
            take_screenshot(self.driver)
            assert "Make deleted successfully" in toaster, f"Expected toaster not displayed, but got {toaster}"
        except TimeoutException as e:
            self.log.error(f"TimeoutException in delete_make: {e}")
            take_screenshot(self.driver)
            return e
        except StaleElementReferenceException as e:
            self.log.error(f"StaleElementReferenceException in delete_make: {e}")
            take_screenshot(self.driver)
            return e
        except ElementNotInteractableException as e:
            self.log.error(f"ElementNotInteractableException in delete_make: {e}")
            take_screenshot(self.driver)
            return e
        except NoSuchElementException as e:
            self.log.error(f"NoSuchElementException in delete_make: {e}")
            take_screenshot(self.driver)
            return e
                
                        
            
            


