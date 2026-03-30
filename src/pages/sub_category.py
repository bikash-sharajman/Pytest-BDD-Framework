from src.pages.base_file import BasePage
from src.locators.common_locators import commonelements
from src.locators.subcat_mstr_locators import subcategory_elements
from selenium.webdriver.support import expected_conditions as ec



class SubCategory(BasePage):
    def __init__(self, driver, wait):
        super().__init__(driver, wait)
        
    def open_sub_category_master(self):
        url = self.driver.current_url
        if "subcategory-master" not in url.lower:
            self.click_on_(commonelements.side_bar)
            self.redirect_to(commonelements.master_menu, commonelements.sub_category_master)
            self.wait.until(ec.url_contains("subcategory-master"))
    
    def add_new_subcategory(self, category_option, sub_category_name):
        self.open_sub_category_master()
        self.click_on(subcategory_elements.add_sub_category_btn)
        self.select_dropdown_option(subcategory_elements.subCat_category_dd, category_option)
        self.enter_value(subcategory_elements.subCat_input, sub_category_name)
        self.click_on(commonelements.modal_save_button)
        
    def edit_sub_category(self, search_subcat, category_option=None, sub_category_name=None):
        self.open_sub_category_master()
        self.search(search_subcat)
        self.click_on(commonelements.edit_icon)
        if category_option is not None:
            self.select_dropdown_option(subcategory_elements.subCat_category_dd, category_option)
        if sub_category_name is not None:
            self.enter_value(subcategory_elements.subCat_input, sub_category_name)
        self.click_on(commonelements.update_button)
        
    def delete_subcategory(self, search_subcat):
        try:
            self.open_sub_category_master()
            self.search(search_subcat)        
            self.click_on(commonelements.delete_icon)
            self.click_on(commonelements.delete_button)
        except Exception as err:
            print(err,'Error')
            

        

        
        
            