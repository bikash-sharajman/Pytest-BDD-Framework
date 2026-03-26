import time
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from datetime import datetime
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains
from src.initialization.config_reader import confr
from src.initialization.driver_initialization import di
from src.locators.login_locators import loginelements
from src.locators.common_locators import commonelements
from src.utils.logger import get_logger
from src.pages.make import MakeModule
from src.pages.project_management_page import ProjectManagement
from src.utils.screenshot import take_screenshot

def before_scenario(context, scenario):
    context.driver, context.wait = di.setup_driver(confr.get_browser())
    context.actions = ActionChains(context.driver)    
    context.make_page = MakeModule(context.driver, context.wait)
    context.project_page = ProjectManagement(context.driver, context.wait)

    if 'login_required' in scenario.tags:
        url = confr.get_baseurl()
        context.driver.get(f"{url}/login")
        context.wait.until(ec.element_to_be_clickable(loginelements.email_field)).send_keys(confr.username)
        context.wait.until(ec.element_to_be_clickable(loginelements.password_field)).send_keys(confr.password)
        context.wait.until(ec.element_to_be_clickable(loginelements.login_button)).click()
        context.wait.until(ec.url_contains('solar'))
        print("Login successfull.")
        time.sleep(1)
        
def before_step(context, step):
    context.log = get_logger()

def after_step(context, step):
    if step.status in ["failed", "error"]:
        context.log.error("capturing screenshot")
        take_screenshot(context.driver, step.name)   


# def take_screenshot(context, step):
    try:
        context.log.info("Inside screenshot function")
        if not hasattr(context, "driver"):
            context.log.error("Driver not available in context")
            return

        timestamp = datetime.now().strftime("%H%M%S")

        scenario_name = context.scenario.name.replace(" ", "_")
        step_name = step.name.replace(" ", "_")

        file_name = f"{scenario_name}-{timestamp}.png"
        file_path = os.path.join(context.screenshot_dir, file_name)

        context.log.info(f"Saving screenshot at: {file_path}")

        success = context.driver.save_screenshot(file_path)

        context.log.info(f"Screenshot save status: {success}")

    except Exception as e:
        context.log.error(f"Screenshot error: {e}")

    try:
        if not context.driver:
            context.log.error("Driver not found!")
            return
        timestamp = datetime.now().strftime("%H%M%S")

        scenario_name = context.scenario.name.replace(" ", "_")[:50]
        step_name = step.name.replace(" ", "_")[:50]

        file_name = f"{scenario_name}__{step_name}__{timestamp}.png"

        file_path = os.path.join(context.screenshot_dir, file_name)

        context.driver.save_screenshot(file_path)

        context.log.error(f"Screenshot saved: {file_path}")

    except Exception as e:
        context.log.error(f"Failed to capture screenshot: {e}")
def after_scenario(context, scenario):
    try:
        context.driver.quit()
        context.driver = None
    except Exception:
        pass
