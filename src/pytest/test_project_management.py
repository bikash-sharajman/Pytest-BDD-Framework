import pytest
from datetime import datetime


today = datetime.now().strftime('%d%m%Y%H%M%S')
project_data = {
    "project_code": f"TAP001{today}",
    "project_name": f"Test Automation Project{today}",
    "short_name": f"TAP001{today}",
    "site_address": "123 Test Lane",
    "state_dd": "Bihar",
    # "latitude": 25.3652,
    # "longitude": 76.2541,
    "cluster_dd": "first demo",
    "billing_dd": "Refex",
    "project_type_dd": "Solar Management System",
    "sub_type_dd": "Solar Power Storage",
    "technology_type_dd": "Monocrystalline",
    "installation_type_dd": "Ground Mount",
    "mounting_type_dd": "Fixed Tilt",
    "tilt_azimuth": 30,
    "dc_capacity": 1500,
    "ac_capacity": 1000,
    "commission_date_picker": 3,
    "warehouse_dd": "Testing Warehouse",
    "tarrif": 1,
    "data_frequency_dd": "5 Minutes",
    "start_time": "06:00AM",
    "end_time": "06:00PM",
    "display_order": 2001
}

@pytest.mark.testing
def test_add_new_project(setup):
    conftest = setup
    result = conftest.project_page.create_new_project(project_data)
    if "exist" in result.lower():
        conftest.log.warning("Project already exist on the table, skipping the add new project steps.")
        return
    elif "added" in result.lower():
        conftest.log.warning("Project successfully added into the system and user gets the privilege for the project. Validating toaster message.")
        toaster = conftest.base_page.get_toaster_message()
        assert "User added to Project Successfully" in toaster, f"Expected toaster not displayed, but got {toaster}"
    else:
        pytest.fail(f"Unexpected result from create_new_project: {result}")

@pytest.mark.testing
def test_update_project(setup):
    conftest = setup
    # today = datetime.now().strftime('%d%m%Y%H%M%S')
    update_data = {
        "project_name": f"Updated {project_data['project_name']}",
        "project_code": f"Updated {project_data['project_code']}"
        
    }
    result = conftest.project_page.update_project(project_data, update_data)
    if "updated" in result.lower():
        toaster = conftest.base_page.get_toaster_message()
        conftest.log.info(toaster)
        print(result)
        assert True
    elif "added" in result.lower():
        toaster = conftest.base_page.get_toaster_message()
        conftest.log.error(toaster)
        assert "Project added Successfully" in toaster, f"Expected toaster not displayed, but got {toaster}"
    else:
        pytest.fail(f"Unexpected result from update_project: {result}")
        

@pytest.mark.usefixtures("setup")
def test_add_project_unit_details():
    pass


    
    
    
    
    
