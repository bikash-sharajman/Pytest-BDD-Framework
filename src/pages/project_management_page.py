

from src.pages.base_file import BasePage
from src.locators.project_management_locators import pm

from selenium.webdriver.support import expected_conditions as ec


class ProjectManagement(BasePage):
    
    def __init__(self, driver, wait):
        super().__init__(driver, wait)
        
    def click_on_add_project_btn(self):
        self.wait.until(ec.element_to_be_clickable(pm.add_project_btn)).click()
        
    def enter_project_name(self, value):
        self.enter_value(pm.project_name, value)
    
    def enter_project_code(self, value):
        self.enter_value(pm.project_code, value)
    
    def enter_project_short_name(self, value):
        self.enter_value(pm.short_name, value)

    def enter_site_address(self, value):
        self.enter_value(pm.site_address, value)
    
    def enter_project_latitude(self, value):
        self.enter_value(pm.latitude, value)
        
    def enter_project_longitude(self, value):
        self.enter_value(pm.longitude, value)
    
    def enter_tilt_angle(self, value):
        self.enter_value(pm.tilt_azimuth, value)
        
    def enter_dc_capacity(self, value):
        self.enter_value(pm.dc_capacity, value)
    
    def enter_ac_capacity(self, value):
        self.enter_value(pm.ac_capacity, value)
        
    def enter_tarrif(self, value):
        self.enter_value(pm.tarrif, value)

    def enter_start_time(self, value):
        self.enter_value(pm.start_time, value)
        
    def enter_end_time(self, value):
        self.enter_value(pm.end_time, value)
        
    def select_from_dropdown(self, locator, option):
        self.select_dropdown_option(locator, option)
    
    
    
    
        