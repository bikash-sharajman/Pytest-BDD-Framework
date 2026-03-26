from selenium.webdriver.common.by import By

class Model:
    add_model = By.XPATH, "//div[@ngbtooltip='Add Model']"
    model_make_dd = By.XPATH, "//select[@formcontrolname='make_id']"
    model_category_dd = By.XPATH, "//select[@formcontrolname='category_id']"
    model_sub_category_dd = By.XPATH, "//select[@formcontrolname='sub_category_id']"
    model_input = By.XPATH, "//input[@formcontrolname='model_name']"
    
model = Model()