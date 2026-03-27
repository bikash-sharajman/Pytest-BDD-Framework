from src.pages.base_file import BasePage
from src.locators.common_locators import commonelements
from selenium.webdriver.support import expected_conditions as ec



class Model(BasePage):
    def __init__(self, driver, wait):
        super().__init__(driver, wait)
    
    def open_category_master(self):
        url = self.driver.current_url
        if "model" not in url.lower():
            self.click_on_(commonelements.side_bar)
            self.redirect_to(commonelements.master_menu, commonelements.model_master)
            self.wait.until(ec.url_contains("model"))
            
    
        


