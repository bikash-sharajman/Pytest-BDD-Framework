import time
import inspect
from src.initialization.config_reader import confr
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
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

    # base_url = confr.get_baseurl()
    # url = f"{base_url}/login"
    # def open_overview_dashboard(self, driver, wait):
    #     try:

    #         # 🔹 Wait for URL to change (either dashboard or login)
    #         wait.until(lambda d: "solar-plant-dashboard" in d.current_url.lower()
    #                             or "login" in d.current_url.lower()
    #                             or "no-privilege" in d.current_url.lower())

    #         url = driver.current_url.lower()
    #         if "solar-plant-dashboard" in url:
    #             self.log.info("User is already on overview dashboard page.")
    #             return True

    #         elif "login" in url:
    #             self.log.info("Perform login and redirect to overview page.")
    #             self.login_page.login(confr.email, confr.password)
    #             wait.until(ec.url_contains("solar-plant-dashboard"))
    #             self.log.info("Login successful, redirected on dashboard.")
    #             return True

    #         elif "no-privilege" in url:
    #             self.log.error("No privilege to access overview dashboard.")
    #             return False

    #         else:
    #             self.log.error(f"Unexpected URL: {url}")
    #             return False

    #     except TimeoutException as e:
    #         self.log.error(f"Timeout in open_overview_dashboard: {str(e)}")
    #         return False
        
    
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
            time.sleep(0.5)
            element.clear()
            element.send_keys(value)
        except StaleElementReferenceException:
            element = self.wait.until(ec.element_to_be_clickable(locator))
            element.clear()
            element.send_keys(value)
        except TimeoutException:
            raise Exception(f"Timeout : Unable to enter value in: {locator}")

    def enter_date(self, locator, value: str):
        try:
            element = self.wait.until(ec.presence_of_element_located(locator))
            self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
            time.sleep(0.5)

            if element.tag_name.lower() == "input":
                input_element = element
            else:
                input_element = element.find_element(By.XPATH, ".//input")

            self.driver.execute_script(
                """
                const input = arguments[0];
                const value = arguments[1];
                input.removeAttribute('readonly');
                input.focus();
                input.value = '';
                input.dispatchEvent(new Event('input', { bubbles: true }));
                input.value = value;
                input.dispatchEvent(new Event('input', { bubbles: true }));
                input.dispatchEvent(new Event('change', { bubbles: true }));
                input.dispatchEvent(new Event('blur', { bubbles: true }));
                """,
                input_element,
                str(value),
            )

            try:
                input_element.send_keys(Keys.TAB)
            except Exception:
                pass

        except NoSuchElementException:
            raise Exception(f"Date input not found inside locator: {locator}")
        except TimeoutException:
            raise Exception(f"Unable to enter date in: {locator}")
        

    def navigate_to(self, locator):
        self.wait.until(ec.element_to_be_clickable(locator)).click()
          

    def redirect_to_master_module(self, locator):
        try:
            self.wait.until(ec.element_to_be_clickable(commonelements.master_menu)).click()
        except TimeoutException:
            self.log.warning("You are not authorized to access the master module.")
            raise TimeoutException("You are not authorized to access the master module.")
        try:
            self.wait.until(ec.element_to_be_clickable(locator)).click()
        except TimeoutException:
            function_name = inspect.stack()[1].function
            message = f"You are not authorized to access {function_name}"
            self.log.warning(message)
            raise TimeoutException(message)
        
    def redirect_to_management_module(self, locator):
        try:
            self.wait.until(ec.element_to_be_clickable(commonelements.management_menu)).click()
        except TimeoutException:
            self.log.warning("You are not authorized to access the management module.")
            raise TimeoutException("You are not authorized to access the management module.")
        try:
            self.wait.until(ec.element_to_be_clickable(locator)).click()
        except TimeoutException:
            function_name = inspect.stack()[1].function
            message = f"You are not authorized to access {function_name}"
            self.log.warning(message)
            raise TimeoutException(message)
        
    def redirect_to_asset_module(self, locator):
        try:
            self.wait.until(ec.element_to_be_clickable(commonelements.asset_menu)).click()
        except TimeoutException:
            self.log.warning("You are not authorized to access the asset module.")
            raise TimeoutException("You are not authorized to access the asset module.")
        try:
            self.wait.until(ec.element_to_be_clickable(locator)).click()
        except TimeoutException:
            function_name = inspect.stack()[1].function
            message = f"You are not authorized to access {function_name}"
            self.log.warning(message)
            raise TimeoutException(message)
        

    
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
    
    def verify_value_on_table(self, element_name: str) -> bool:
        try:
            self.log.info(f"Validating '{element_name}' in table.")
            self.search(element_name)
            locator = By.XPATH, f"//tbody[@class='p-datatable-tbody']//tr//td//ngb-highlight//span[normalize-space()='{element_name}']"

            try:
                self.wait.until(ec.presence_of_element_located(locator))
            except TimeoutException:
                self.log.warning(f"'{element_name}' NOT found in table.")
                return False
            
            elements = self.driver.find_elements(*locator)

            if elements:
                self.log.info(f"'{element_name}' exists in table.")
                return True
            else:
                self.log.warning(f"'{element_name}' NOT found in table.")
                return False

        except (StaleElementReferenceException, Exception) as e:
            self.log.error(f"Error while validating '{element_name}': {str(e)}")
            return False
    
    def get_toaster_message(self):
        try:
            toast = self.wait.until(ec.visibility_of_element_located(commonelements.toaster))
            # self.wait.until(lambda d: toast.text.strip() != "")
            message = toast.text.strip()
            self.log.info(f"Toaster message received: '{message}'")
            return message
        except TimeoutException:
            raise Exception("Toaster message not visible")

    def _click_with_fallback(self, element):
        try:
            element.click()
        except (ElementClickInterceptedException, StaleElementReferenceException):
            self.driver.execute_script("arguments[0].click();", element)
            self.log.info("JS click executed successfully")
    
    def select_dropdown_option(self, locator, option):
        try:
            dropdown = self.wait.until(ec.element_to_be_clickable(locator))
            self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", dropdown)
            time.sleep(0.5)
            self._click_with_fallback(dropdown)
            self.log.info("Dropdown is clicked.")

            option_locator = (By.XPATH, f"//p-selectitem//li//span[normalize-space()=\"{option}\"]",)
            option_element = self.wait.until(ec.visibility_of_element_located(option_locator))
            self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", option_element)
            time.sleep(0.5)
            self._click_with_fallback(option_element)
            self.log.info(f"Dropdown option '{option}' selected successfully")
        except StaleElementReferenceException:

            dropdown = self.wait.until(ec.element_to_be_clickable(locator))
            dropdown.click()
            self.log.info("Dropdown is clicked again")

            option = self.wait.until(ec.element_to_be_clickable(option_locator))
            option.click()
            self.log.info("Dropdown option is clicked after retry.")

        except (TimeoutException, NoSuchElementException) as e:
            self.log.error(f"Dropdown option - {option} not found. Exception - {e}")
        

        


    
        
    
















