import pytest
from selenium.webdriver.support import expected_conditions as ec
from src.initialization.driver_initialization import di
from src.initialization.config_reader import confr
from src.pages.base_file import BasePage
from src.pages.login import Login
from src.pages.category import CategoryPage
from src.pages.make import MakePage
from src.pages.sub_category import SubCategoryPage
from src.pages.project_management_page import ProjectManagement
from src.pages.warehouse import WarehousePage
from src.pages.model import Model
from src.utils.logger import get_logger


class PageObjects:
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait
        self.base_page = BasePage(driver, wait)
        self.login_page = Login(driver, wait)
        self.category_page = CategoryPage(driver, wait)
        self.make_page = MakePage(driver, wait)
        self.sub_category_page = SubCategoryPage(driver, wait)
        self.log = get_logger()
        # self.take_screenshot = ss.take_screenshot(driver)
        self.project_page = ProjectManagement(driver, wait)
        self.warehouse_page = WarehousePage(driver, wait)
        self.model_page = Model(driver, wait)
        
_base_url = confr.get_baseurl()
_url = f"{_base_url}/login"
    
@pytest.fixture(scope="function")
def setup():
    driver, wait = di.setup_driver()
    driver.get(_url)
    object = PageObjects(driver, wait)
    
    yield object
    
    driver.quit()


@pytest.fixture(autouse=True)
def before_test(setup, request):
    if request.node.get_closest_marker("no_login"):
        yield
        return

    conftest = setup
    conftest.login_page.login(confr.email, confr.password)
    conftest.wait.until(ec.url_contains("solar-plant-dashboard"))

    yield
    
    
    
    

# @pytest.fixture(scope="function")
# def ood(setup):
#     conftest = setup
#     try:
#         driver = conftest.driver
#         wait = conftest.wait
#         driver.get(f"{base_url}/solar-plant-dashboard")

#         # 🔹 Wait for URL to change (either dashboard or login)
#         wait.until(lambda d: "solar-plant-dashboard" in d.current_url.lower()
#                              or "login" in d.current_url.lower()
#                              or "no-privilege" in d.current_url.lower())

#         url = driver.current_url.lower()
#         if "solar-plant-dashboard" in url:
#             conftest.log.info("User is already on overview dashboard page.")
#             return True

#         elif "login" in url:
#             conftest.log.info("Perform login and redirect to overview page.")
#             conftest.login_page.login(confr.email, confr.password)
#             wait.until(ec.url_contains("solar-plant-dashboard"))
#             conftest.log.info("Login successful, redirected on dashboard.")
#             return True

#         elif "no-privilege" in url:
#             conftest.log.error("No privilege to access overview dashboard.")
#             return False

#         else:
#             conftest.log.error(f"Unexpected URL: {url}")
#             return False

#     except TimeoutException as e:
#         conftest.log.error(f"Timeout in open_overview_dashboard: {str(e)}")
#         return False
