# Import necessary modules and functions
from time import time
from impFunctions import getLinks, download_image
import logging

# Set up logging
logging.basicConfig(filename='./logs/downloadImages.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Get a list of URLs using the getLinks() function
urls = getLinks()

# Record the start time
start = time()

# Iterate over the URLs and download images using the download_image() function
for i, url in enumerate(urls):
    download_image(url, i)

# Record the end time
end = time()

# Calculate and print the total execution time
print(f'Total Time : {end-start} secs')
logging.info(f'Total Time : {end-start} secs')
