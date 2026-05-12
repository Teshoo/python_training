from datetime import datetime
from selenium import webdriver
from pages.dynamic_loading_page import DynamicLoading

import logging
import os

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

logger = logging.getLogger(__name__)
driver = webdriver.Chrome()

os.makedirs('screenshots', exist_ok=True)

def test_dynamic_loading()-> None:
    logger.info("Test Dynamic Controls")
    try:
        logger.info("Initializing...")
        
        page = DynamicLoading(driver)
        
        logger.info("Navigating to Dynamic Loading page...")
        page.open(page.URL)
        
        assert page.URL in driver.current_url, f"URL should be {page.URL}"
        logger.info("ASSERT: Dynamic Loading page loaded")
        
        logger.info("Clicking on Example 2 link...")
        page.click_on_example_2_link()
        assert page.URL_EXAMPLE_2 in driver.current_url
        logger.info("ASSERT: Example 2 page loaded")
        assert page.get_start_button() is not None, f"The Start button should be visible"
        logger.info("ASSERT: The Start button is visible")
        
        logger.info("Clicking on the Sart button...")
        page.click_on_start_button()
        page.wait_hello_world_to_be_visible()
        assert page.get_hello_world_title().text == "Hello World!", f"Message should be 'Hello World!'; got {page.get_hello_world_title().text}"
        logger.info("ASSERT: The text Hello World is displayed")
        
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
    test_dynamic_loading()