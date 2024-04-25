from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep

website=input("enter website to automate\n")
word2count=input('enter required word to count: ')



def word_counter(word,word_list):
    count=0
    for wrd in word_list:
        if wrd==word or wrd==word or wrd==word or wrd==word:
            count+=1
    return count


driver=webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()

driver.get(website)

link=driver.find_element(By.XPATH,'/html/body/div[4]').text
# content_page=driver.find_elements(By.XPATH,'//*[@id="main-container"]/div[3]').text
word_list=link.split(" ")


print(word_counter(word2count,word_list))
driver.quit()