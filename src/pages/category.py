from src.pages.base_file import BasePage
from src.locators.common_locators import commonelements
from src.locators.category_mstr_locators import category
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.keys import Keys



class CategoryPage(BasePage):
    def __init__(self, driver, wait):
        super().__init__(driver, wait)
        
    def open_category_master(self):
        url = self.driver.current_url
        if "category-master" not in url.lower():
            self.click_on(commonelements.side_bar)
            self.redirect_to(commonelements.master_menu, commonelements.category_master)
            self.wait.until(ec.url_contains("category-master"))
        # self.click_on(commonelements.dashboard_menu)
        # self.redirect_to(commonelements.master_menu, commonelements.category_master)
        # self.wait.until(ec.url_contains("category-master"))
        
    def add_new_category(self, category_name:str):
        self.open_category_master()
        self.click_on(category.add_category_btn)
        self.enter_value(category.category_input, category_name)
        self.click_on(commonelements.modal_save_button)
    
    def search_category(self, category_name:str):
        self.search(category_name)
        search_box = self.wait.until(ec.element_to_be_clickable(commonelements.search_bar))
        search_box.send_keys(Keys.ENTER)
        
    def update_category(self, category_name:str, updated_cat:str):
        self.open_category_master()
        self.search_category(category_name)
        self.click_on(commonelements.edit_icon)
        self.enter_value(category.category_input, updated_cat)
        self.click_on(commonelements.update_button)
    
    def delete_category(self, category_name:str):
        self.open_category_master()
        self.search_category(category_name)
        self.click_on(commonelements.delete_icon)
        self.click_on(commonelements.delete_button)
    

        
    