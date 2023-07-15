import threading
from time import time
from impFunctions import download_image, getLinks
import logging

# Set up logging
logging.basicConfig(filename='./logs/multiProcessing.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Import necessary modules and functions

# Get a list of URLs using the getLinks() function
urls = getLinks()

# Create an empty list to store the threads
threads = []

# Record the start time
start = time()

# Iterate over the URLs and create a thread for each URL
for i, url in enumerate(urls):
    # Create a new thread with the target function set to download_image
    # and arguments (url, i)
    thread = threading.Thread(target=download_image, args=(url, i))
    
    # Start the thread
    thread.start()
    
    # Add the thread to the list of threads
    threads.append(thread)

# Wait for all the threads to complete
for thread in threads:
    thread.join()

# Record the end time
end = time()

# Calculate and print the total execution time
print(f'Total Time : {end - start} secs')
