import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import (
    ElementClickInterceptedException,
    StaleElementReferenceException,
    TimeoutException,
    ElementNotInteractableException,
    NoSuchElementException
)

from src.locators.common_locators import commonelements
from src.utils.logger import get_logger

class BasePage:
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait
        self.actions = ActionChains(driver)
        self.log = get_logger()

    
    def click_on(self, locator):
        try:
            element = self.wait.until(ec.element_to_be_clickable(locator))
            element.click()
        except (ElementClickInterceptedException, StaleElementReferenceException):
            self.driver.execute_script("arguments[0].click();", element)
        except TimeoutException:
            raise Exception(f"Element not clickable: {locator}")
        

    def hover_on_logo(self):
        logo_el = self.wait.until(ec.presence_of_element_located(commonelements.logo))
        self.actions.move_to_element(logo_el).perform()

    def enter_value(self, locator, value:str):
        try:
            element = self.wait.until(ec.element_to_be_clickable(locator))
            element.clear()
            element.send_keys(value)
        except StaleElementReferenceException:
            element = self.wait.until(ec.element_to_be_clickable(locator))
            element.clear()
            element.send_keys(value)
        except TimeoutException:
            raise Exception(f"Unable to enter value in: {locator}")


    def navigate_to(self, locator):
        self.wait.until(ec.element_to_be_clickable(locator)).click()

    def redirect_to(self, locator1, locator2):
        self.wait.until(ec.element_to_be_clickable(locator1)).click()
        self.wait.until(ec.element_to_be_clickable(locator2)).click()
        # self.hover_on_logo()

    
    def search(self, element: str):
        try:
            item = self.wait.until(ec.presence_of_element_located(commonelements.logo))
            self.actions.move_to_element(item).perform()
            search = self.wait.until(ec.element_to_be_clickable(commonelements.search_bar))
            search.clear()
            search.send_keys(element)
            time.sleep(0.5)
            self.log.info(f"Searching for {element}")
        except TimeoutException as e:
            raise self.log.error(f"{element} not found in search result.{e}")
    

    def verify_value_on_table(self, element_name: str):
        try:
            self.log.info(f"Validating the {element_name} in list table.")
            self.search(element_name)
            time.sleep(1)
            elements = self.driver.find_elements\
                (By.XPATH, f"//tbody[@class='p-datatable-tbody']//tr/td[2]//ngb-highlight[normalize-space()='{element_name}']")
            # self.log.info(f"Elements found count: {len(elements)}")

            if len(elements) > 0:
                self.log.info(f"{element_name} exists in table")
                return True
            else:
                self.log.warning(f"{element_name} NOT found in table")
                return False
        except Exception as e:
            self.log.error(f"{element_name} is not dispalyed on the list table. : {str(e)}")
            return "Element not found"

    # def verify_value_on_table(self, element_name: str):
    #     try:
    #         self.log.info(f"Validating the {element_name} in list table.")

    #         xpath = f"//tbody[@class='p-datatable-tbody']//tr/td[2]//ngb-highlight[normalize-space()='{element_name}']"
    #         self.log.info(f"XPath: {xpath}")

    #         # Print all matching elements count
    #         elements = self.driver.find_elements(By.XPATH, xpath)
    #         self.log.info(f"Elements found count: {len(elements)}")
    #         element = self.wait.until(
    #             ec.visibility_of_element_located((By.XPATH, xpath))
    #         )

    #         return element.text.strip() == element_name

    #     except Exception as e:
    #         self.log.error(f"Exception: {str(e)}")
    #         return False


    def get_toaster_message(self):
        try:
            toast = self.wait.until(ec.visibility_of_element_located(commonelements.toaster))
            # self.wait.until(lambda d: toast.text.strip() != "")
            return toast.text.strip()
        except TimeoutException:
            raise Exception("Toaster message not visible")

    def _click_with_fallback(self, element):
        try:
            element.click()
        except (ElementClickInterceptedException, StaleElementReferenceException):
            self.driver.execute_script("arguments[0].click();", element)
    
    def select_dropdown_option(self, locator, option):
        try:
            dropdown = self.wait.until(ec.element_to_be_clickable(locator))
            self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", dropdown)
            time.sleep(0.5)
            self._click_with_fallback(dropdown)

            option_locator = (By.XPATH, f"//p-selectitem//li//span[normalize-space()=\"{option}\"]",)
            option_element = self.wait.until(ec.visibility_of_element_located(option_locator))
            self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", option_element)
            time.sleep(0.5)
            self._click_with_fallback(option_element)
        except StaleElementReferenceException:

            dropdown = self.wait.until(ec.element_to_be_clickable(locator))
            dropdown.click()

            option = self.wait.until(ec.element_to_be_clickable(option_locator))
            option.click()

        except TimeoutException:
            raise Exception(f"Dropdown option '{option}' not found")
        
    
















