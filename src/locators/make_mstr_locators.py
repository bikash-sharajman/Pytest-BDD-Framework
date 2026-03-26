from selenium.webdriver.common.by import By




class MakeModule:
    add_make = By.XPATH, "//p-button//span[text() = 'Add Make']"
    make_input = By.XPATH, "//input[@formcontrolname='make_name']"
    make_save_button = By.XPATH, "//button//span[2][text()=' Save']"
    view_make_modal = By.XPATH, "//p-dialog//span[text()='Make']"
    update_button = By.XPATH, "//span[text()=' Update']"
    # make_master_table = By.XPATH, "//table[@id='pn_id_1-table']"
    make_validation_message = By.XPATH, "//p-floatlabel//div[@role='alert']//span//span"


makemodule = MakeModule()