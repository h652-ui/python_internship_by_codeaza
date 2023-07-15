import requests
import logging

# Function to download an image from a given URL
def download_image(url, index):
    logging.info(f'file_{index} Download Start')
    
    try:
        # Send a GET request to the URL to retrieve the image
        img = requests.get(url)
    except:
        logging.exception(f'Error Occured in downloading file_{index}')

    
    # Open a file in binary write mode and write the image content to it
    with open(f'./files/file_{index}.jpg', 'wb') as file:
        file.write(img.content)
        
    # Print a message indicating that the file has been downloaded
    logging.info(f'file_{index} Downloaded...')


# Function to retrieve a list of image URLs
def getLinks():
    urls = []
    try:
        # Loop to generate 5 random image URLs using the Unsplash API
        for i in range(5):
                # Send a GET request to the Unsplash API to get a random image
                resp = requests.get('https://api.unsplash.com/photos/random?client_id=xYthxZUbxBvv2cS_efL71BJPyVVEcncKMeYk518argw')
                
                # Extract the URL of the full-sized image from the API response
                url = resp.json()['urls']['full']
                
                # Add the URL to the list of URLs
                urls.append(url)
    except:
        logging.exception('Error Occured in Getting Links!')
    
    return urls
