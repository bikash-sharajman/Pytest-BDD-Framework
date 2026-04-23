from src.pages.base_file import BasePage
from src.locators.common_locators import commonelements
from src.locators.subcat_mstr_locators import subcategory_elements
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import (
    TimeoutException,
    StaleElementReferenceException,
    ElementNotInteractableException,
    NoSuchElementException
)

class SubCategoryPage(BasePage):

    def __init__(self, driver, wait):
        super().__init__(driver, wait)

    def open_sub_category_master(self):
        try:
            url = self.driver.current_url
            if "subcategory-master" not in url.lower():
                self.click_on(commonelements.overview_dashboard)
                self.redirect_to_master_module(commonelements.sub_category_master)
                self.wait.until(ec.url_contains("subcategory"))
                self.log.info("User is redirected to subcategory master page.")
            else:
                self.log.info("User is at subcategory module.")
        except TimeoutException as e:
            print(f"TimeoutException in open_sub_category_master: {e}")

    def create_new_subcategory(self, category_option, sub_category_name):
        try:
            self.open_sub_category_master()
            if self.verify_value_on_table(sub_category_name):
                self.log.info(f"{sub_category_name} already exist.")
                return "exist"
            self.click_on(subcategory_elements.add_sub_category_btn)
            self.select_dropdown_option(subcategory_elements.subCat_category_dd, category_option)
            self.enter_value(subcategory_elements.subCat_input, sub_category_name)
            self.click_on(commonelements.modal_save_button)
            self.log.info(f"{sub_category_name} created successfully.")
            return "added"
        except (TimeoutException, StaleElementReferenceException,
                ElementNotInteractableException, NoSuchElementException) as e:
            msg = f"error: {type(e).__name__} in update_project: {e}"
            self.log.error(msg)
            return msg

    def update_subcategory(self, search_subcat, category_option=None, sub_category_name=None):
        try:
            self.open_sub_category_master()
            if self.verify_value_on_table(search_subcat):
                self.log.info(f"{search_subcat} Sub category exists.")
                self.click_on(commonelements.edit_icon)
                if category_option is not None:
                    self.select_dropdown_option(subcategory_elements.subCat_category_dd, category_option)
                else:
                    self.log.warning("Category not provided, sub category unable to add sub category in master.")
                if sub_category_name is not None:
                    self.enter_value(subcategory_elements.subCat_input, sub_category_name)
                else:
                    self.log.warning("Sub category value is not provided, so unable to add sub category in master.")
                self.click_on(commonelements.update_button)
                return "updated"
            else:
                self.click_on(subcategory_elements.add_sub_category_btn)
                if category_option is not None:
                    self.select_dropdown_option(subcategory_elements.subCat_category_dd, category_option)
                if sub_category_name is not None:
                    self.enter_value(subcategory_elements.subCat_input, sub_category_name)
                self.click_on(commonelements.modal_save_button)
                return "added"
        except (TimeoutException, StaleElementReferenceException,
                ElementNotInteractableException, NoSuchElementException) as e:
            msg = f"error: {type(e).__name__} in update_project: {e}"
            self.log.error(msg)
            return msg

    def delete_subcategory(self, sub_category_name, category_option="Demo category"):
        try:
            self.open_sub_category_master()
            if self.verify_value_on_table(sub_category_name):
                self.log.info(f"{sub_category_name} Sub category exists.")
                self.click_on(commonelements.delete_icon)
                self.click_on(commonelements.delete_button)
                return "deleted"
            else:
                self.click_on(subcategory_elements.add_sub_category_btn)
                if category_option is not None:
                    self.select_dropdown_option(subcategory_elements.subCat_category_dd, category_option)
                else:
                    self.log.warning("Category not provided, sub category unable to add sub category in master.")
                if sub_category_name is not None:
                    self.enter_value(subcategory_elements.subCat_input, sub_category_name)
                else:
                    self.log.warning("Sub category value is not provided, so unable to add sub category in master.")
                self.click_on(commonelements.modal_save_button)
                self.click_on(commonelements.toaster)
                self.search(sub_category_name)
                self.click_on(commonelements.delete_icon)
                self.click_on(commonelements.delete_button)
                return "removed"
        except (TimeoutException, StaleElementReferenceException,
                ElementNotInteractableException, NoSuchElementException) as e:
            msg = f"error: {type(e).__name__} in update_project: {e}"
            self.log.error(msg)
            return msg