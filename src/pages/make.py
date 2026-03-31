from src.pages.base_file import BasePage
from src.locators.common_locators import commonelements
from src.locators.make_mstr_locators import makemodule
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import (TimeoutException,
        StaleElementReferenceException, ElementNotInteractableException,
        NoSuchElementException)


class MakePage(BasePage):

    def __init__(self, driver, wait):
        super().__init__(driver, wait)

    def open_make_master(self):
        try:
            url = self.driver.current_url
            if "make" not in url.lower():
                self.click_on(commonelements.side_bar)
                self.redirect_to(commonelements.master_menu, commonelements.make_master)
                self.wait.until(ec.url_contains("make"))
                self.log.info("User is redirected to make master page.")
        except TimeoutException as e:
            print(f"TimeoutException in open_make_master: {e}")
        except StaleElementReferenceException as e:
            print(f"StaleElementReferenceException in open_make_master: {e}")
        except ElementNotInteractableException as e:
            print(f"ElementNotInteractableException in open_make_master: {e}")
        except NoSuchElementException as e:
            print(f"NoSuchElementException in open_make_master: {e}")

    def create_new_make(self, make):
        try:
            self.open_make_master()
            # self.search(make)
            table_result = self.verify_value_on_table(make)
            if table_result:
                self.log.info("Make already exists.")
                return("Make already exists.")
            else:
                self.log.info(f"{make} not found, adding the new make {make}.")
                self.click_on(makemodule.add_make)
                self.enter_value(makemodule.make_input, make)
                self.click_on(commonelements.modal_save_button)
                self.log.info(f"{make} is sucessfully added into system.")
                toaster = self.get_toaster_message()
                assert "Data Saved Sucessfully" in toaster, f"Expected toaster not displayed, but got {toaster}"
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

    def update_make(self, make_name, updated_make):
        try:
            self.open_make_master()
            self.search(make_name)
            self.click_on(commonelements.edit_icon)
            self.enter_value(makemodule.make_input, updated_make)
            self.click_on(commonelements.update_button)
        except TimeoutException as e:
            print(f"TimeoutException in update_make: {e}")
        except StaleElementReferenceException as e:
            print(f"StaleElementReferenceException in update_make: {e}")
        except ElementNotInteractableException as e:
            print(f"ElementNotInteractableException in update_make: {e}")
        except NoSuchElementException as e:
            print(f"NoSuchElementException in update_make: {e}")

    # def search_make(self, make_name):
    #     try:
    #         self.search(make_name)
    #     except TimeoutException as e:
    #         print(f"TimeoutException in search_make: {e}")
    #     except StaleElementReferenceException as e:
    #         print(f"StaleElementReferenceException in search_make: {e}")
    #     except ElementNotInteractableException as e:
    #         print(f"ElementNotInteractableException in search_make: {e}")
    #     except NoSuchElementException as e:
    #         print(f"NoSuchElementException in search_make: {e}")

    def delete_make(self, make_name):
        try:
            self.open_make_master()
            self.search(make_name)
            self.click_on(commonelements.delete_icon)
            self.click_on(commonelements.delete_button)
        except TimeoutException as e:
            print(f"TimeoutException in delete_make: {e}")
        except StaleElementReferenceException as e:
            print(f"StaleElementReferenceException in delete_make: {e}")
        except ElementNotInteractableException as e:
            print(f"ElementNotInteractableException in delete_make: {e}")
        except NoSuchElementException as e:
            print(f"NoSuchElementException in delete_make: {e}")
