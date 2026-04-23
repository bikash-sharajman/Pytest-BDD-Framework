from selenium.webdriver.common.by import By


class WarehouseLocators:
    
    add_warehouse_btn = By.XPATH, "//span[text() ='Add Warehouse']"
    warehouse_type_dd = By.XPATH, "//p-select[@formcontrolname='warehouse_type']//div"
    warehouse_subtype_dd = By.XPATH, "//p-select[@formcontrolname='warehouse_sub_type']//div"
    warehouse_name = By.XPATH, "//input[@formcontrolname='warehouse_name']"
    warehouse_country_dd = By.XPATH, "//p-select[@formcontrolname='country_id']//div"
    warehouse_city = By.XPATH, "//input[@formcontrolname='city']"
    warehouse_incharge_dd = By.XPATH, "//p-select[@formcontrolname='incharge']//div"
    warehouse_latitude = By.XPATH, "//input[@formcontrolname='latitude']"
    warehouse_longitude = By.XPATH, "//input[@formcontrolname='longitude']"
    warehouse_address = By.XPATH, "//p-floatlabel//textarea[@formcontrolname='warehouse_address']"
    
    warehouse_save_btn = By.XPATH, "//button[text()=' Save ']"
    
    
    
    
    
warehouse_elements = WarehouseLocators()