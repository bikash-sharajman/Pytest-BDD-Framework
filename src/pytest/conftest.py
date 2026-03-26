import pytest
from src.initialization.driver_initialization import di
from src.initialization.config_reader import confr



base_url = confr.get_baseurl()
url = f"{base_url}/login"

@pytest.fixture(scope="function")
def setup():
    driver, wait = di.setup_driver("chrome")
    driver.get(url)
    
    yield driver, wait

    driver.quit()
