from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
import time

# Set up Selenium options
firefox_options = Options()

# Create a new instance of the Firefox driver
driver = webdriver.Firefox(options=firefox_options)

# Open the website
url = "https://captcha.com/demos/features/captcha-demo.aspx"
driver.get(url)

# Find the captcha input field
captcha_field = driver.find_element(By.ID, "captchaCode")

# Pause and ask the user to enter the captcha
captcha_input = input("Please enter the captcha: ")

# Enter the captcha value into the input field
captcha_field.send_keys(captcha_input)

# Find the "Validate" button and click on it
validate_button = driver.find_element(By.ID, "validateCaptchaButton")
validate_button.click()

time.sleep(10)
# Close the browser
driver.quit()
