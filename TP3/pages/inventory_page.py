from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage

class InventoryPage(BasePage):
    PATH: str = BasePage.URL + "inventory.html"
    
    INVENTORY_LIST = (By.CLASS_NAME, "inventory_list")
    
    def wait_inventory_list_to_be_visible(self):
        try:
            self.wait.until(
                EC.visibility_of_element_located(self.INVENTORY_LIST)
            ), "Inventory list not visible"
        except Exception as e:
            print(f"Erreur : {e}")
            
    def get_inventory_list(self):
        return self.driver.find_element(*self.INVENTORY_LIST)