from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select

class DropdownPage(BasePage):
    URL: str = "https://the-internet.herokuapp.com/dropdown"
    
    DROPDOWN_LIST = (By.ID, "dropdown")
    SELECTED_OPTION = (By.CSS_SELECTOR, "option[selected='selected']")
    
    def wait_dropdown_list_to_be_visible(self):
        try:
            self.wait.until(
                EC.visibility_of_element_located(self.DROPDOWN_LIST)
            ), "Dropdown list not visible"
        except Exception as e:
            print(f"Erreur : {e}")
         
    def get_dropdown_list(self):
        return self.driver.find_element(*self.DROPDOWN_LIST)       
    
    def select_an_option(self, value):
        Select(self.get_dropdown_list()).select_by_value(value)
        
    def get_selected_value(self):
        return self.driver.find_element(*self.SELECTED_OPTION).get_attribute("value")
    