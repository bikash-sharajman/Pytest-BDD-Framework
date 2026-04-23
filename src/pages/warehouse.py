import time

from selenium.common.exceptions import (
    ElementNotInteractableException,
    NoSuchElementException,
    StaleElementReferenceException,
    TimeoutException,
)
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec

from src.locators.common_locators import commonelements
from src.locators.warehouse_mstr_locators import warehouse_elements as wh
from src.pages.base_file import BasePage
from src.utils.screenshot import take_screenshot


class WarehousePage(BasePage):
    def __init__(self, driver, wait):
        super().__init__(driver, wait)

    def warehouse_master(self):
        try:
            if "warehouse" not in self.driver.current_url.lower():
                self.click_on(commonelements.overview_dashboard)
                self.redirect_to_master_module(commonelements.warehouse_master)
                self.wait.until(ec.url_contains("warehouse"))
                self.log.info("User is redirected to warehouse master page.")
            else:
                self.log.info("User is at warehouse master page.")
        except TimeoutException as e:
            take_screenshot(self.driver)
            self.log.error(f"TimeoutException in opening warehouse_master: {e}")
            return False
        return True

    def verify_value_on_warehouse_table(self, warehouse_name: str) -> bool:
        try:
            self.log.info(f"Validating '{warehouse_name}' in warehouse table.")
            item = self.wait.until(ec.presence_of_element_located(commonelements.logo))
            self.actions.move_to_element(item).perform()

            search = self.wait.until(
                ec.element_to_be_clickable((By.XPATH, "//input[@id='searchWarehouseInput']"))
            )
            search.clear()
            search.send_keys(warehouse_name)
            time.sleep(0.5)

            locator = (
                By.XPATH,
                f"//tbody[@class='p-datatable-tbody']//tr//td//ngb-highlight//span[normalize-space()='{warehouse_name}']",
            )

            try:
                self.wait.until(ec.presence_of_element_located(locator))
            except TimeoutException:
                self.log.warning(f"'{warehouse_name}' NOT found in warehouse table.")
                return False

            elements = self.driver.find_elements(*locator)
            if elements:
                self.log.info(f"'{warehouse_name}' exists in warehouse table.")
                return True

            self.log.warning(f"'{warehouse_name}' NOT found in warehouse table.")
            return False
        except (StaleElementReferenceException, TimeoutException, NoSuchElementException) as e:
            self.log.error(f"Error while validating warehouse '{warehouse_name}': {e}")
            return False

    def _fill_warehouse_form(self, warehouse_data: dict):
        dropdown_fields = {
            "warehouse_type_dd",
            "warehouse_subtype_dd",
            "warehouse_country_dd",
            "warehouse_incharge_dd",
        }
        warehouse_type = str(warehouse_data.get("warehouse_type_dd", ""))

        for field, value in warehouse_data.items():
            locator = getattr(wh, field, None)
            if locator is None or value is None:
                continue

            if field == "warehouse_subtype_dd" and "external" not in warehouse_type.lower():
                self.log.info("Warehouse subtype skipped because warehouse type is not EXTERNAL.")
                continue

            if field in dropdown_fields:
                self.select_dropdown_option(locator, value)
            else:
                self.enter_value(locator, str(value))

    def create_new_warehouse(self, warehouse_data: dict):
        try:
            self.warehouse_master()
            warehouse_name = warehouse_data.get("warehouse_name")
            result = self.verify_value_on_warehouse_table(warehouse_name)
            if result:
                self.log.info("Warehouse already exist.")
                take_screenshot(self.driver)
                return "Warehouse already exist"

            self.click_on(wh.add_warehouse_btn)
            self._fill_warehouse_form(warehouse_data)
            take_screenshot(self.driver)
            self.click_on(wh.warehouse_save_btn)
            self.log.info("Warehouse save button is clicked.")
            take_screenshot(self.driver)
            return "added"
        except (TimeoutException, StaleElementReferenceException,
                ElementNotInteractableException, NoSuchElementException) as e:
            msg = f"error: {type(e).__name__} in update_project: {e}"
            self.log.error(msg)
            return msg

    def update_warehouse(self, warehouse_data: dict, update_data: dict):
        try:
            self.warehouse_master()
            warehouse_name = warehouse_data.get("warehouse_name")
            if self.verify_value_on_warehouse_table(warehouse_name):
                self.log.info(f"{warehouse_name} warehouse exists.")
                self.click_on(commonelements.edit_icon)
                self._fill_warehouse_form(update_data)
                self.wait.until(ec.element_to_be_clickable((By.XPATH,"//button[normalize-space()='Update']"))).click()
                take_screenshot(self.driver)
                return "updated"

            self.log.warning(f"{warehouse_name} warehouse does not exist. Adding new warehouse.")
            return self.create_new_warehouse(warehouse_data)
        except (TimeoutException, StaleElementReferenceException,
                ElementNotInteractableException, NoSuchElementException) as e:
            msg = f"error: {type(e).__name__} in update_project: {e}"
            self.log.error(msg)
            return msg
        
        
    def delete_warehouse(self, warehouse_data:dict):
        try:
           self.warehouse_master()
           warehouse_name = f"Updated {warehouse_data['warehouse_name']}"
           if self.verify_value_on_warehouse_table(warehouse_name):
               self.log.info(f"{warehouse_name} is present on the moduel to delete.")
               self.click_on(commonelements.delete_icon)
               self.click_on(commonelements.delete_button)
               self.log.info("Delete button is clicked. Verifying the toaster........")
               return "deleted"
           else:
               return "Warehouse does not exist to delete."
            
        except (TimeoutException, StaleElementReferenceException,
                ElementNotInteractableException, NoSuchElementException) as e:
            msg = f"error: {type(e).__name__} in update_project: {e}"
            self.log.error(msg)
            return msg
        
