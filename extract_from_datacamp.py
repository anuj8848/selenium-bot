from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
import re



driver=webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()

driver.get("https://www.datacamp.com/tutorial/pandas")

link=driver.find_element(By.XPATH,'/html').text
# content_page=driver.find_element(By.XPATH,'//*[@id="main-container"]/div[3]').text

matches = re.findall(r'\b\w*Data\w*\b', link, re.IGNORECASE)
print(len(matches))


driver.quit()