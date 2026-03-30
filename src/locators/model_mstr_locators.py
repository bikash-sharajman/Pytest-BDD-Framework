from selenium.webdriver.common.by import By

class Model:
    add_model_btn = By.XPATH, "//p-button//span[text()='Add Model']"
    model_make_dd = By.XPATH, "//p-floatlabel//p-select[@formcontrolname='make_id']//div"
    model_category_dd = By.XPATH, "//p-floatlabel//p-select[@formcontrolname='category_id']//div"
    model_sub_category_dd = By.XPATH, "//p-floatlabel//p-select[@formcontrolname='sub_category_id']//div"
    model_input = By.XPATH, "//input[@formcontrolname='model_name']"
    modal_text = By.XPATH, "//div[@role='dialog']//div[2]/span"
    
modelelements = Model()