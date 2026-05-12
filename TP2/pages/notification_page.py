from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class NotificationPage(BasePage):
    URL: str = "https://the-internet.herokuapp.com/notification_message_rendered"
    
    CLICK_HERE_BUTTON = (By.CSS_SELECTOR, "a[href='/notification_message']")
    NOTIFICATION_TEXT = (By.CSS_SELECTOR, "div#flash")
    
    NOTIFICATION_MESSAGE = {
            'success': "Action successful",
            'unsuccesful': "Action unsuccesful, please try again",
            'unsuccessful': "Action unsuccessful, please try again"   
        }
    
    def get_notification_text(self):
        return self.driver.find_element(*self.NOTIFICATION_TEXT).text
    
    def click_on_click_here_button(self):
        self.driver.find_element(*self.CLICK_HERE_BUTTON).click()
        
    def wait_notification_to_be_visible(self):
        try:
            self.wait.until(
                EC.visibility_of_element_located(self.NOTIFICATION_TEXT)
            ), "Notification not visible"
        except Exception as e:
            print(f"Erreur : {e}")
            
    def is_a_correct_notification_message(self):
        for i, e in enumerate(self.NOTIFICATION_MESSAGE.items()):
            if e[1] in self.get_notification_text():
                return True
        return False