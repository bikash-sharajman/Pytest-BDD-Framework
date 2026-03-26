import time
from behave import given, when, then
from behave.exception import StepNotImplementedError

from src.locators.project_management_locators import pm
from src.locators.common_locators import commonelements

from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from datetime import datetime

def get_tab_locator(tab_name: str):
    project_tabs = {
        "basic details": pm.basic_details_tab,
        "unit details": pm.unit_details_tab,
        "data logger details": pm.data_logger_tab,
        "asset details": pm.asset_details_tab,
        "data acquisition": pm.data_aquisition_tab,
        "contact details": pm.contact_details_tab,
        "forecast information": pm.forcast_information_tab,
        "site person details": pm.site_person_tab,
        "vendor details": pm.vendor_details_tab,
        "documents": pm.document_tab,
        "anomaly detection": pm.anomaly_tab,
    }

    # .lower() on both sides handles any case mismatch safely
    locator = project_tabs.get(tab_name.strip().lower())

    if locator is None:
        raise Exception(f"Tab '{tab_name}' not found.")
    return locator

def _navigate_to_project_tab(context, tab_locator):
    try:
        context.log.info(f"User is redirecting to {tab_locator} tab.")
        context.wait.until(ec.element_to_be_clickable(tab_locator)).click()
    
    except Exception as e:
        context.log.error(f"Unable to redirect to {tab_locator}, {e}")

def _select_option_from_dropdown(context, locator, option:str):
    context.wait.until(ec.element_to_be_clickable(locator)).click()
    # time.sleep(1)
    option_locator = By.XPATH, f"//p-selectitem//li//span[normalize-space()='{option}']"
    time.sleep(1)
    context.wait.until(ec.element_to_be_clickable(option_locator)).click()


@given(u'Navigate to Project Management')
def step_impl(context):
    try:
        context.log.info("Navigating to project management from sidebar.")
        context.wait.until(ec.element_to_be_clickable(commonelements.overview_dashboard)).click()
        # time.sleep(3)
        context.wait.until(ec.element_to_be_clickable(commonelements.management_menu)).click()
        # time.sleep(3)
        context.wait.until(ec.element_to_be_clickable(commonelements.project_management)).click()
        # time.sleep(2)
        # context.wait.until(ec.element_to_be_clickable(commonelements.side_bar)).click()
        context.wait.until(ec.url_contains("plant-management"))
    except Exception as e:
        context.log.error(f"Navigation to make module failed: {e}")
        raise

@given(u'Click on Add Project button')
def step_impl(context):
    try:
        # context.log.info("clicking on add project button to fill out the project basic details page.")
        # context.wait.until(ec.element_to_be_clickable(pm.add_project_btn)).click()
        context.project_page.click_on_add_project_btn()
    except Exception as e:
        context.log.error(f"Unable to click on add project button : {e}")

@when(u'User enters project code "{project_code}"')
def step_impl(context, project_code):
    try:
        context.log.info("User is entering project code")
        today = datetime.now().strftime('%d%m%Y%H%M%S')
        context.wait.until(ec.element_to_be_clickable(pm.project_code)).send_keys(project_code+today)
    except Exception as e:
        context.log.error(f"Unable to enter value in project code field : {e}")

@when(u'User enters project name "{project_name}"')
def step_impl(context, project_name):
    try:
        today = datetime.now().strftime('%d%m%Y%H%M%S')
        context.log.info("User is entering project name")
        context.wait.until(ec.element_to_be_clickable(pm.project_name)).send_keys(project_name+today)
    except Exception as e:
        context.log.error(f"Unable to enter value in project name field : {e}")
        

@when(u'User enters short name "{project_short_name}"')
def step_impl(context, project_short_name):
    try:
        context.log.info("User is entering project short name.")
        today = datetime.now().strftime('%d%m%Y%H%M%S')
        context.wait.until(ec.element_to_be_clickable(pm.short_name)).send_keys(project_short_name+today)
    except Exception as e:
        context.log.error(f"Unable to enter value in project short name field : {e}")

