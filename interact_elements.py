import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


i=0
driver=webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

while i<3:
    driver.get("https://google.com")

    googleSearchBox=driver.find_element(By.ID,'APjFqb')
    googleSearchBox.send_keys("Automations")
    googleSearchBox.send_keys(Keys.ENTER)
    if i==0:
        change2Eng=driver.find_element(By.PARTIAL_LINK_TEXT,'Change to English')
        change2Eng.send_keys(Keys.ENTER)

    links=driver.find_element(By.PARTIAL_LINK_TEXT,'What Is Automation?')
    links.click()
    i+=1
    time.sleep(3)
      

    

driver.quit()

