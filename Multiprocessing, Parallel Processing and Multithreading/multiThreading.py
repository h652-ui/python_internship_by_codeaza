import requests
import threading
from time import time

def download_image(url, index):
    print(f'file_{index} Download Start')
    img = requests.get(url)
    with open(f'./files/file_{index}.jpg', 'wb') as file:
            file.write(img.content)
    print(f'file_{index} Downloaded...')

urls = []
for i in range(5):
    resp = requests.get('https://api.unsplash.com/photos/random?client_id=xYthxZUbxBvv2cS_efL71BJPyVVEcncKMeYk518argw')
    url = resp.json()['urls']['full']
    urls.append(url)

threads = []
start = time()
for i in range(5):
    thread = threading.Thread(target=download_image, args=(url, i))
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()

end = time()
print(f'Total Time : {end - start} secs')