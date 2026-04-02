import time
from datetime import datetime

from src.locators.base_file import BasePage
from src.locators.project_management_locators import pm
from src.locators.common_locators import commonelements

from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By

from selenium.common.exceptions import (
    TimeoutException, StaleElementReferenceException, NoSuchElementException,
    ElementNotInteractableException)


class ProjectManagement(BasePage):
    def __init__(self, driver, wait):
        super().__init__(driver, wait)

    def select_current_commissioning_date(self):
        try:
            self.log.info("Selecting current commissioning date from date picker.")
            date_picker = self.wait.until(ec.element_to_be_clickable(pm.commission_date_picker))
            self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", date_picker)
            date_picker.click()

            current_day = str(datetime.now().day)
            day_locator = (
                By.XPATH,
                f"//table[contains(@class,'p-datepicker-calendar')]//td[not(contains(@class,'p-disabled'))]//span[normalize-space()='{current_day}']"
            )
            self.wait.until(ec.element_to_be_clickable(day_locator)).click()
            self.log.info(f"Current commissioning date selected: {current_day}")
        except TimeoutException as e:
            self.take_screenshot(self.driver)
            msg = f"TimeoutException in select_current_commissioning_date: {e}"
            self.log.error(msg)
            return msg
        except NoSuchElementException as e:
            self.take_screenshot(self.driver)
            msg = f"NoSuchElementException in select_current_commissioning_date: {e}"
            self.log.error(msg)
            return msg
        return "selected"

    
    def open_project_management(self):
        
        try:
            if "plant-management" not in self.driver.current_url.lower():
                self.click_on(commonelements.overview_dashboard)
                self.redirect_to(commonelements.management_menu, commonelements.project_management)
                self.wait.until(ec.url_contains("plant-management"))
                self.log.info("User is redirected to project management page.")
            else:
                self.log.info("User is at project management module.")
        except TimeoutException as e:
            self.take_screenshot(self.driver)
            self.log.error(f"TimeoutException in open_project_management: {e}")
            return False
        return True

    def create_new_project(self, project_data: dict):
        dropdown_fields = {
        "state_dd", "cluster_dd", "billing_dd", "project_type_dd", "sub_type_dd",
        "technology_type_dd", "installation_type_dd", "mounting_type_dd",
        "warehouse_dd", "data_frequency_dd"
    }
        date_fields = {"commission_date_picker"}
        try:
            self.open_project_management()
            project_name = project_data.get("project_name")
            if self.verify_value_on_table(project_name):
                self.log.info(f"{project_name} already exist.")
                self.take_screenshot(self.driver)
                return "exist"
            self.click_on(pm.add_project_btn)
            # Fill in all required fields
            for field, value in project_data.items():
                locator = getattr(pm, field, None)
                if locator and value is not None:
                    if field in dropdown_fields:
                        self.select_dropdown_option(locator, value)
                    elif field in date_fields:
                        self.enter_date(locator, value)
                    else:
                        self.enter_value(locator, value)
            self.take_screenshot(self.driver)
            self.click_on(commonelements.modal_save_button)            
            self.log.info(f"{project_name} created successfully.")
            self.take_screenshot(self.driver)
            
            self.click_on(pm.site_person_tab)
            self.click_on(pm.add_person_button)
            self.wait.until(ec.element_to_be_clickable(pm.site_person_tab_search_bar)).send_keys("8249973673")
            time.sleep(1)
            self.wait.until(ec.element_to_be_clickable((By.XPATH, "//li[@role='option']//span"))).click()
            self.click_on(pm.role_type_dd)
            self.click_on(pm.site_tech_option)
            self.click_on(commonelements.modal_save_button)
            self.log.info("project privilege provided.")
            self.take_screenshot(self.driver)
            return "added"
        except TimeoutException as e:
            self.take_screenshot(self.driver)
            msg = f"TimeoutException in create_new_project: {e}"
            self.log.error(msg)
            return msg
        except StaleElementReferenceException as e:
            self.take_screenshot(self.driver)
            msg = f"StaleElementReferenceException in create_new_project: {e}"
            self.log.error(msg)
            return msg
        except ElementNotInteractableException as e:
            self.take_screenshot(self.driver)
            msg = f"ElementNotInteractableException in create_new_project: {e}"
            self.log.error(msg)
            return msg
        except NoSuchElementException as e:
            self.take_screenshot(self.driver)
            msg = f"NoSuchElementException in create_new_project: {e}"
            self.log.error(msg)
            return msg

    def update_project(self, search_project, update_data: dict):
        dropdown_fields = {
        "state_dd", "cluster_dd", "billing_dd", "project_type_dd", "sub_type_dd",
        "technology_type_dd", "installation_type_dd", "mounting_type_dd",
        "warehouse_dd", "data_frequency_dd"
    }
        date_fields = {"commission_date_picker"}
        try:
            self.open_project_management()
            if self.verify_value_on_table(search_project):
                self.log.info(f"{search_project} project exists.")
                self.click_on(commonelements.edit_icon)
                for field, value in update_data.items():
                    locator = getattr(pm, field, None)
                    if locator and value is not None:
                        if field in dropdown_fields:
                            self.select_dropdown_option(locator, value)
                        elif field in date_fields:
                            self.enter_date(locator, value)
                        else:
                            self.enter_value(locator, value)
                self.click_on(commonelements.update_button)
                self.take_screenshot(self.driver)
                return "updated"
            else:
                self.log.warning(f"{search_project} project does not exist. Adding new project.")
                return self.create_new_project(update_data)
        except TimeoutException as e:
            msg = f"TimeoutException in update_project: {e}"
            self.log.error(msg)
            return msg
        except StaleElementReferenceException as e:
            msg = f"StaleElementReferenceException in update_project: {e}"
            self.log.error(msg)
            return msg
        except ElementNotInteractableException as e:
            msg = f"ElementNotInteractableException in update_project: {e}"
            self.log.error(msg)
            return msg
        except NoSuchElementException as e:
            msg = f"NoSuchElementException in update_project: {e}"
            self.log.error(msg)
            return msg


    
    
    
    
    
        
