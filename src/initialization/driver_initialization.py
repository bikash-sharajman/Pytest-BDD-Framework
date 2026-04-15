import os
from selenium import  webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.firefox.service import Service as FirefoxService
from src.initialization.config_reader import confr

root_dir = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
driver_dir = os.path.join(root_dir, "Drivers")
chromium_dir = os.path.join(root_dir, "chromium")

chrome_driver_path = os.path.join(driver_dir, "chromedriver.exe")
chromium_path = os.path.join(chromium_dir, "chrome.exe")
firefox_driver_path = os.path.join(driver_dir, "geckodriver.exe")


class DriverInit:

    @staticmethod
    def setup_driver(browser: str = None, headless: bool = None):
        browser = (browser or confr.get_browser()).lower()
        headless = confr.get_headless() if headless is None else headless
        timeout = confr.get_timeout()

        if browser == "chrome":
            options = ChromeOptions()
            if headless:
                options.add_argument("--headless=new")
                options.add_argument("--window-size=1920,1080")
            else:
                options.add_argument("--start-maximized")
            # options.binary_location = chromium_path
            options.add_argument("--disable-gpu")
            options.add_argument("--no-sandbox")
            options.add_argument("--disable-dev-shm-usage")
            options.add_argument("--remote-debugging-port=0")
            options.add_argument("--no-first-run")
            options.add_argument("--no-default-browser-check")
            options.add_argument("--disable-extensions")
            # options.add_argument(f"--user-data-dir={tempfile.mkdtemp(prefix='chrome-profile-')}")
            # service = ChromeService(executable_path=chromium_path)
            service = ChromeService(executable_path=chrome_driver_path)
            driver = webdriver.Chrome(service=service, options=options)

        elif browser == "firefox":
            options = FirefoxOptions()
            if headless:
                options.add_argument("--headless")
            service = FirefoxService(executable_path=firefox_driver_path)
            driver = webdriver.Firefox(service=service, options=options)

        else:
            raise ValueError(f"Unsupported browser: {browser}")

        if headless:
            driver.set_window_size(1920, 1080)
        else:
            driver.maximize_window()

        wait = WebDriverWait(driver, timeout)
        return driver, wait


        
di = DriverInit()






