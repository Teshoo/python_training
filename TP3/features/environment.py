from selenium import webdriver
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

def before_scenario(context, scenario):
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()
    context.login_page = LoginPage(context.driver)
    context.inventory_page = InventoryPage(context.driver)

def after_scenario(context, scenario):
    context.driver.quit()