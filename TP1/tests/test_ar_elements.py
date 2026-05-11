from datetime import datetime
from selenium import webdriver
from pages.a_r_elements_page import ARElementsPage

import logging
import os

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

logger = logging.getLogger(__name__)
driver = webdriver.Chrome()

os.makedirs('screenshots', exist_ok=True)

def test_ar_elements()-> None:    
    logger.info("Test Add/Remove Elements")
    try:
        logger.info("Initializing...")
        
        page = ARElementsPage(driver)
        
        logger.info("Navigating to Add/Remove Elements page...")
        page.open(page.URL)
 
        page.wait_add_element_button_to_be_visible()
        assert page.get_add_element_button() is not None, f"Add Element button should be visible"
        logger.info("ASSERT: Add/Remove Elements page displayed")
        
        logger.info("Clicking on Add Element Button 3 times...")
        for i in range(0,3):
            page.click_on_add_element_button()
        nb_delete_buttons = len(page.get_delete_element_buttons())
        assert nb_delete_buttons == 3, f"There should be 3 Delete buttons, got {nb_delete_buttons}"
        logger.info("ASSERT: 3 elements added")
        
        logger.info("Clicking on first Delete element button...")
        page.click_on_first_delete_element_button()
        nb_delete_buttons = len(page.get_delete_element_buttons())
        assert nb_delete_buttons == 2, f"There should be 2 Delete buttons, got {nb_delete_buttons}"
        logger.info("ASSERT: 2 elements left")
        
        logger.info("Deleting all elements...")
        page.delete_all_elements()
        nb_delete_buttons = len(page.get_delete_element_buttons())
        assert nb_delete_buttons == 0, f"There should be 0 Delete buttons, got {nb_delete_buttons}"
        logger.info("ASSERT: 0 elements left")
        
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
    test_ar_elements()