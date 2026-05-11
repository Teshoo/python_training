from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage

class LoggedPage(BasePage):
    URL: str = "https://the-internet.herokuapp.com/secure"
    
    LOGOUT_BUTTON = (By.CSS_SELECTOR, "a[href='/logout']")
    SUCCESS_ALERT = (By.CLASS_NAME, "success")
            
    def wait_success_alert_to_be_visible(self):
        try:
            self.wait.until(EC.visibility_of_element_located(self.SUCCESS_ALERT)), "Success alert not visible"
        except Exception as e:
            print(f"Erreur : {e}")
            
    def wait_logout_button_to_be_visible(self):
        try:
            self.wait.until(EC.visibility_of_element_located(self.LOGOUT_BUTTON)), "Success alert not visible"
        except Exception as e:
            print(f"Erreur : {e}")
        
    def logout(self):
        self.click_logout_button()
        
    def click_logout_button(self):
        self.driver.find_element(*self.LOGOUT_BUTTON).click()
        
    def get_success_alert(self):
        return self.driver.find_element(*self.SUCCESS_ALERT)