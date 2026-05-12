from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class BasePage:
    URL: str = "https://www.saucedemo.com/"
    
    def __init__(self,driver,timeout=5):
        self.driver = driver
        self.wait = WebDriverWait(driver,timeout)

    def open(self, url):
        self.driver.get(url)
        
    def wait_url_to_be_correct(self, url):
        try:
            self.wait.until(EC.url_matches(url)), f"URL should be ${url}"
        except Exception as e:
            print(f"Error: {e}")