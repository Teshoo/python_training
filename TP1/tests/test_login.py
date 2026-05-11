from datetime import datetime
from selenium import webdriver
from pages.login_page import LoginPage
from pages.logged_page import LoggedPage

import logging
import os

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

logger = logging.getLogger(__name__)

os.makedirs('screenshots', exist_ok=True)

USERNAME = "tomsmith"
PASSWORD = "SuperSecretPassword!"

driver = webdriver.Chrome()

def test_login()-> None:    
    logger.info("Test Login")
    try:
        logger.info("Initializing...")
        
        login_page = LoginPage(driver)
        logged_page = LoggedPage(driver)
        
        logger.info("Navigating to login page...")
        login_page.open(login_page.URL)
        login_page.wait_login_form_to_be_visible()
        assert login_page.get_login_form() is not None, f"Login form should be visible"
        logger.info("ASSERT: Login page displayed")
        
        logger.info(f"Logging in with [username: {USERNAME}] and [password: {PASSWORD}]...")
        login_page.login(USERNAME, PASSWORD)
        logged_page.wait_url_to_be_correct(logged_page.URL)
        logged_page.wait_success_alert_to_be_visible()
        logged_page.wait_logout_button_to_be_visible()
        assert logged_page.URL in driver.current_url
        assert logged_page.get_success_alert() is not None, f"Success alert should be visible"
        logger.info("ASSERT: Login successful")
        
        logger.info("Logging out...")
        logged_page.logout()
        login_page.wait_url_to_be_correct(login_page.URL)
        login_page.wait_login_form_to_be_visible()
        assert login_page.URL in driver.current_url
        logger.info("ASSERT: Logout successful")
        
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
    test_login()