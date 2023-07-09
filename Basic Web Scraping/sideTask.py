import grequests
from bs4 import BeautifulSoup as bs
import re
from linksList import links
import pandas as pd

def get_data(urls):
    reqs = [grequests.get(link) for link in urls]
    resp = grequests.map(reqs)
    return resp

def parseData(responses):
    data = []
    for response in responses:
        sp = bs(response.text, 'lxml')
        product_url = response.url
        category = sp.find('div', {'class': 'breadcrumb-v2'})
        category_1 = re.sub(r'^\s+|\s+$', '', category.find_all('li')[2].text)
        category_2 = re.sub(r'^\s+|\s+$', '', category.find_all('li')[3].text)
        series = sp.find('h2', {'class': 'coleccion-name'}).text
        name = sp.find('h1', {'id': 'prod-name'}).text
        article = sp.find('p', {'id': 'prod-ref'}).text
        articleNum = re.sub(' ', '', article.split(':')[1])
        dim = sp.find('span', {'id': 'dim-txt'}).text
        matches = re.findall(r'\d+', dim)
        if len(matches) >= 3:
            length = matches[0]
            width = matches[1]
            height = matches[2]
        color = re.sub(r'\s', '', sp.find('span', {'id': f'ncollapse{articleNum}'}).text)
        type = sp.find(lambda tag: tag.name == "option" and tag.has_attr("selected"))
        type = '' if type is None else re.sub(r'\s', '', type.text)
        main_img = sp.find('img', {'data-finish': f'n-finished-{articleNum}'})
        main_img = sp.find(lambda tag: tag.name == "img" and tag.has_attr("data-finish"))['src'] if main_img is None else main_img['src']
        gallery = sp.find('div', {'id': 'productDetailThumbnailSlider'})
        gallery_images = list(map(lambda tag: tag['src'], gallery.find_all(lambda tag: tag.name == 'img' and f'n-finished-{articleNum}' not in tag.get('data-finish'))))
        short_description_section = sp.find('section', {'id': 'anclaProductFeat'})
        material = short_description_section.find('p', {'data-code': 'Material'}) 
        material = '' if material is None else re.sub('Material: ', '', material.text)
        short_description = list(map(lambda element: element.text, short_description_section.find_all('p')))
        data_sheet = list(map(lambda element: element['href'], sp.find_all('a', {'class': 'descarga'})))
        data_file_3d = sp.find('a', {'class': 'icon-stp'})
        data_file_3d = '' if data_file_3d is None else data_file_3d['href']
        long_description = sp.find('p', {'class': 'clamp'})
        if long_description:
            lD = long_description.text

        # Store the data in a dictionary
        data.append({
            'Category 1': category_1,
            'Category 2': category_2,
            'Series': series,
            'Name': name,
            'Color': color,
            'Type': type,
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


resp = get_data(links)
parseData(resp)