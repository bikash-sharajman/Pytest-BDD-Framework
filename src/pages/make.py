from src.pages.base_file import BasePage
from src.locators.common_locators import commonelements
from src.locators.make_mstr_locators import makemodule
from selenium.webdriver.support import expected_conditions as ec


class MakePage(BasePage):

    def __init__(self, driver, wait):
        super().__init__(driver, wait)

    def open_make_master(self):
        url = self.driver.current_url
        if "make" not in url.lower():
            self.click_on(commonelements.side_bar)
            self.redirect_to(commonelements.master_menu, commonelements.make_master)
            self.wait.until(ec.url_contains("make"))

    def create_new_make(self, make):
        self.open_make_master()
        self.click_on(makemodule.add_make)
        self.enter_value(makemodule.make_input, make)
        self.click_on(commonelements.modal_save_button)

    def update_make(self, make_name, updated_make):
        self.open_make_master()
        self.search_make(make_name)
        self.click_on(commonelements.edit_icon)
        self.enter_value(makemodule.make_input, updated_make)
        self.click_on(commonelements.update_button)

    def search_make(self, make_name):
        self.search(make_name)

    def delete_make(self, make_name):
        self.open_make_master()
        self.search(make_name)
        self.click_on(commonelements.delete_icon)
        self.click_on(commonelements.delete_button)

