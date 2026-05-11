from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class ARElementsPage(BasePage):
    URL: str = "https://the-internet.herokuapp.com/add_remove_elements/"
    
    ADD_ELEMENT_BUTTON = (By.CSS_SELECTOR, "button[onclick='addElement()']")
    DELETE_ELEMENT_BUTTON = (By.CSS_SELECTOR, "button[onclick='deleteElement()']")
    
    def wait_add_element_button_to_be_visible(self):
        try:
            self.wait.until(
                EC.visibility_of_element_located(self.ADD_ELEMENT_BUTTON)
            ), "Add Element button not visible"
        except Exception as e:
            print(f"Erreur : {e}")
         
    def click_on_add_element_button(self):
        self.get_add_element_button().click()
        
    def click_on_first_delete_element_button(self):
        self.get_delete_element_buttons()[0].click()
        
    def delete_all_elements(self):
        for e in enumerate(self.get_delete_element_buttons()):
            e[1].click()
            
    def get_add_element_button(self):
        return self.driver.find_element(*self.ADD_ELEMENT_BUTTON)       

    def get_delete_element_buttons(self):
        return self.driver.find_elements(*self.DELETE_ELEMENT_BUTTON)
