import pytest



warehouse_data = {
    "warehouse_type_dd": "EXTERNAL",
    "warehouse_subtype_dd": "REGIONAL",
    "warehouse_name": "Demo Warehouse",
    "warehouse_country_dd": "India",
    "warehouse_city": "Delhi",
    "warehouse_incharge_dd": "First User",
    "warehouse_latitude": "23.859685",
    "warehouse_longitude": "76.526958",
    "warehouse_address": "This warehouse entered through automation.",
}


@pytest.mark.testing
def test_add_new_warehouse(setup):
    conftest = setup
    result = conftest.warehouse_page.create_new_warehouse(warehouse_data)
    if "exist" in result.lower():
        print(result)
        assert True
    elif "added" in result.lower():
        toaster = conftest.base_page.get_toaster_message()
        assert "warehouse added successfully" in toaster.lower(), \
        pytest.fail(f"Expected toaster not displayed, but got {toaster}")
    else:
        pytest.fail(f"Unexpected result from create_new_warehouse: {result}")


@pytest.mark.testing
def test_update_warehouse(setup):
    conftest = setup
    update_data = {
        "warehouse_name": f"Updated {warehouse_data['warehouse_name']}",
        "warehouse_city": "Pune",
        "warehouse_address": "This warehouse is updated through automation.",
    }
    result = conftest.warehouse_page.update_warehouse(warehouse_data, update_data)
    if "updated" in result.lower():
        toaster = conftest.base_page.get_toaster_message()
        assert "warehouse updated successfully" in toaster.lower(),\
            pytest.fail(f"Expected toaster not displayed, but got {toaster}")
    elif "added" in result.lower():
        toaster = conftest.base_page.get_toaster_message()
        assert "warehouse added successfully" in toaster.lower(),\
            pytest.fail(f"Expected toaster not displayed, but got {toaster}")
    else:
        pytest.fail(f"Unexpected result from update_warehouse: {result}")


@pytest.mark.testing
def test_delete_warehouse(setup):
    conftest = setup
    result = conftest.warehouse_page.delete_warehouse(warehouse_data)
    if "deleted" in result.lower():
        toaster = conftest.base_page.get_toaster_message()
        assert "warehouse deleted successfully" in toaster.lower(),\
            pytest.fail(f"Expected toaster not displayed, but got {toaster}")
    else:
        pytest.fail(f"unable to delete the warehouse : {result}")

