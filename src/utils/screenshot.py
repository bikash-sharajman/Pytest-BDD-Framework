import os
from datetime import datetime
import inspect


    
def take_screenshot(driver, name=None):
    try:
        base_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        screenshot_name = name or inspect.stack()[1].function
        now = datetime.now()
        screenshot_dir = os.path.join(base_dir, "screenshots", now.strftime("%Y"), now.strftime("%m"), now.strftime("%d"))
        
        os.makedirs(screenshot_dir, exist_ok=True)
        
        timestamp = now.strftime("%H%M%S")
        
        file_name = f"{screenshot_name.replace(' ', '_')}_{timestamp}.png"
        file_path = os.path.join(screenshot_dir, file_name)
        
        driver.save_screenshot(file_path)
        print(f"Screenshot saved: {file_path}")
        return file_path

    except Exception as e:
        print(f"Screenshot failed: {e}")



