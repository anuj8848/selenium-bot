from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import re

def initialize_driver():
    """Initialize WebDriver"""
    service = ChromeService(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    return driver

def get_website_content(driver, url):
    """Get content of the website"""
    driver.get(url)
    return driver.find_element(By.XPATH, '/html').text

def find_matches(text):
    """Find matches in the text"""
    return re.findall(r'\b\w*Data\w*\b', text, re.IGNORECASE)

def quit_driver(driver):
    """Quit WebDriver"""
    driver.quit()

if __name__ == "__main__":
    driver = initialize_driver()
    website_content = get_website_content(driver, "https://www.datacamp.com/tutorial/pandas")
    matches = find_matches(website_content)
    print(len(matches))
    quit_driver(driver)
