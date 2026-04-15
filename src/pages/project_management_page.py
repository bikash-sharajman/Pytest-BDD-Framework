import time
from datetime import datetime

from src.locators.base_file import BasePage
from src.locators.project_management_locators import pm
from src.locators.common_locators import commonelements

from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

from selenium.common.exceptions import (
    TimeoutException, StaleElementReferenceException, NoSuchElementException,
    ElementNotInteractableException)

from src.utils.screenshot import take_screenshot


class ProjectManagement(BasePage):
    def __init__(self, driver, wait):
        super().__init__(driver, wait)
    
    # def select_commission_date(self, date):
    #     date_picker = self.wait.until(ec.element_to_be_clickable(pm.commission_date_picker))
    #     self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", date_picker)
    #     date_picker.click()
    #     # day = datetime.now().day
    #     time.sleep(0.5)
    #     date = self.wait.until(ec.element_to_be_clickable((By.XPATH, f"//tbody//span[text() = '{date}']")))
    #     time.sleep(0.5)
    #     date.click()
    
    
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
            take_screenshot(self.driver)
            self.log.error(f"TimeoutException in open_project_management: {e}")
            return False
        return True

    def create_new_project(self, project_data: dict):
        dropdown_fields = {
        "state_dd", "cluster_dd", "billing_dd", "project_type_dd", "sub_type_dd",
        "technology_type_dd", "installation_type_dd", "mounting_type_dd",
        "warehouse_dd", "data_frequency_dd"}
        date_fields = {"commission_date_picker"}
        maps = {"mapping_button"}
        try:
            self.open_project_management()
            # project_name = project_data['project_name']
            # if self.verify_value_on_table(project_name):
            #     self.log.info(f"{project_name} already exist.")
            #     take_screenshot(self.driver)
            #     return "exist"
            self.click_on(pm.add_project_btn)
            # Fill in all required fields
            for field, value in project_data.items():
                locator = getattr(pm, field, None)
                if locator and value is not None:
                    if field in dropdown_fields:
                        self.select_dropdown_option(locator, value)
                    elif field in date_fields:
                        # self.enter_date(locator, value)
                        date_picker = self.wait.until(ec.element_to_be_clickable(pm.commission_date_picker))
                        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", date_picker)
                        date_picker.click()
                        day = datetime.now().day
                        time.sleep(1)
                        date = self.wait.until(ec.element_to_be_clickable((By.XPATH, f"//tbody//span[text() = '{day}']")))
                        self.driver.execute_script("arguments[0].click();", date)
                        # date.click()
                        self.log.info("date picker is clicked.")
                    elif field in maps:
                        map_field = self.wait.until(ec.element_to_be_clickable(pm.mapping_button))
                        map_field.click()
                        time.sleep(2)
                        map_point = self.wait.until(ec.element_to_be_clickable((By.XPATH, "//app-map-picker/div/div/div/div[3]/div[1]/div[1]")))
                        actions = ActionChains(self.driver)
                        actions.move_to_element_with_offset(map_point, 100, 50).click().perform()
                    else:
                        self.enter_value(locator, value)
            take_screenshot(self.driver)
            self.click_on(commonelements.modal_save_button)            
            self.log.info(f"{project_data.get('project_name')} created successfully.")
            take_screenshot(self.driver)
            
            self.click_on(pm.site_person_tab)
            self.click_on(pm.add_person_button)
            self.wait.until(ec.element_to_be_clickable(pm.site_person_tab_search_bar)).send_keys("8249973673")
            time.sleep(1)
            self.wait.until(ec.element_to_be_clickable((By.XPATH, "//li[@role='option']//span"))).click()
            self.click_on(pm.role_type_dd)
            self.click_on(pm.site_tech_option)
            self.click_on(commonelements.modal_save_button)
            self.log.info("project privilege provided.")
            take_screenshot(self.driver)
            return "added"
        except TimeoutException as e:
            take_screenshot(self.driver)
            msg = f"TimeoutException in create_new_project: {e}"
            self.log.error(msg)
            return msg
        except StaleElementReferenceException as e:
            take_screenshot(self.driver)
            msg = f"StaleElementReferenceException in create_new_project: {e}"
            self.log.error(msg)
            return msg
        except ElementNotInteractableException as e:
            take_screenshot(self.driver)
            msg = f"ElementNotInteractableException in create_new_project: {e}"
            self.log.error(msg)
            return msg
        except NoSuchElementException as e:
            take_screenshot(self.driver)
            msg = f"NoSuchElementException in create_new_project: {e}"
            self.log.error(msg)
            return msg

    def update_project(self,project_data: dict, update_data: dict):
        dropdown_fields = {
        "state_dd", "cluster_dd", "billing_dd", "project_type_dd", "sub_type_dd",
        "technology_type_dd", "installation_type_dd", "mounting_type_dd",
        "warehouse_dd", "data_frequency_dd"
    }
        date_fields = {"commission_date_picker"}
        try:
            self.open_project_management()
            if self.verify_value_on_table(project_data.get('project_name')):
                self.log.info(f"{project_data.get('project_name')} project exists.")
                self.click_on(commonelements.edit_icon)
                for field, value in update_data.items():
                    locator = getattr(pm, field, None)
                    if locator and value is not None:
                        if field in dropdown_fields:
                            self.select_dropdown_option(locator, value)
                        elif field in date_fields:
                            date_picker = self.wait.until(ec.element_to_be_clickable(pm.commission_date_picker))
                            self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", date_picker)
                            date_picker.click()
                            day = datetime.now().day
                            time.sleep(1)
                            date = self.wait.until(ec.element_to_be_clickable((By.XPATH, f"//tbody//span[text() = '{day}']")))
                            date.click()
                        else:
                            self.enter_value(locator, value)
                self.click_on(commonelements.update_button)
                take_screenshot(self.driver)
                return "updated"
            else:
                self.log.warning(f"{update_data.get('project_name')} project does not exist. Adding new project.")
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


    
    
    
    
    
        
