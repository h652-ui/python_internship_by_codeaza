import time
import re
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import math

# Set up Selenium options
firefox_options = Options()

# Create a new instance of the Firefox driver
driver = webdriver.Firefox(options=firefox_options)

credential = {'email': 'hkhan14112001@gmail.com', 'password': 'KHANSAHAB1a'}


# Define the URL of the laptop category on Daraz
url = "https://www.facebook.com/groups/programmercreatelife/members"

# Navigate to the laptop category
driver.get(url)

time.sleep(1)

email = driver.find_element(By.ID, 'email')
password = driver.find_element(By.ID, 'pass')
btn = driver.find_element(By.ID, 'loginbutton')

time.sleep(1)

email.send_keys(credential['email'])
password.send_keys(credential['password'])
btn.click()
time.sleep(5)

# Function to scroll to the end of the page
def scroll_to_end():
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

# Number of times to scroll to the end of the page
scroll_count = 5

# Scroll to the end of the page five times
for _ in range(scroll_count):
    scroll_to_end()
    time.sleep(1)  # Wait for 1 second after each scroll

membersDiv = driver.find_element(By.CSS_SELECTOR, 'div.xamitd3.x1sy10c2.xieb3on.x193iq5w.xrljuej')

elements = driver.find_elements(By.CSS_SELECTOR, 'div.x1lq5wgf.xgqcy7u.x30kzoy.x9jhf4c.x1lliihq')

links = []
for element in elements:
    link = element.find_element(By.CSS_SELECTOR, 'a.x1i10hfl.xjbqb8w.x6umtig.x1b1mbwd.xaqea5y.xav7gou.x9f619.x1ypdohk.xt0psk2.xe8uvvx.xdj266r.x11i5rnm.xat24cr.x1mh8g0r.xexx8yu.x4uap5.x18d9i69.xkhd6sd.x16tdsg8.x1hl2dhg.xggy1nq.x1a2a7pz.xt0b8zv.xzsf02u.x1s688f')
    match = re.search(r"user/(\d+)/", link.get_attribute('href'))
    links.append(match.group(1))

# Open a new browser window
driver.execute_script("window.open();")
driver.switch_to.window(driver.window_handles[-1])

for link in links:
    driver.get("https://www.facebook.com/profile.php?id="+str(link))
    

print(links)
    
driver.quit()