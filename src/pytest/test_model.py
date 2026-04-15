import pytest
from src.initialization.config_reader import confr
from selenium.webdriver.support import expected_conditions as ec
from src.utils.screenshot import take_screenshot


@pytest.mark.testing
def test_add_new_model(setup):
    conftest = setup
    