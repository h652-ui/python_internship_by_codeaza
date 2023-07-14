import requests
from time import time

urls = []
for i in range(5):
    resp = requests.get('https://api.unsplash.com/photos/random?client_id=xYthxZUbxBvv2cS_efL71BJPyVVEcncKMeYk518argw')
    url = resp.json()['urls']['full']
    urls.append(url)

start = time()

for i, url in enumerate(urls):
    print(f'file_{i} Downloaded Start...')
    img = requests.get(url)
    with open(f'./files/file_{i}.jpg', 'wb') as file:
        file.write(img.content)
    print(f'file_{i} Downloaded...')
        
end = time()

print(f'Total Time : {end-start} secs')