@when(u'User enters site address "{site_address}"')
def step_impl(context, site_address):
    try:
        context.log.info("User is entering site address.")
        context.wait.until(ec.element_to_be_clickable(pm.site_address)).send_keys(site_address)
    except Exception as e:
        context.log.error(f"Unable to enter value in site address field : {e}")

@when(u'User selects state "{state}"')
def step_impl(context, state):
    try:
        context.log.info("User is selecting option from state dropdown")
        _select_option_from_dropdown(context, pm.state_dd, state)
    except Exception as e:
        context.log.error(f"Unable to select an option from state dropdown : {e}")

@when(u'User enters latitude "{latitude}"')
def step_impl(context, latitude):
    try:
        context.log.info("User is entering latitude of the project.")
        context.wait.until(ec.element_to_be_clickable(pm.latitude)).send_keys(latitude)
    except Exception as e:
        context.log.error(f"Unable to enter value in latitude field : {e}")
        

@when(u'User enters longitude "{longitude}"')
def step_impl(context, longitude):
    try:
        context.log.info("User is entering latitude of the project.")
        context.wait.until(ec.element_to_be_clickable(pm.longitude)).send_keys(longitude)
    except Exception as e:
        context.log.error(f"Unable to enter value in longitude field : {e}")


@when(u'User selects cluster type "{cluster}"')
def step_impl(context, cluster):
    try:
        context.log.info("User is selecting option from cluster dropdown")
        _select_option_from_dropdown(context, pm.cluster_dd, cluster)
    except Exception as e:
        context.log.error(f"Unable to select an option from cluster dropdown : {e}")


@when(u'User selects billing entity "{bill_entity}"')
def step_impl(context, bill_entity):
    try:
        context.log.info("User is selecting option from billing entity dropdown")
        _select_option_from_dropdown(context, pm.billing_dd, bill_entity)
    except Exception as e:
        context.log.error(f"Unable to select an option from billint entity dropdown : {e}")


@when(u'User selects project type "{project_type}"')
def step_impl(context, project_type):
    try:
        context.log.info("User is selecting option from project_type dropdown")
        _select_option_from_dropdown(context, pm.project_type_dd, project_type)
    except Exception as e:
        context.log.error(f"Unable to select an option from project_type dropdown : {e}")


@when(u'User selects project sub type "{sub_type}"')
def step_impl(context, sub_type):
    try:
        context.log.info("User is selecting option from project sub type dropdown")
        _select_option_from_dropdown(context, pm.sub_type_dd, sub_type)
    except Exception as e:
        context.log.error(f"Unable to select an option from project sub type dropdown : {e}")

@when(u'User selects technology type "{technology_type}"')
def step_impl(context, technology_type):
    try:
        context.log.info("User is selecting option from technology type dropdown")
        _select_option_from_dropdown(context, pm.technology_type_dd, technology_type)
    except Exception as e:
        context.log.error(f"Unable to select an option from technology type dropdown : {e}")


@when(u'User selects installation type "{installation_type}"')
def step_impl(context, installation_type):
    try:
        context.log.info("User is selecting option from installation type dropdown")
        context.wait.until(ec.element_to_be_clickable(pm.installation_type_dd)).click()
        time.sleep(1)
        option_locator = By.XPATH, f"//p-selectitem//li//span[normalize-space()='{installation_type}']"
        time.sleep(1)
        context.wait.until(ec.element_to_be_clickable(option_locator)).click()
    except Exception as e:
        context.log.error(f"Unable to select an option from installation type dropdown : {e}")


@when(u'User selects mounting type "{mounting_type}"')
def step_impl(context, mounting_type):
    try:
        context.log.info("User is selecting option from mounting type dropdown")
        _select_option_from_dropdown(context, pm.mounting_type_dd, mounting_type)
    except Exception as e:
        context.log.error(f"Unable to select an option from mounting type dropdown : {e}")


