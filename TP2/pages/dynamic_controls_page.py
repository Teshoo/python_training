from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class DynamicControls(BasePage):
    URL: str = "https://the-internet.herokuapp.com/dynamic_controls"
    
    CHECKBOX = (By.CSS_SELECTOR, "input[type='checkbox']")
    SWAP_BUTTON = (By.CSS_SELECTOR, "button[onclick='swapCheckbox()']")
    CHECKBOX_STATUS_MESSAGE = (By.CSS_SELECTOR, "form#checkbox-example > p#message")
    TEXT_INPUT = (By.CSS_SELECTOR, "form#input-example > input")
    ENABLE_BUTTON = (By.CSS_SELECTOR, "button[onclick='swapInput()']")
    INPUT_STATUS_MESSAGE = (By.CSS_SELECTOR, "form#input-example > p#message")
    
    def get_checkbox(self):
        return self.driver.find_element(*self.CHECKBOX)
    
    def get_swap_button(self):
        return self.driver.find_element(*self.SWAP_BUTTON)
    
    def get_message(self):
        return self.driver.find_element(*self.CHECKBOX_STATUS_MESSAGE)
    
    def get_input_text(self):
        return self.driver.find_element(*self.TEXT_INPUT)
    
    def get_enable_button(self):
        return self.driver.find_element(*self.ENABLE_BUTTON)
    
    def click_on_swap_button(self):
        self.get_swap_button().click()
    
    def click_on_enable_button(self):
        self.get_enable_button().click()
        
    def add_text_in_input_text(self, text):
        self.get_input_text().send_keys(text)
    
    def wait_checkbox_to_be_visible(self):
        try:
            self.wait.until(
                EC.visibility_of_element_located(self.CHECKBOX)
            ), "Checkbox not visible"
        except Exception as e:
            print(f"Erreur : {e}")
            
    def wait_checkbox_not_to_be_visible(self):
        try:
            self.wait.until(
                EC.invisibility_of_element_located(self.CHECKBOX)
            ), "Checkbox visible"
        except Exception as e:
            print(f"Erreur : {e}")

    def wait_input_to_be_enabled(self):
        try:
            return self.wait.until(
                EC.element_to_be_clickable(self.TEXT_INPUT)
            ), "Input not enabled"
        except Exception as e:
            print(f"Erreur : {e}")