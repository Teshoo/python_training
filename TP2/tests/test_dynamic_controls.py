from datetime import datetime
from selenium import webdriver
from pages.dynamic_controls_page import DynamicControls

import logging
import os

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

logger = logging.getLogger(__name__)
driver = webdriver.Chrome()

os.makedirs('screenshots', exist_ok=True)

def test_dynamic_controls()-> None:
    logger.info("Test Dynamic Controls")
    try:
        logger.info("Initializing...")
        
        page = DynamicControls(driver)
        
        logger.info("Navigating to Dynamic Controls page...")
        page.open(page.URL)
        
        assert page.URL in driver.current_url, f"URL should be {page.URL}"
        logger.info("ASSERT: Dynamic Controls page loaded")
        assert page.get_checkbox() is not None, f"The checkbox should be visible"
        logger.info("ASSERT: The checkbox is visible")
        
        logger.info("Clicking on Remove button...")
        page.click_on_swap_button()
        page.wait_checkbox_not_to_be_visible()
        assert page.get_message().text == "It's gone!", f"Message should be 'It's gone!'; got {page.get_message().text}"
        logger.info("ASSERT: The checkbox is not visible")
        
        logger.info("Clicking on Add button...")
        page.click_on_swap_button()
        page.wait_checkbox_to_be_visible()
        assert page.get_message().text == "It's back!", f"Message should be 'It's back!'; got {page.get_message().text}"
        logger.info("ASSERT: The checkbox is visible")
        
        logger.info("Testing input text...")
        assert page.get_input_text().is_enabled() is False, f"The input text should be disabled"
        logger.info("ASSERT: The input text is disabled")
        
        logger.info("Clicking on Enable button...")
        page.click_on_enable_button()
        page.wait_input_to_be_enabled()
        assert page.get_input_text().is_enabled(), f"The input text should not be disabled"
        logger.info("ASSERT: The input text is not disabled")
        
        logger.info("Adding text in input text...")
        page.add_text_in_input_text("testing")
        assert page.get_input_text().get_attribute("value") == "testing", f"The text inside the input text should be 'testing'; got {page.get_input_text().get_attribute("value")}"
        logger.info("ASSERT: The text is inserted in the input text")
        
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
    test_dynamic_controls()