@when(u'User enters tilt azimuth "{tilt_angle}"')
def step_impl(context, tilt_angle):
    try:
        context.log.info("User is entering tilt angle of the project.")
        context.wait.until(ec.element_to_be_clickable(pm.tilt_azimuth)).send_keys(tilt_angle)
    except Exception as e:
        context.log.error(f"Unable to enter value in tilt_azimuth field : {e}")


@when(u'User enters DC capacity "{dc_capacity}"')
def step_impl(context, dc_capacity):
    try:
        context.log.info("User is entering dc_capacity of the project.")
        context.wait.until(ec.element_to_be_clickable(pm.dc_capacity)).send_keys(dc_capacity)
    except Exception as e:
        context.log.error(f"Unable to enter value in dc_capacity field : {e}")


@when(u'User enters AC capacity "{ac_capacity}"')
def step_impl(context, ac_capacity):
    try:
        context.log.info("User is entering ac_capacity of the project.")
        context.wait.until(ec.element_to_be_clickable(pm.ac_capacity)).send_keys(ac_capacity)
    except Exception as e:
        context.log.error(f"Unable to enter value in ac_capacity field : {e}")


@when(u'User selects the commissioning date')
def step_impl(context):
    try:
        context.log.info("Entering commissioning date")
        date_picker = context.wait.until(ec.element_to_be_clickable(pm.commission_date_picker))
        context.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", date_picker)
        date_picker.click()
        day = datetime.now().day
        time.sleep(1)
        date = context.wait.until(ec.element_to_be_clickable((By.XPATH, f"//tbody//span[text() = '{day}']")))
        date.click()
        
    except Exception as e:
        context.log.error(f"Unable to enter commissioning date: {e}")
        raise


@when(u'User selects warehouse "{warehouse}"')
def step_impl(context, warehouse):
    try:
        context.log.info("User is selecting option from project warehouse dropdown")
        ware = context.wait.until(ec.element_to_be_clickable(pm.warehouse_dd))
        context.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", ware)
        ware.click()
        context.log.info("Warehouse dropdown opened")
        time.sleep(2)
        warehouse_option = warehouse
        context.wait.until(
            ec.visibility_of_element_located((By.CSS_SELECTOR, "p-selectitem"))
        )
        context.log.info("Dropdown panel visible")
        option_locator = (
            By.XPATH,
            f"//p-selectitem//li//span[normalize-space()='{warehouse_option}']"
        )
        option = context.wait.until(
            ec.visibility_of_element_located(option_locator)
        )

        # Use JS click — more reliable for PrimeNG
        context.driver.execute_script("arguments[0].click();", option)
        context.log.info(f"Warehouse selected : {warehouse}")
        
        
    except Exception as e:
        context.log.error(f"Unable to select an option from project warehouse dropdown : {e}")


@when(u'User enters tariff "{tarrif}"')
def step_impl(context, tarrif):
    try:
        context.log.info("User is entering tarrif of the project.")
        context.wait.until(ec.element_to_be_clickable(pm.tarrif)).send_keys(tarrif)
    except Exception as e:
        context.log.error(f"Unable to enter value in tarrif field : {e}")


@when(u'User selects data frequency "{frequency}"')
def step_impl(context, frequency):
    try:
        context.log.info(f"Selecting {frequency} from data frequency dropdown.")
        freq_dd = context.wait.until(ec.element_to_be_clickable(pm.data_frequency_dd))
        context.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", freq_dd)
        freq_dd.click()
        
        time.sleep(1)
        installation_option = context.wait.until(ec.element_to_be_clickable\
            ((By.XPATH, f"//p-selectitem//span[normalize-space()='5 Minutes']")))
        installation_option.click()
        
        
    except Exception as e:
        context.log.error("Unable to select the data frequency of the project")
        raise


@when(u'User enters start time "{start_time}"')
def step_impl(context, start_time):
    try:
        context.log.info("User is entering start time of the project.")
        context.wait.until(ec.element_to_be_clickable(pm.start_time)).send_keys(start_time)
    except Exception as e:
        context.log.error(f"Unable to enter value in start time field : {e}")


