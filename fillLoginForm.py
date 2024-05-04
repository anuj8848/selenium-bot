'''
this is a simple program automates the login and and getting content of table task.
You have to give your email and password once.
'''


from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def initialize_driver():
    return webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

def login(driver, email, password):
    driver.get("https://websiteexample.com/")  # your website
    
    """ Login Form """
    
    # get element for entering email through XPATH
    get_email = driver.find_element(By.XPATH,'replace this by xpath of email element')
    get_email.send_keys(email)
    # get element for entering password through XPATH
    get_passwd = driver.find_element(By.XPATH,'replace this by xpath of password element')
    get_passwd.send_keys(password)
    
    # get and click login button through XPATH
    driver.find_element(By.XPATH,'replace this by xpath of login button').click()
    sleep(5)

def get_project_table(driver):
    # get project table using XPATH
    project_table = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,'replace this by xpath of required table element')))
    return project_table

def extract_table_data(table_element):
    # extract content of table in a list
    table_data = []
    rows = table_element.find_elements(By.TAG_NAME,"tr")
    for row in rows:
        row_data = []
        cells = row.find_elements(By.TAG_NAME,"td")
        for cell in cells:
            row_data.append(cell.text)
        table_data.append(row_data)
    return table_data

def display_name(table_data):
    # row[2] contains project name,there project name is printed
    project_name = [row[2] for row in table_data]
    print(project_name)

def main():
    driver = initialize_driver()
    login(driver, "your_email", "your_password")
    project_table = get_project_table(driver)
    table_data = extract_table_data(project_table)
    display_name(table_data)
    driver.quit()

if __name__ == "__main__":
    main()
