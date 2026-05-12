from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class DynamicLoading(BasePage):
    URL: str = "https://the-internet.herokuapp.com/dynamic_loading"
    URL_EXAMPLE_2: str = URL + "/2"
    
    EXAMPLE_2_LINK = (By.CSS_SELECTOR, "a[href='/dynamic_loading/2']")
    START_BUTTON = (By.CSS_SELECTOR, "div#start > button")
    HELLO_WORLD_TITLE = (By.CSS_SELECTOR, "div#finish")
    
    def get_start_button(self):
        return self.driver.find_element(*self.START_BUTTON)
    
    def get_hello_world_title(self):
        return self.driver.find_element(*self.HELLO_WORLD_TITLE)
    
    def click_on_example_2_link(self):
        self.driver.find_element(*self.EXAMPLE_2_LINK).click()
    
    def click_on_start_button(self):
        return self.driver.find_element(*self.START_BUTTON).click()
    
    def wait_hello_world_to_be_visible(self):
        try:
            self.wait.until(
                EC.visibility_of_element_located(self.HELLO_WORLD_TITLE)
            ), "Hello World not visible"
        except Exception as e:
            print(f"Erreur : {e}")