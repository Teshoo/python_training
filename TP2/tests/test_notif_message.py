from datetime import datetime
from selenium import webdriver
from pages.notification_page import NotificationPage

import logging
import os

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

logger = logging.getLogger(__name__)
driver = webdriver.Chrome()

os.makedirs('screenshots', exist_ok=True)

def test_notification_message()-> None:
    logger.info("Test Notification Message")
    try:
        logger.info("Initializing...")
        
        page = NotificationPage(driver)
        
        logger.info("Navigating to Notification Message page...")
        page.open(page.URL)
        
        assert page.URL in driver.current_url
        logger.info("ASSERT: Notification Message page loaded")
        
        logger.info("Clicking on Click Here button...")
        page.click_on_click_here_button()
        page.wait_notification_to_be_visible()
        assert page.get_notification_text() is not None
        logger.info("ASSERT: Notification message is displayed")
        
        logger.info("Clicking on Click Here button 10 times...")
        for i in range(0,10):
            page.click_on_click_here_button()
            assert page.is_a_correct_notification_message()
        logger.info("ASSERT: Notification messages are correct")
        
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
    test_notification_message()