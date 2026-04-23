from src.pages.base_file import BasePage
from src.locators.common_locators import commonelements
from src.locators.asset_page_locators import asset_elements
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import (TimeoutException,
        StaleElementReferenceException, ElementNotInteractableException,
        NoSuchElementException)

from src.utils.screenshot import take_screenshot



class AssetModulePage(BasePage):
    def __init__(self, driver, wait):
        super().__init__(driver, wait)
        
    def asset_module(self):
        try:
            url = self.driver.current_url
            if "asset" not in url.lower():
                self.click_on(commonelements.overview_dashboard)
                self.redirect_to_asset_module(commonelements.asset_list)
                self.wait.until(ec.url_contains("asset"))
                self.log.info("User is redirected to asset module.")
            else:
                self.log.info("User is at asset module.")
        except TimeoutException as e:
            print(f"TimeoutException in asset_list: {e}")