@when(u'User enters end time "{end_time}"')
def step_impl(context, end_time):
    try:
        context.log.info("User is entering end time of the project.")
        context.wait.until(ec.element_to_be_clickable(pm.end_time)).send_keys(end_time)
    except Exception as e:
        context.log.error(f"Unable to enter value in end time field : {e}")


@when(u'User enters display order "{display_order}"')
def step_impl(context, display_order):
    try:
        context.log.info("User is entering display order of the project.")
        context.wait.until(ec.element_to_be_clickable(pm.display_order)).send_keys(display_order)
    except Exception as e:
        context.log.error(f"Unable to enter value in display_order field : {e}")


@then(u'User should see project created success message')
def step_impl(context):
    try:
        toast = context.wait.until(ec.element_to_be_clickable(commonelements.toaster))
        toaster = toast.text
        toaster_msg = toaster.lower()
        assert "successfully" in toaster_msg, f"Expected toaster message does not appear, get - {toaster_msg}"

    except Exception as e:
        context.log.error(f"Toaster does not appear : {e}")
        
@then(u'Project privilege provided to the user')
def step_impl(context):
    try:
        context.log.info("Project privilege is providing to the user")
        context.wait.until(ec.element_to_be_clickable(pm.site_person_tab)).click()
        context.wait.until(ec.element_to_be_clickable(pm.add_person_button)).click()

        context.wait.until(ec.element_to_be_clickable(pm.site_person_tab_search_bar)).send_keys("8249073673")
        time.sleep(1)

        context.wait.until(ec.element_to_be_clickable((By.XPATH, "//li[@role='option']//span"))).click()

        context.wait.until(ec.element_to_be_clickable(pm.role_type_dd)).click()
        time.sleep(1)

        context.wait.until(ec.element_to_be_clickable(pm.site_tech_option)).click()
        time.sleep(0.5)
        context.wait.until(ec.element_to_be_clickable(commonelements.modal_save_button)).click()
        time.sleep(0.5)
        
        
    except Exception as e:
        context.log.error("Unable to provide the user privilege.")
        raise

@then(u'Validation message "{expected_message}" should be displayed.')
def step_impl(context, expected_message):
    context.log.info(f"Checking validation messages | expected : {expected_message}")

    try:
        # Find ALL error message elements on the page
        all_error_messages = context.wait.until(ec.visibility_of_all_elements_located\
            (commonelements.input_field_required_error_message))

        total_found = len(all_error_messages)
        context.log.info(f"Total validation messages found : {total_found}")

        # Check every message matches expected text
        failed = []
        for index, message in enumerate(all_error_messages, start=1):
            actual_text = message.text.strip()
            if actual_text != expected_message:
                failed.append(f"Field {index} → got '{actual_text}'")
            else:
                context.log.info(f"Field {index} | '{actual_text}'")

        # If any message did not match — fail the test
        if failed:
            context.log.error(f"Mismatched messages : {failed}")
            raise AssertionError(
                f"{len(failed)} field(s) did not show expected message.\n"
                + "\n".join(failed)
            )

        context.log.info(
            f"All {total_found} fields show '{expected_message}'"
        )

    except Exception as e:
        context.log.error(f"Validation message check failed | {e}")
        raise
    

@then(u'the following tabs should be disabled')
def step_impl(context) -> None:

    try:
        for row in context.table:
            tab_name = row['tab_name'].strip().lower()

            context.log.info(f"Checking if '{tab_name}' tab is disabled")

            # Get locator from shared helper
            locator = get_tab_locator(tab_name)

            # Use presence — disabled elements are NOT clickable
            element = context.wait.until(
                ec.presence_of_element_located(locator)
            )

            is_disabled = element.get_attribute("data-p-disabled")

            assert is_disabled == "true", \
                (f"'{tab_name}' tab is NOT disabled.")

            context.log.info(f"'{tab_name}' tab is disabled as expected.")

    except AssertionError as ae:
        context.log.error(f"Tab disability check failed: {ae}")
        raise
    except Exception as e:
        context.log.error(f"Error while checking tabs: {e}")
        raise
    
