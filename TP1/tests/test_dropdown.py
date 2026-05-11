from datetime import datetime
from selenium import webdriver
from pages.dropdown_page import DropdownPage

import logging
import os

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

logger = logging.getLogger(__name__)
driver = webdriver.Chrome()

os.makedirs('screenshots', exist_ok=True)

def test_dropdown_list()-> None:    
    logger.info("Test Dropdown List")
    try:
        logger.info("Initializing...")
        
        page = DropdownPage(driver)
        
        logger.info("Navigating to Dropdown List page...")
        page.open(page.URL)
        page.wait_dropdown_list_to_be_visible()
        assert page.get_dropdown_list() is not None, f"Dropdown list should be visible"
        logger.info("ASSERT: Dropdown List page displayed")
        
        logger.info("Selecting option 1 in dropdown list...")
        page.select_an_option("1")
        assert page.get_selected_value() == "1", f"Selected option should be 1"
        logger.info("ASSERT: Option 1 selected")
        
        logger.info("Selecting option 2 in dropdown list...")
        page.select_an_option("2")
        assert page.get_selected_value() == "2", f"Selected option should be 2"
        logger.info("ASSERT: Option 2 selected")
        
    except Exception as e:
        logger.error(f"Error: {e}")
        logger.error("Stack trace:", exc_info=True)
        
        if driver:
            screenshot_name = f"screenshots/error_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
            driver.save_screenshot(screenshot_name)
            logger.info(f" Screenshot sauvegardé: {screenshot_name}")

    finally:
        if driver:
            logger.info("Closing WebDriver...")
            driver.quit()
            logger.info(" WebDriver closed")
        
        logger.info("Test ended")
        
if __name__ == "__main__":
    test_dropdown_list()