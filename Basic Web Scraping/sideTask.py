import grequests
from bs4 import BeautifulSoup as bs
import re
from linksList import links
import pandas as pd

# Function to send asynchronous HTTP requests to multiple URLs
def get_data(urls):
    reqs = [grequests.get(link) for link in urls]
    resp = grequests.map(reqs)
    return resp

# Function to parse the HTML responses and extract data
def parseData(responses):
    data = []
    for response in responses:
        sp = bs(response.text, 'lxml')  # Create BeautifulSoup object to parse HTML
        product_url = response.url  # Get the URL of the current product
        category = sp.find('div', {'class': 'breadcrumb-v2'})  # Find the category information in the HTML
        category_1 = re.sub(r'^\s+|\s+$', '', category.find_all('li')[2].text)  # Extract the first category
        category_2 = re.sub(r'^\s+|\s+$', '', category.find_all('li')[3].text)  # Extract the second category
        series = sp.find('h2', {'class': 'coleccion-name'}).text  # Extract the series name
        name = sp.find('h1', {'id': 'prod-name'}).text  # Extract the product name
        article = sp.find('p', {'id': 'prod-ref'}).text  # Extract the article number
        articleNum = re.sub(' ', '', article.split(':')[1])  # Clean the article number
        dim = sp.find('span', {'id': 'dim-txt'}).text  # Extract the dimensions
        matches = re.findall(r'\d+', dim)  # Extract numerical values from the dimensions
        if len(matches) >= 3:
            length = matches[0]
            width = matches[1]
            height = matches[2]
        color = re.sub(r'\s', '', sp.find('span', {'id': f'ncollapse{articleNum}'}).text)  # Extract the color
        type = sp.find(lambda tag: tag.name == "option" and tag.has_attr("selected"))  # Find the selected option (type)
        type = '' if type is None else re.sub(r'\s', '', type.text)  # Extract the type
        main_img = sp.find('img', {'data-finish': f'n-finished-{articleNum}'})  # Find the main image
        main_img = sp.find(lambda tag: tag.name == "img" and tag.has_attr("data-finish"))['src'] if main_img is None else main_img['src']  # Extract the main image URL
        gallery = sp.find('div', {'id': 'productDetailThumbnailSlider'})  # Find the image gallery
        gallery_images = list(map(lambda tag: tag['src'], gallery.find_all(lambda tag: tag.name == 'img' and f'n-finished-{articleNum}' not in tag.get('data-finish'))))  # Extract gallery image URLs
        short_description_section = sp.find('section', {'id': 'anclaProductFeat'})  # Find the short description section
        material = short_description_section.find('p', {'data-code': 'Material'})  # Find the material information
        material = '' if material is None else re.sub('Material: ', '', material.text)  # Extract the material
        short_description = list(map(lambda element: element.text, short_description_section.find_all('p')))  # Extract short description paragraphs
        data_sheet = list(map(lambda element: element['href'], sp.find_all('a', {'class': 'descarga'})))  # Extract data sheet URLs
        data_file_3d = sp.find('a', {'class': 'icon-stp'})  # Find the 3D data file
        data_file_3d = '' if data_file_3d is None else data_file_3d['href']  # Extract the 3D data file URL
        long_description = sp.find('p', {'class': 'clamp'})  # Find the long description
        if long_description:
            lD = long_description.text  # Extract the long description

        # Store the data in a dictionary
        data.append({
            'Category 1': category_1,
            'Category 2': category_2,
            'Series': series,
            'Name': name,
            'Color': color,
            'Type': type,
            'lenght': length,
            'width': width,
            'height': height,
            'Main Image': main_img,
            'Gallery Images': gallery_images,
            'Material': material,
            'Short Description': short_description,
            'Data File 3D': data_file_3d,
            'Long Description': lD,
            'Product URL' :product_url
        })

    # Create a DataFrame from the data
    df = pd.DataFrame(data)

    # Save the DataFrame to an Excel file
    df.to_excel('output.xlsx', index=False)

# Get the data from the provided links
resp = get_data(links)

# Parse the data and save it to an Excel file
parseData(resp)
