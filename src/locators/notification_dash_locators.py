from selenium.webdriver.common.by import By



action_required_toggle_button = (By.XPATH, "//label[@for='slider']//span")
snooze_time = (By.XPATH, "//input[@formcontrolname='snoozeTime']")
type_of_alarm_dd = (By.XPATH, "//p-select[@formcontrolname='alarm_type']/div")
technician_dd = (By.XPATH, "//p-select[@formcontrolname='technician']/div")
approver_dd = (By.XPATH, "//p-select[@formcontrolname='approver']/div")
estimated_tat = (By.XPATH, "//input[@formcontrolname='tattime']")
raise_ticket_btn = (By.XPATH, "//button[text() = ' Raise a Ticket ']")