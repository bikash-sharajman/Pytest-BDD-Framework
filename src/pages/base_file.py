import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import (
    ElementClickInterceptedException,
    StaleElementReferenceException,
    TimeoutException,
)

from src.locators.common_locators import commonelements

class BasePage:
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait
        self.actions = ActionChains(driver)

    
    def click_on(self, locator):
        self.wait.until(ec.element_to_be_clickable(locator)).click()
        

    def hover_on_logo(self):
        logo_el = self.wait.until(ec.presence_of_element_located(commonelements.logo))
        self.actions.move_to_element(logo_el).perform()

    def enter_value(self, locator, value):
        element = self.wait.until(ec.element_to_be_clickable(locator))
        element.clear()
        element.send_keys(value)

    def update_value(self, locator, value):
        self.enter_value(locator, value)


    def navigate_to(self, locator):
        self.wait.until(ec.element_to_be_clickable(locator)).click()

    def redirect_to(self, locator1, locator2):
        self.wait.until(ec.element_to_be_clickable(locator1)).click()
        self.wait.until(ec.element_to_be_clickable(locator2)).click()
        # self.hover_on_logo()

    
    def search(self, element: str):
        item = self.wait.until(ec.presence_of_element_located(commonelements.logo))
        self.actions.move_to_element(item).perform()
        search = self.wait.until(ec.element_to_be_clickable(commonelements.search_bar))
        search.clear()
        search.send_keys(element)
    

    def verify_value_on_table(self, element_name: str):
        item =  self.wait.until(ec.visibility_of_element_located
            (commonelements.element_on_table(element_name)))
        return item

    def get_toaster_message(self):
        toast = self.wait.until(ec.element_to_be_clickable(commonelements.toaster))
        toaster = toast.text.strip()

        return toaster

    def _click_with_fallback(self, element):
        try:
            element.click()
        except (ElementClickInterceptedException, StaleElementReferenceException):
            self.driver.execute_script("arguments[0].click();", element)
    
    def select_dropdown_option(self, locator, option):
        dropdown = self.wait.until(ec.element_to_be_clickable(locator))
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", dropdown)
        time.sleep(0.5)
        self._click_with_fallback(dropdown)

        option_locator = (
            By.XPATH,
            f"//p-selectitem//li//span[normalize-space()=\"{option}\"]",
        )
        option_element = self.wait.until(ec.visibility_of_element_located(option_locator))
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", option_element)
        time.sleep(0.5)
        self._click_with_fallback(option_element)
        
    
















