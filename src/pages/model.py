from src.pages.base_file import BasePage
from src.locators.common_locators import commonelements
from src.locators.model_mstr_locators import modelelements
from selenium.webdriver.support import expected_conditions as ec



class Model(BasePage):
    def __init__(self, driver, wait):
        super().__init__(driver, wait)
    
    def open_model_master(self):
        url = self.driver.current_url
        if "model" not in url.lower():
            self.click_on_(commonelements.side_bar)
            self.redirect_to(commonelements.master_menu, commonelements.model_master)
            self.wait.until(ec.url_contains("model"))
            
    def add_new_model(self, model_name, category_name, make_name, sub_category_name):
        self.open_model_master()
        self.click_on(modelelements.add_model_btn)
        self.select_dropdown_option(modelelements.model_make_dd, make_name)
        self.select_dropdown_option(modelelements.model_category_dd, category_name)
        self.select_dropdown_option(modelelements.model_sub_category_dd, sub_category_name)
        self.enter_value(modelelements.model_input, model_name)
        self.click_on(commonelements.modal_save_button)
        
    def edit_modal(self):
        pass
        
    
        
            
    
        


