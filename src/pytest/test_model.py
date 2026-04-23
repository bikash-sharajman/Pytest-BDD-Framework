import pytest
from src.utils.screenshot import take_screenshot




# @pytest.mark.testing
def test_add_new_modal(setup):
    conftest = setup
    result = conftest.model_page.add_new_model("Test model", "Devices", "Demo Make", "SCADA")
    if "already exist" in result:
        conftest.log.warning("Model already present on the table.")
        take_screenshot(conftest.driver)
        return
    else:
        toaster = conftest.base_page.get_toaster_message()
        assert "Model Saved Sucessfully" in toaster, f"Expected toaster not displayed, but got {toaster}"
        take_screenshot(conftest.driver)
        
@pytest.mark.testing
def test_edit_model(setup):
    conftest = setup
    result = conftest.model_page.edit_model("Test model", updated_model_name="Updated model")
    toaster = conftest.base_page.get_toaster_message()
    if "updated" in result.lower():
        conftest.log.info("Model is successfully updated.") 
    elif "created" in result.lower():
        conftest.log.warning("Model not found, details edited after adding the model.")    
    else:
        conftest.log.warning(toaster)
        
    assert "Model updated successfully." in toaster, f"Expected toaster not displayed, but got {toaster}"
    take_screenshot(conftest.driver)
        
        
# @pytest.mark.testing
def test_delete_model(setup):
    conftest = setup
    result = conftest.model_page.delete_model(model_name="Updated model")
    if "deleted" in result.lower():
        conftest.log.info("Model exist and deleted successfully.")        
    else:
        conftest.log.warning("Model not found, in result new model added and deleted.")
    toaster = conftest.base_page.get_toaster_message()
    assert "Model deleted successfully." in toaster, f"Expected toaster not displayed, but got {toaster}"

    