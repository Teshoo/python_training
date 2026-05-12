from datetime import datetime
from selenium import webdriver
from pages.infinite_scroll_page import InfiniteScroll

import logging
import os
import time

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

logger = logging.getLogger(__name__)
driver = webdriver.Chrome()

SCROLL_PAUSE = 2

os.makedirs('screenshots', exist_ok=True)

def test_infinite_scroll()-> None:
    logger.info("Test Dynamic Controls")
    try:
        logger.info("Initializing...")
        
        page = InfiniteScroll(driver)
        
        logger.info("Navigating to Infinite Scroll page...")
        page.open(page.URL)
        assert page.URL in driver.current_url, f"URL should be {page.URL}"
        logger.info("ASSERT: Infinite Scroll page loaded")
        assert page.get_text_blocks()[0] is not None, f"First text block should be displayed"
        logger.info("ASSERT: The first text block is displayed")
        
        logger.info("Scrolling to footer 5 times...")
        for i in range(0,5):
            nb_blocks_before = len(page.get_text_blocks())
            page.scroll_page()
            time.sleep(SCROLL_PAUSE)
            assert nb_blocks_before < len(page.get_text_blocks()), f"Number of blocks should have incresed; got {nb_blocks_before} vs {len(page.get_text_blocks())}"
        logger.info("ASSERT: Number of text blocks has increased after each scrolling")
        
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
    test_infinite_scroll()