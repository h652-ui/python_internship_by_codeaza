from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
import time

# Set up Selenium options
firefox_options = Options()

# Create a new instance of the Firefox driver
driver = webdriver.Firefox(options=firefox_options)

# Define the URL of the laptop category on Daraz
url = "https://meet.google.com/"

# Navigate to the laptop category
driver.get(url)

element = driver.find_element(by=By.CLASS_NAME, value='glue-button--high-emphasis')
element.click()
time.sleep(5)

driver.close()