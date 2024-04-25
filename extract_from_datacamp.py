from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep

driver=webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()

driver.get("https://www.datacamp.com/tutorial/pandas")

link=driver.find_element(By.XPATH,'//*[@id="main-container"]/div[3]/aside[1]/div/div/nav/div/ul[1]/li/a').click()
sleep(3)
content_page=driver.find_element(By.XPATH,'//*[@id="main-container"]/div[3]').text
word_list=content_page.split(" ")
count=0
for i in word_list:
    if i=='data' or i=='Data' or i=='datas' or i=='Datas':
        count+=1
print(count)
sleep(3)
driver.quit()