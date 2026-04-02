from selenium.webdriver.common.by import  By




class project_management:
    
    
    add_project_btn = By.XPATH, "//p-button[@label='Add Project']//button//span[2]"
    export_btn = By.XPATH, "//p-button[@label='Export']//button//span[2]"
    
    #tabs
    basic_details_tab = By.XPATH, "//p-tab[text()='Basic Details']"
    unit_details_tab = By.XPATH, "//p-tab[text()='Unit Details']"
    data_logger_tab = By.XPATH, "//p-tab[text()='Data Logger Details']"
    asset_details_tab = By.XPATH, "//p-tab[text()='Asset Details']"
    data_aquisition_tab = By.XPATH, "//p-tab[text()='Data Acquisition']"
    contact_details_tab = By.XPATH, "//p-tab[text()='Contact Details']"
    forcast_information_tab = By.XPATH, "//p-tab[text()='Forecast Information']"
    site_person_tab = By.XPATH, "//p-tab[text()='Site Person Details']"
    vendor_details_tab = By.XPATH, "//p-tab[text()='Vendor Details']"
    document_tab = By.XPATH, "//p-tab[text()='Documents']"
    anomaly_tab = By.XPATH, "//p-tab[text()='Anomaly Detection']"
            
    

    #basic details tab
    pm_input_error_message = By.XPATH, "//input[@id='tilt_azimuth'] /ancestor::p-floatlabel //div[@role='alert']//span"
    project_code = By.CSS_SELECTOR, "[id='plant_code']"
    project_name = By.CSS_SELECTOR, "[id='plant_name']"
    short_name = By.CSS_SELECTOR, "[id='short_name']"
    site_address = By.CSS_SELECTOR, "[id='site_address']"
    latitude = By.CSS_SELECTOR, "[id='latitude']"
    longitude = By.CSS_SELECTOR, "[id='longitude']"
    tilt_azimuth = By.CSS_SELECTOR, "[id='tilt_azimuth']"
    dc_capacity = By.CSS_SELECTOR, "[id='dc_capacity']"
    ac_capacity = By.CSS_SELECTOR, "[id='ac_capacity']"
    tarrif = By.CSS_SELECTOR, "[id='tariff']"
    start_time = By.CSS_SELECTOR, "[id='start_time']"
    end_time = By.CSS_SELECTOR, "[id='end_time']"
    display_order = By.CSS_SELECTOR, "[id='display_order']"
    wms_installed_checkbox = By.XPATH, "//input[@name='is_wms_installed']"
    smb_installed_checkbox = By.XPATH, "//input[@name='is_smb_installed']"
    
    state_dd = By.XPATH, "//p-floatlabel//p-select[@name='state_id']//div"
    cluster_dd = By.XPATH, "//p-floatlabel//p-select[@name='cluster_id']//div"
    billing_dd = By.XPATH, "//p-floatlabel//p-select[@name='company_id']//div"
    project_type_dd = By.XPATH, "//p-floatlabel//p-select[@name='domain']//div"
    sub_type_dd = By.XPATH, "//p-floatlabel//p-select[@name='sub_domain']//div"
    technology_type_dd = By.XPATH, "//p-floatlabel//p-select[@name='technology_type']//div"
    installation_type_dd = By.XPATH, "//p-floatlabel//p-select[@name='installation_type']"
    mounting_type_dd = By.XPATH, "//p-floatlabel//p-select[@name='mounting_type']//div"
    warehouse_dd = By.XPATH, "//p-floatlabel//p-select[@name='warehouse_id']//div"
    data_frequency_dd = By.XPATH, "//p-floatlabel//p-select[@id='data_frequency']"
    commission_date_picker = By.XPATH, "//*[@id='commissioning_date']"
    
    
    #site person tab
    add_person_button = By.XPATH, "//p-button//span[normalize-space()='Add Person']"
    site_person_tab_search_bar = By.XPATH, "//p-floatlabel//input[@name='undefined']"
    role_type_dd = By.XPATH, "//p-floatlabel//p-select[@id='user_role']"
    site_tech_option = By.XPATH, "//p-selectitem//li[@aria-label='Site Tech']"
    
    
    #anomaly detection
    add_anomaly_button = By.XPATH, "//button//span[text()='Add Anomaly']"
    

    









pm = project_management()


