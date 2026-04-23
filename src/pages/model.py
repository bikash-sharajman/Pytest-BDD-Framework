from src.pages.base_file import BasePage
from src.locators.common_locators import commonelements
from src.locators.model_mstr_locators import modelelements
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import (TimeoutException,
        StaleElementReferenceException, ElementNotInteractableException,
        NoSuchElementException)

from src.utils.screenshot import take_screenshot



class Model(BasePage):
    def __init__(self, driver, wait):
        super().__init__(driver, wait)
    
    def open_model_master(self):
        try:
            url = self.driver.current_url
            if "model" not in url.lower():
                self.click_on(commonelements.overview_dashboard)
                self.redirect_to_master_module(commonelements.model_master)
                self.wait.until(ec.url_contains("model"))
                self.log.info("User is redirected to model master page.")
            else:
                self.log.info("User is at model module.")
        except TimeoutException as e:
            print(f"TimeoutException in open_model_master: {e}")
            
    def add_new_model(self, model_name, category_name, make_name, sub_category_name):
        try:
            self.open_model_master()
            result = self.verify_value_on_table(model_name)
            if result:
                self.log.info("Model already exist.")
                take_screenshot(self.driver)
                return "Model already exist"
            else:
                self.log.info(f"{model_name} not found, adding the new model {model_name}.")
                self.click_on(modelelements.add_model_btn)
                self.select_dropdown_option(modelelements.model_make_dd, make_name)
                self.select_dropdown_option(modelelements.model_category_dd, category_name)
                self.select_dropdown_option(modelelements.model_sub_category_dd, sub_category_name)
                self.enter_value(modelelements.model_input, model_name)
                self.click_on(commonelements.modal_save_button)
                take_screenshot(self.driver)
                return "Model added successfully."   
        except (TimeoutException, StaleElementReferenceException,
                ElementNotInteractableException, NoSuchElementException) as e:
            msg = f"error: {type(e).__name__} in update_project: {e}"
            self.log.error(msg)
            return msg
            
        
    def edit_model(self, model_name, new_make_name=None, new_category_name=None, new_subcat_name=None, 
                   updated_model_name=None):
        try:
            self.open_model_master()
            table_result = self.verify_value_on_table(model_name)
            if table_result:
                
                self.click_on(commonelements.edit_icon)
                if new_make_name is not None:
                    self.select_dropdown_option(modelelements.model_make_dd, new_make_name)
                if new_category_name is not None:
                    self.select_dropdown_option(modelelements.model_category_dd, new_category_name)
                if new_subcat_name is not None:
                    self.select_dropdown_option(modelelements.model_sub_category_dd, new_subcat_name)
                if updated_model_name is not None:
                    self.enter_value(modelelements.model_input, updated_model_name)
                self.click_on(commonelements.update_button)
                take_screenshot(self.driver)
            else:
                self.log.info(f"{updated_model_name} not found, creating the model then update it.")
                self.click_on(modelelements.add_model_btn)
                self.select_dropdown_option(modelelements.model_make_dd, "Demo Make")
                self.select_dropdown_option(modelelements.model_category_dd, "Devices")
                self.select_dropdown_option(modelelements.model_sub_category_dd, "SCADA")
                self.enter_value(modelelements.model_input, model_name)
                self.click_on(commonelements.modal_save_button)
                self.click_on(commonelements.toaster)
                self.search(model_name)
                self.click_on(commonelements.edit_icon)
                if updated_model_name is not None:
                    self.enter_value(modelelements.model_input, updated_model_name)
                self.click_on(commonelements.update_button)
                take_screenshot(self.driver)
                return "created"
            self.log.info(f"{model_name} is successfully updated with {updated_model_name}.")
            return "updated"
        except (TimeoutException, StaleElementReferenceException,
                ElementNotInteractableException, NoSuchElementException) as e:
            msg = f"error: {type(e).__name__} in update_project: {e}"
            self.log.error(msg)
            return msg
        
    def delete_model(self, model_name, make_name, category_name, subcat_name):
        try:
            self.open_model_master()
            table_result = self.verify_value_on_table(model_name)
            if table_result:
                self.log.info("Model already exists.")
                self.click_on(commonelements.delete_icon)
                self.click_on(commonelements.delete_button)
                return "deleted"
            else:
                self.click_on(modelelements.add_model_btn)
                self.select_dropdown_option(modelelements.model_make_dd, make_name)
                self.select_dropdown_option(modelelements.model_category_dd, category_name)
                self.select_dropdown_option(modelelements.model_sub_category_dd, subcat_name)
                self.enter_value(modelelements.model_input, model_name)
                self.click_on(commonelements.modal_save_button)
                self.click_on(commonelements.toaster)
                self.search(model_name)
                self.click_on(commonelements.delete_icon)
                self.click_on(commonelements.delete_button)
                return "removed"
        
        except (TimeoutException, StaleElementReferenceException,
                ElementNotInteractableException, NoSuchElementException) as e:
            msg = f"error: {type(e).__name__} in update_project: {e}"
            self.log.error(msg)
            return msg
        
    
        
            
    
        


