from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage

class LoginPage(BasePage):
    URL: str = "https://the-internet.herokuapp.com/login"
    
    LOGIN_FORM = (By.ID, "login")
    USERNAME_INPUT = (By.ID, "username")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")
        
    def wait_login_form_to_be_visible(self):
        try:
            self.wait.until(
                EC.visibility_of_element_located(self.LOGIN_FORM)
            ), "Login form not visible"
        except Exception as e:
            print(f"Erreur : {e}")
        
    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login_button()
    
    def enter_username(self, username):
        self.driver.find_element(*self.USERNAME_INPUT).send_keys(username)
        
    def enter_password(self, password):
        self.driver.find_element(*self.PASSWORD_INPUT).send_keys(password)

    def click_login_button(self):
        self.driver.find_element(*self.LOGIN_BUTTON).click()
        
    def get_login_form(self):
        return self.driver.find_element(*self.LOGIN_FORM)