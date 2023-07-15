from time import time
from multiprocessing import Pool
from impFunctions import download_image, getLinks
import logging

# Set up logging
logging.basicConfig(filename='./logs/multiProcessing.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Import necessary modules and functions

# Check if the code is being executed as the main module
if __name__ == '__main__':
    # Get a list of URLs using the getLinks() function
    urls = getLinks()
    
    # Record the start time
    start = time()

    # Create a pool of processes with a maximum of 5 processes
    with Pool(processes=5) as pool:
        # Use starmap to apply the download_image function to each URL and index in parallel
        # zip(urls, range(5)) creates pairs of (url, index) for each URL and its corresponding index
        # starmap applies the download_image function to each pair of arguments in parallel
        results = pool.starmap(download_image, list(zip(urls, range(5))))

    # Record the end time
    end = time()

    # Calculate and print the total execution time
    print(f'Total Time : {end - start} secs')
