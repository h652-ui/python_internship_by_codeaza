from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

# Set up Selenium options
firefox_options = Options()

# Create a new instance of the Firefox driver
driver = webdriver.Firefox(options=firefox_options)

# Define the URL of the laptop category on Daraz
url = "https://www.daraz.pk/laptops/?spm=a2a0e.searchlistcategory.cate_7.5.1b74742cdOFlDu"

# Navigate to the laptop category
driver.get(url)


while(True):
    links = []
    try:
        WebDriverWait(driver=driver, timeout=10).until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, 'title--wFj93'))
        )
        elements = driver.find_elements(by=By.CLASS_NAME, value='title--wFj93')                            
    except Exception as e:
        print(f"Error: {str(e)}")
        break
    
    for element in elements:
        link = element.find_element(by=By.TAG_NAME, value='a')
        href = link.get_attribute("href")
        links.append(href)
    
    driver.execute_script("window.open();")
    driver.switch_to.window(driver.window_handles[-1])

    for link in links:
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
            print(title, price, details_list, rating)
        except Exception as e:
            print(f"Error: {str(e)}")
            break

    driver.close()
    driver.switch_to.window(driver.window_handles[0])
    wait = WebDriverWait(driver, 10)
    element = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'ant-pagination-next')))
    if(element.is_enabled):
        element.send_keys(Keys.RETURN)
    else:
        break
    time.sleep(5)
    
driver.quit()
