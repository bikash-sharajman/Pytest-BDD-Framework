from selenium.webdriver.common.by import By
import os




class AssetModule:
    
    file1 = os.path.abspath(r"C:\Users\SHARAJMAN\Downloads\4.png")
    
    
    
    add_asset_btn = By.XPATH, "//span[normalize-space()='Add Assets']"
    add_asset_life_cycle_btn = By.XPATH, "//p-button[normalize-space()='Add Lifecycle Item']"
    # move_to_asset_detail_page_of = By.XPATH, f"//tbody//tr//td[normalize-space()='{asset_name}']"
    asset_name = By.XPATH, "//input[@formcontrolname='asset_name']"
    asset_category_dd = By.XPATH, "//p-select[@formcontrolname='asset_category_id']//div"
    asset_type_dd = By.XPATH, "//p-select[@formcontrolname='asset_type_id']//div"
    asset_status_dd = By.XPATH, "//p-select[@formcontrolname='status']//div"
    asset_critical_dd = By.XPATH, "//p-select[@formcontrolname='criticality']//div"
    asset_description = By.XPATH, "//textarea[@formcontrolname='description']"
    asset_serial_number = By.XPATH, "//input[@formcontrolname='serial_number']"
    asset_part_number = By.XPATH, "//input[@formcontrolname='part_number']"
    asset_cost_center = By.XPATH, "//input[@formcontrolname='cost_center']"
    asset_supplier = By.XPATH, "//input[@formcontrolname='supplier']"
    asset_save_btn = By.XPATH, "//button//span[normalize-space()='Save Asset']"
    asset_update_btn = By.XPATH, "//button//span[normalize-space()='Update Asset']"
    
    
    asset_manufacturer_dd = By.XPATH, "//p-select[@formcontrolname='manufacturer']//div"
    asset_model_dd = By.XPATH, "//p-select[@formcontrolname='model']//div"
    asset_ac_capacity = By.XPATH, "//input[@formcontrolname='ac_capacity']"
    asset_dc_capacity = By.XPATH, "//input[@formcontrolname='dc_capacity']"
    asset_voltage = By.XPATH, "//input[@formcontrolname='voltage']"
    asset_current = By.XPATH, "//input[@formcontrolname='current']"
    asset_power = By.XPATH, "//input[@formcontrolname='power']"
    asset_efficiency = By.XPATH, "//input[@formcontrolname='efficiency']"
    asset_operating_temp = By.XPATH, "//input[@formcontrolname='operating_tem']"
    asset_ip_rating = By.XPATH, "//input[@formcontrolname='ip_rating']"
    asset_rated_power = By.XPATH, "//input[@formcontrolname='rated_power']"
    
    
    asset_lifecycle_type_dd = By.XPATH, "//p-select[@formcontrolname='type']//div"   
    asset_lifecycle_status_dd = By.XPATH, "//p-select[@formcontrolname='status']//div"   
    asset_lifecycle_name = By.XPATH, "//input[@formcontrolname='name']"
    asset_lifecycle_provider = By.XPATH, "//input[@formcontrolname='provider']"
    asset_lifecycle_reminder = By.XPATH, "//input[@id='reminder']"
    asset_lifecycle_cost = By.XPATH, "//input[@id='cost']"
    asset_lifecycle_frequency_dd = By.XPATH, "//p-select[@formcontrolname='frequency']//div"
    asset_lifecycle_document_upload = By.XPATH, "//p-button//span[normalize-space()='Choose Document']"
    asset_document_upload = By.XPATH, "//span[normalize-space()='Upload']"
    
    asset_date_picker_next_month_arrow = By.XPATH, "//button[@aria-label='Next Month']"
    asset_date_picker_previous_month_arrow = By.XPATH, "//button[@aria-label='Previous Month']"
    asset_date_picker_month_selection_btn = By.XPATH, "//button[@aria-label='Choose Month']"
    asset_date_picker_year_selection_btn = By.XPATH, "//button[@aria-label='Choose Year']"
    asset_lifecycle_start_date_datepicker = By.XPATH, "//button[@aria-label='Choose Date']/ancestor::p-floatlabel//input[@id='startDate']"
    asset_lifecycle_end_date_datepicker = By.XPATH, "//button[@aria-label='Choose Date']/ancestor::p-floatlabel//input[@id='endDate']"

    
    
    
    
    

asset_elements = AssetModule()

