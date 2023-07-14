import requests
from time import time
from multiprocessing import Pool

def download_image(url, index):
    print(f'file_{index} Download Start')
    img = requests.get(url)
    with open(f'./files/file_{index}.jpg', 'wb') as file:
            file.write(img.content)
    print(f'file_{index} Downloaded...')

if __name__ == '__main__':
    urls = []
    for i in range(5):
        resp = requests.get('https://api.unsplash.com/photos/random?client_id=xYthxZUbxBvv2cS_efL71BJPyVVEcncKMeYk518argw')
        url = resp.json()['urls']['full']
        urls.append(url)

    start = time()

    with Pool(processes=5) as pool:
        results = pool.starmap(download_image, list(zip(urls, range(5))))

    end = time()

    print(f'Total Time : {end - start} secs')
