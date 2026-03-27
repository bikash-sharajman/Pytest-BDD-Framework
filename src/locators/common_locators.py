from selenium.webdriver.common.by import By


class CommonLocators:
    
    side_bar = By.XPATH, "//aside[@class='left-sidebar']"
    go_back_button = By.XPATH, "//span[text()='Go Back']"
    search_bar =By.XPATH, "//p-iconfield//input[@psize='small']"
    modal_cancel_button = By.XPATH, "//button//span[normalize-space()='Cancel']"
    modal_save_button = By.XPATH, "//button//span[2][normalize-space()='Save']"
    save_button = By.XPATH, "//button[text()='Save']"
    update_button = By.XPATH, "//button//span[2][text()=' Update']"
    view_icon = By.XPATH, "//tbody//p-button[@icon='pi pi-eye']"
    edit_icon = By.XPATH, "//tbody//p-button[@icon='pi pi-pencil']"
    delete_icon =By.XPATH, "//tbody//p-button[@icon='pi pi-trash']"
    confirm_delete_text = By.XPATH, "//span[text()='Confirm Delete']"
    delete_button = By.XPATH, "//p-button//span[text()='Delete']"
    yes_button = By.XPATH, "//button[text()='Yes']"
    toaster = By.XPATH, "//div[@id='toast-container']/div/div"
    logo = By.XPATH, "//app-vertical-navigation//ul[2]//li//a/img"
    element_on_table = By.XPATH, "//tbody[@class='p-datatable-tbody']//tr/td[2]//ngb-highlight"
    master_list_table = By.XPATH, "//p-table//table[contains(@class,'p-datatable')]"
    input_field_required_error_message = By.XPATH, "//p-message//div[@role='alert']//div//span"

    #locators of sidebar menu
    dashboard_menu = By.XPATH, "//i-feather[@class='icon-grid']"
    management_menu = By.XPATH, "//i-feather[@class='icon-people']"
    master_menu = By.XPATH, "//i-feather[@class='icon-settings']"
    ticket_menu = By.XPATH, "//i-feather[@class='fas fa-ticket-alt']"
    maintenance_menu = By.XPATH, "//i-feather[@class='icon-wrench']"
    asset_menu = By.XPATH, "//i-feather[@class='icon-support']"
    overview_dashboard = By.XPATH, "//i-feather[@class='icon-home']"

    #management menu
    user_management = By.XPATH, "//aside//span[ormalize-space()= 'User Management']"
    project_management = By.XPATH, "//a[@href='/plant-management']"
    vendor_management = By.XPATH, "//aside//span[ormalize-space()= 'Vendor Management']"
    team_management = By.XPATH, "//aside//span[ormalize-space()= 'Team Management']"
    invenvtory_management = By.XPATH, "//aside//span[ormalize-space()= 'Inventory Management']"

    #master menu
    make_master = By.XPATH, "//a[@href='/make']"
    warehouse_master = By.XPATH, "//a[@href='/warehouse']"
    activity_master = By.XPATH, "//a[@href='/activity-master']"
    incident_master = By.XPATH, "//aside//span[text()= 'Incident']"
    element_master = By.XPATH, "//aside//span[text()= 'Element']"
    company_master = By.XPATH, "//aside//span[text()= 'Company']"
    category_master = By.XPATH, "//aside//span[text()= 'Category']"
    cluster_master = By.XPATH, "//aside//span[text()= 'Cluster']"
    sub_category_master = By.XPATH, "//aside//span[text()= 'Sub Category']"
    item_master = By.XPATH, "//aside//span[text()= 'Items']"
    model_master = By.XPATH, "//aside//span[text()= 'Model']"
    alarm_master = By.XPATH, "//aside//span[text()= 'Alarm']"
    inventory_master = By.XPATH, "//aside//span[text()= 'Inventory']"

    #dashboard sub-menus
    inventory_dashboard = By.XPATH, "//aside//span[text()= 'Inverter Dashboard']"
    ws_dashboard = By.XPATH, "//aside//span[text()= 'WS Dashboard']"
    mfm_dashboard = By.XPATH, "//aside//span[text()= 'MFM Dashboard']"
    smb_dashboard = By.XPATH, "//aside//span[text()= 'SMB Dashboard']"
    trend_dashboard = By.XPATH, "//aside//span[text()= 'Trend Dashboard']"
    cmms_dashboard = By.XPATH, "//aside//span[text()= 'CMMS Dashboard']"
    inverter_list_view = By.XPATH, "//aside//span[text()= 'Inverter List View']"
    inverter_performance = By.XPATH, "//aside//span[text()= 'Inverter Performance']"
    inverter_dashboard = By.XPATH, "//aside//span[text()= 'Inverter Dashboard']"
    smb_details_dashboard = By.XPATH, "//aside//span[text()= 'SMB Details Dashboard']"
    manage_band = By.XPATH, "//aside//span[text()= 'Manage Band']"
    upload_dsm_schedule = By.XPATH, "//aside//span[text()= 'Upload Dsm Schedule']"
    string_dashboard = By.XPATH, "//aside//span[text()= 'String Dashboard']"

    notification_dashboard  = By.XPATH, "//aside//span[text()= 'Notification Dashboard']"
    ticket_dashboard = By.XPATH, "//aside//span[text()= 'Ticket Dashboard']"
    technician_dashboard = By.XPATH, "//aside//span[text()= 'Technician Dashboard']"
    alert_list = By.XPATH, "//aside//span[text()= 'Alert List']"

    scheduler = By.XPATH, "//aside//span[text()= 'Scheduler']"
    task_viewer = By.XPATH, "//aside//span[text()= 'Task Viewer']"
    maintenance_new = By.XPATH, "//aside//span[text()= 'Maintenance New']"

    asset_list = By.XPATH, "//aside//span[text()= 'Asset List']"
    asset_heirarchy = By.XPATH, "//aside//span[text()= 'Asset Hierarchy']"

    add_category = By.XPATH, "//div[@ngbtooltip='Add Category']"
    category_input = By.XPATH, "//input[@formcontrolname='catType']"
    
commonelements = CommonLocators()