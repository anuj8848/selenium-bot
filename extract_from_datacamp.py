from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep

def word_counter(word_list):
    count=0
    for word in word_list:
        if word=='data' or word=='Data' or word=='datas' or word=='Datas':
            count+=1
    return count


driver=webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()

driver.get("https://www.datacamp.com/tutorial/pandas")

link=driver.find_element(By.XPATH,'//*[@id="main-container"]/div[3]/aside[1]/div/div/nav/div/ul[1]/li/a').click()
content_page=driver.find_element(By.XPATH,'//*[@id="main-container"]/div[3]').text
word_list=content_page.split(" ")


print(word_counter(word_list))
driver.quit()