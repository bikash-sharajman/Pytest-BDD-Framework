from selenium.webdriver.common.by import By


class sub_category:
    add_sub_category_btn = By.XPATH, "//p-button[@label='Add Sub Category']//button//span[2]"
    subCat_category_dd = By.XPATH, "//p-select[@id='catType']//div//chevrondownicon"
    subCat_input = By.XPATH, "//input[@formcontrolname='subCat']"
    subCat_validation_message = By.XPATH, "//p-floatlabel//div[@role='alert']//span[1]"
    subCat_dropdown_option = By.XPATH, "//p-selectitem//li//span[text()='{option}']"
    view_subcat_modal = By.XPATH, "//p-dialog//span[text()='Sub Category']"
    category_field_value_required_message = By.XPATH, "//p-message//div[@role='alert']//div//span[1]"
    
subcat = sub_category()

