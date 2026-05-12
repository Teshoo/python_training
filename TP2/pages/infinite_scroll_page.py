from pages.base_page import BasePage
from selenium.webdriver import ActionChains
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class InfiniteScroll(BasePage):
    URL: str = "https://the-internet.herokuapp.com/infinite_scroll"
    
    TEXT_BLOCK = (By.CLASS_NAME, "jscroll-added")
    FOOTER = (By.ID, "page-footer")
    
    def get_text_blocks(self):
        return self.driver.find_elements(*self.TEXT_BLOCK)
    
    def get_footer(self):
        return self.driver.find_element(*self.FOOTER)
    
    def scroll_page(self):
        ActionChains(self.driver)\
            .scroll_to_element(self.get_footer()).perform()