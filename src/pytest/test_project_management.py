import pytest
from src.initialization.config_reader import confr
from selenium.webdriver.support import expected_conditions as ec
from datetime import datetime

today = datetime.now().strftime('%d%m%Y%H%M%S')


@pytest.mark.testing
def test_add_new_project(setup):
    conftest = setup
    conftest.login_page.login(confr.email, confr.password)
    conftest.wait.until(ec.url_contains("solar-plant-dashboard"))
    project_data = {
        "project_code": f"TAP001{today}",
        "project_name": f"Test Automation Project{today}",
        "short_name": f"TAP001{today}",
        "site_address": "123 Test Lane",
        "state_dd": "Bihar",
        "latitude": 25.3652,
        "longitude": 76.2541,
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
        "commission_date_picker": "today",
        "warehouse_dd": "Testing Warehouse",
        "tarrif": 1,
        "data_frequency_dd": "5 Minutes",
        "start_time": "06:00AM",
        "end_time": "06:00PM",
        "display_order":2000
           
    }
    result = conftest.project_page.create_new_project(project_data)
    if "exist" in result.lower():
        print(result)
        assert True
    elif "added" in result.lower():
        toaster = conftest.base_page.get_toaster_message()
        assert "Project added Successfully" in toaster, pytest.fail(f"Expected toaster not displayed, but got {toaster}")
    else:
        pytest.fail(f"Unexpected result from create_new_project: {result}")

@pytest.mark.smoke
def test_update_project(setup):
    conftest = setup
    conftest.login_page.login(confr.email, confr.password)
    conftest.wait.until(ec.url_contains("solar-plant-dashboard"))
    update_data = {
        "project_name": f"Updated Test Automation Project{today}",
        "short_name": f"Updated project short name{today}",
        "project_code": f"Updated project{today}"
        # Add other fields to update as needed
    }
    result = conftest.project_page.update_project("Test Project", update_data)
    if "updated" in result.lower():
        toaster = conftest.base_page.get_toaster_message()
        conftest.log.info(toaster)
        print(result)
        assert True
    elif "added" in result.lower():
        toaster = conftest.base_page.get_toaster_message()
        conftest.log.error(toaster)
        assert "Project added Successfully" in toaster, pytest.fail(f"Expected toaster not displayed, but got {toaster}")
    else:
        pytest.fail(f"Unexpected result from update_project: {result}")


    
    
    
    
    
