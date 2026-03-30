from selenium.webdriver.common.by import By


class SubCategory:
    add_sub_category_btn = By.XPATH, "//p-button[@label='Add Sub Category']//button//span[2]"
    subCat_category_dd = By.XPATH, "//p-floatlabel//p-select[@formcontrolname='catType']//div"
    subCat_input = By.XPATH, "//input[@formcontrolname='subCat']"
    subCat_validation_message = By.XPATH, "//p-floatlabel//div[@role='alert']//span[1]"
    # subCat_dropdown_option = By.XPATH, "//p-selectitem//li//span[text()='{option}']"
    view_subcat_modal = By.XPATH, "//p-dialog//span[text()='Sub Category']"
    category_field_value_required_message = By.XPATH, "//label[@for='catType'] /ancestor::p-floatlabel//p-message//span[last()]"
    subcategory_field_error_message = By.XPATH, "//label[@for='subCat'] /ancestor::p-floatlabel//p-message//span[last()]"
    
subcategory_elements = SubCategory()

