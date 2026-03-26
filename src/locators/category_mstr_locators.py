from selenium.webdriver.common.by import By

class categoryModule:
    add_category = By.XPATH, "//p-button//span[text() = 'Add Category']"
    category_input = By.XPATH, "//input[@formcontrolname='catType']"
    category_save_button = By.XPATH, "//button//span[2][text()=' Save']"
    view_category_modal = By.XPATH, "//p-dialog//span[text()='Add Category']"
    update_button = By.XPATH, "//span[text()=' Update']"
    category_master_table = By.XPATH, "//p-table//table[@id='pn_id_6-table']"


category = categoryModule()