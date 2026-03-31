import pytest
from src.initialization.driver_initialization import di
from src.initialization.config_reader import confr
from src.pages.base_file import BasePage
from src.pages.login import Login
from src.pages.category import CategoryPage
from src.pages.make import MakePage
from src.pages.sub_category import SubCategory
from src.utils.logger import get_logger


class Conftest:
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait
        self.base_page = BasePage(driver, wait)
        self.login_page = Login(driver, wait)
        self.category_page = CategoryPage(driver, wait)
        self.make_page = MakePage(driver, wait)
        self.subCategory_page = SubCategory(driver, wait)
        self.log = get_logger()
        
base_url = confr.get_baseurl()
url = f"{base_url}/login"
    
@pytest.fixture(scope="function")
def setup():
    driver, wait = di.setup_driver("chrome")
    driver.get(url)
    
    conftest = Conftest(driver, wait)
    
    yield conftest

    driver.quit()
