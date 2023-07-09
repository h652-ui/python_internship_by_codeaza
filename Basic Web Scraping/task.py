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

# Define the URL of the laptop category on Daraz
url = "https://www.laufen.co.at/produkte"

# Navigate to the laptop category
driver.get(url)

mainLinks = []

# Find the category element
category = driver.find_element(By.CLASS_NAME, 'portlet-boundary')

# Find sub-categories within the category
sub_categories = driver.find_elements(By.CLASS_NAME, 'content-wrapper')

links = []
for index, sub in enumerate(sub_categories):
    # Get the link of each sub-category
    link = sub.find_element(By.TAG_NAME, 'a').get_attribute('href')
    if(index != 0):
        links.append(link)
    if index == 3:
        break

# Accept cookie consent
driver.find_element(By.ID, 'onetrust-accept-btn-handler').click()

# Open a new browser window
driver.execute_script("window.open();")
driver.switch_to.window(driver.window_handles[-1])

for link in links:
    driver.get(link)

    # Get the text indicating the total number of products and pages
    getText = driver.find_element(By.ID, 'nextButtonTotalsSpan').text
    result = re.findall(r'\d+', getText)

    pages = 1
    if len(result) == 2:
        # Calculate the number of pages
        pages = math.floor(int(result[1]) / int(result[0]))

    for pageNo in range(1, pages + 1):
        n_link = f"{link}?page={pageNo}"
        driver.get(n_link)
        sub_links = []

        # Find elements representing individual product links
        sub_links_elements = driver.find_elements(By.CLASS_NAME, 'title-producto')

        for sub_link_element in sub_links_elements:
            # Get the URL of each product
            lin = sub_link_element.find_element(By.TAG_NAME, 'a').get_attribute('href')
            sub_links.append(lin)

        # Open a new browser window
        driver.execute_script("window.open();")
        driver.switch_to.window(driver.window_handles[-1])

        for li in sub_links:
            driver.get(li)

            # Find all available options for the product
            elements = driver.find_elements(By.TAG_NAME, 'option')
            options = []
            for element in elements:
                options.append(element.get_attribute('data-value'))

            for option in options:
                # Select each option one by one
                clickable = driver.find_element(By.CSS_SELECTOR, f"option[data-value='{option}']")
                clickable.click()

                # Wait for the select element to be clickable
                wait = WebDriverWait(driver, 10)
                wait.until(EC.element_to_be_clickable((By.TAG_NAME, 'select')))

                element = driver.find_element(By.CLASS_NAME, 'colors')
                elements = element.find_elements(By.CLASS_NAME, 'fondo')

                for element in elements:
                    # Click on each color option
                    element.click()
                    time.sleep(1)
                    mainLinks.append(driver.current_url)

        # Close the current browser window
        driver.close()
        driver.switch_to.window(driver.window_handles[-1])

# Quit the browser
driver.quit()
