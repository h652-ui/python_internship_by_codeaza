import logging
import threading
import time
import schedule
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from database import insert_data, cnx

def script():
    # Set up logging
    logging.basicConfig(filename='project.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

    # Set up Selenium options
    firefox_options = Options()

    # Create a new instance of the Firefox driver
    driver = webdriver.Firefox(options=firefox_options)

    # Define the URL of the laptop category on Daraz
    url = "https://www.daraz.pk/laptops/?spm=a2a0e.searchlistcategory.cate_7.5.1b74742cdOFlDu"

    # Navigate to the laptop category
    driver.get(url)

    while True:
        links = []
        try:
            WebDriverWait(driver=driver, timeout=10).until(
                EC.presence_of_all_elements_located((By.CLASS_NAME, 'title--wFj93'))
            )
            elements = driver.find_elements(by=By.CLASS_NAME, value='title--wFj93')
        except Exception as e:
            logging.error(f"Error: {str(e)}")
            break

        for element in elements:
            link = element.find_element(by=By.TAG_NAME, value='a')
            href = link.get_attribute("href")
            links.append(href)

        driver.execute_script("window.open();")
        driver.switch_to.window(driver.window_handles[-1])

        for link in links:
            reviews = []
            driver.get(link)
            try:
                WebDriverWait(driver=driver, timeout=10).until(
                    EC.presence_of_all_elements_located((By.CLASS_NAME, 'pdp-mod-product-badge-title'))
                )
                title = driver.find_element(By.CLASS_NAME, 'pdp-mod-product-badge-title').text
                price_string = driver.find_element(By.CLASS_NAME, 'pdp-price').text
                price = int(price_string.replace("Rs.", "").replace(",", ""))
                div_of_lis = driver.find_element(By.CLASS_NAME, 'pdp-product-highlights')
                list_of_lis = div_of_lis.find_elements(By.TAG_NAME, 'li')
                wait = WebDriverWait(driver, 10)
                section_element = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'pdp-view-more-btn')))
                driver.execute_script("arguments[0].scrollIntoView();", section_element)
                rating_span = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'score-average')))
                rating = float(rating_span.text)
                details_list = []
                for li in list_of_lis:
                    details_list.append(li.text)
                items = driver.find_elements(By.CLASS_NAME, 'item')
                for item in items:
                    # Find 'item-content' div
                    item_content = item.find_element(By.CLASS_NAME, "item-content")
                    comment = item_content.find_element(By.CLASS_NAME, 'content').text
                    # Find 'seller-reply-wrapper' div (if exists)
                    seller_reply_wrapper = None
                    try:
                        seller_reply_wrapper = item.find_element(By.CLASS_NAME, "seller-reply-wrapper")
                    except:
                        pass

                    if seller_reply_wrapper:
                        # Find 'content' div inside 'seller-reply-wrapper'
                        seller_reply_content = seller_reply_wrapper.find_element(By.CLASS_NAME, "content")
                        reply = seller_reply_content.text
                        reviews.append([comment, reply])
                    else:
                        # Only append 'item-content' text to the result list
                        reviews.append([comment])

                data = [title, price, rating, details_list, reviews]
                # Insert the data into the database in a separate thread
                thread = threading.Thread(target=insert_data, args=(data,))
                thread.start()
                time.sleep(1)  # Delay before continuing to the next iteration
            except Exception as e:
                logging.error(f"Error: {str(e)}")
                break

        driver.close()
        driver.switch_to.window(driver.window_handles[0])
        wait = WebDriverWait(driver, 10)
        element = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'ant-pagination-next')))
        if element.is_enabled:
            element.send_keys(Keys.RETURN)
        else:
            break
        time.sleep(5)

    driver.quit()
    cnx.close()

# Schedule the script to run every Tuesday at 11:00 AM
schedule.every().tuesday.at("11:00").do(script)

# Run the schedule loop
while True:
    schedule.run_pending()
    time.sleep(1)