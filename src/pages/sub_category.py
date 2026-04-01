from src.locators.base_file import BasePage
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
                self.click_on(commonelements.side_bar)
                self.redirect_to(commonelements.master_menu, commonelements.sub_category_master)
                self.wait.until(ec.url_contains("subcategory"))
                self.log.info("User is redirected to subcategory master page.")
            else:
                self.log.info("User is at subcategory module.")
        except TimeoutException as e:
            print(f"TimeoutException in open_sub_category_master: {e}")
        except StaleElementReferenceException as e:
            print(f"StaleElementReferenceException in open_sub_category_master: {e}")
        except ElementNotInteractableException as e:
            print(f"ElementNotInteractableException in open_sub_category_master: {e}")
        except NoSuchElementException as e:
            print(f"NoSuchElementException in open_sub_category_master: {e}")

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
        except TimeoutException as e:
            msg = f"TimeoutException in create_new_subcategory: {e}"
            print(msg)
            return msg
        except StaleElementReferenceException as e:
            msg = f"StaleElementReferenceException in create_new_subcategory: {e}"
            print(msg)
            return msg
        except ElementNotInteractableException as e:
            msg = f"ElementNotInteractableException in create_new_subcategory: {e}"
            print(msg)
            return msg
        except NoSuchElementException as e:
            msg = f"NoSuchElementException in create_new_subcategory: {e}"
            print(msg)
            return msg

    def update_subcategory(self, search_subcat, category_option=None, sub_category_name=None):
        try:
            self.open_sub_category_master()
            self.click_on(commonelements.edit_icon)
            if category_option is not None:
                self.select_dropdown_option(subcategory_elements.subCat_category_dd, category_option)
            if sub_category_name is not None:
                self.enter_value(subcategory_elements.subCat_input, sub_category_name)
            self.click_on(commonelements.update_button)
            return f"{search_subcat} updated."
        except TimeoutException as e:
            msg = f"TimeoutException in update_subcategory: {e}"
            print(msg)
            return msg
        except StaleElementReferenceException as e:
            msg = f"StaleElementReferenceException in update_subcategory: {e}"
            print(msg)
            return msg
        except ElementNotInteractableException as e:
            msg = f"ElementNotInteractableException in update_subcategory: {e}"
            print(msg)
            return msg
        except NoSuchElementException as e:
            msg = f"NoSuchElementException in update_subcategory: {e}"
            print(msg)
            return msg

    # def search_subcategory(self, sub_category_name):
    #     try:
    #         self.search(sub_category_name)
    #     except TimeoutException as e:
    #         print(f"TimeoutException in search_subcategory: {e}")
    #     except StaleElementReferenceException as e:
    #         print(f"StaleElementReferenceException in search_subcategory: {e}")
    #     except ElementNotInteractableException as e:
    #         print(f"ElementNotInteractableException in search_subcategory: {e}")
    #     except NoSuchElementException as e:
    #         print(f"NoSuchElementException in search_subcategory: {e}")

    def delete_subcategory(self, sub_category_name):
        try:
            self.open_sub_category_master()
            self.search(sub_category_name)
            self.click_on(commonelements.delete_icon)
            self.click_on(commonelements.delete_button)
            return f"{sub_category_name} deleted."
        except TimeoutException as e:
            msg = f"TimeoutException in delete_subcategory: {e}"
            print(msg)
            return msg
        except StaleElementReferenceException as e:
            msg = f"StaleElementReferenceException in delete_subcategory: {e}"
            print(msg)
            return msg
        except ElementNotInteractableException as e:
            msg = f"ElementNotInteractableException in delete_subcategory: {e}"
            print(msg)
            return msg
        except NoSuchElementException as e:
            msg = f"NoSuchElementException in delete_subcategory: {e}"
            print(msg)
            return msg