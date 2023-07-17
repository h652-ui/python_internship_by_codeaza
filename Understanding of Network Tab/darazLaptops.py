import requests

print('\nThis Program fetch all Laptop Varieties from Daraz\n')

url = 'https://www.daraz.pk/laptops/?ajax=true&page=3&spm=a2a0e.home.cate_7.5.35e34076HUfi7I'

resp = requests.get(url)
mods = resp.json()['mods']
items = mods['listItems']

for item in items:
    name = item['name']
    url = item['productUrl']
    print(f"\nName of Laptop: {name}")
    print(f"URL of Laptop:  {url}\n")